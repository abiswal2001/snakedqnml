""" Player class which represents a player playing snake. """

""" Necessary imports """
import random
import pickle
import ComputerSnake


""" Importing tf agents """
import tensorflow as tf

from tf_agents.agents.dqn import dqn_agent
from tf_agents.drivers import dynamic_step_driver
from tf_agents.environments import suite_gym
from tf_agents.environments import tf_py_environment
from tf_agents.eval import metric_utils
from tf_agents.metrics import tf_metrics
from tf_agents.networks import q_network
from tf_agents.policies import random_tf_policy
from tf_agents.replay_buffers import tf_uniform_replay_buffer
from tf_agents.trajectories import trajectory
from tf_agents.utils import common
from tf_agents.replay_buffers import tf_uniform_replay_buffer


""" SIMULATION VARIABLES

Number of iterations the simulation runs """
num_iterations = 1000000

""" Initial amount of data points """
initial_collect_steps = 1000

""" Data collected each time the simulation is run """
collect_steps_per_iteration = 1

""" """
replay_buffer_max_length = 100000

batch_size = 64
learning_rate = 1e-3
log_interval = 1000

num_eval_episodes = 5
eval_interval = 1000000


""" Creates a game the computer can simulate snake. """
def simulate():
    # Set up the environments for the agent to train and test its performance
    envTrain = ComputerSnake.Snake()
    envEval = ComputerSnake.Snake()

    # Convert and wrap in TFPyEnvironment training and evaluation environments
    train_env = tf_py_environment.TFPyEnvironment(envTrain)
    eval_env = tf_py_environment.TFPyEnvironment(envEval)

    # Set up q network with necessary parameters
    fc_layer_params = (100,)
    q_net = q_network.QNetwork(
        train_env.observation_spec(),
        train_env.action_spec(),
        fc_layer_params=fc_layer_params
    )
    optimizer = tf.compat.v1.train.AdamOptimizer(learning_rate=learning_rate) # look up
    train_step_counter = tf.Variable(0)

    # Set up and initialize the DQN learning agent. It takes in the time_step spec,
    # action spec, the q network, the optimizer, a loss function, and train_step_counter
    agent = dqn_agent.DqnAgent(
        train_env.time_step_spec(),
        train_env.action_spec(),
        q_network=q_net,
        optimizer=optimizer, # look up
        td_errors_loss_fn=common.element_wise_squared_loss,
        train_step_counter=train_step_counter
    )
    agent.initialize()

    # Set up policies the agent can use
    eval_policy = agent.policy
    collect_policy = agent.collect_policy

    # Policy which randomly selects actions for each step
    random_policy = random_tf_policy.RandomTFPolicy(train_env.time_step_spec(),
                                                    train_env.action_spec())

    #Buffer to store previous states
    replay_buffer = tf_uniform_replay_buffer.TFUniformReplayBuffer(
    data_spec=agent.collect_data_spec,
    batch_size=train_env.batch_size,
    max_length=replay_buffer_max_length)

    # Dataset generates trajectories with shape [Bx2x...] This is so that the agent has access to both the current
    # and previous state to compute loss. Parallel calls and prefetching are used to optimize process.
    dataset = replay_buffer.as_dataset(
        num_parallel_calls=3,
        sample_batch_size=batch_size,
        num_steps=2).prefetch(3)
    iterator = iter(dataset)

    # (Optional) Optimize by wrapping some of the code in a graph using TF function.
    agent.train = common.function(agent.train)

    # Reset the train step
    agent.train_step_counter.assign(0)

    # Evaluate the agent's policy once before training.
    avg_return = compute_avg_return(eval_env, agent.policy, num_eval_episodes)
    returns = [avg_return]

    # We initially fill the replay buffer with 100 trajectories to help the assistant
    collect_data(train_env, random_policy, replay_buffer, steps=5000)
    train_env.reset()

    # Here, we run the simulation to train the agent
    for _ in range(num_iterations):
        # Collect a few steps using collect_policy and save to the replay buffer.
        for _ in range(collect_steps_per_iteration):
            collect_step(train_env, agent.collect_policy, replay_buffer)

        # Sample a batch of data from the buffer and update the agent's network.
        experience, unused_info = next(iterator)
        train_loss = agent.train(experience).loss

        # Number of training steps so far
        step = agent.train_step_counter.numpy()

        # Prints the training loss every 200 steps
        if step % log_interval == 0:
           print('Moves made = {0}'.format(step))

        # Evaluates the agent's policy every 1000 steps and prints results
        if step % eval_interval == 0:
            avg_return = compute_avg_return(eval_env, agent.policy, num_eval_episodes)
            print('step = {0}: Average Return = {1}'.format(step, avg_return))
            returns.append(avg_return)

""" Computes the average reward of an policy with specified environment and trials.
This method plays out NUM_EPISODES number of full games of snake to get the average return.
This does not play a certain number of games of snake to get the return. """
def compute_avg_return(environment, policy, num_episodes=10):
  # Total sum of all the returns
  total_return = 0.0

  # Number of games it should run before returning the average_return
  for _ in range(num_episodes):

    time_step = environment.reset()
    episode_return = 0.0

    # While the snake is not dead
    while not time_step.is_last():
      # Gets the next action based on the current state
      action_step = policy.action(time_step)

      # Makes the next action
      time_step = environment.step(action_step.action)

      # Adds the reward of whatever action was made
      episode_return += time_step.reward
    total_return += episode_return

  # Calculate the return, print it, and return it.
  avg_return = total_return / num_episodes
  print(avg_return)
  return avg_return.numpy()[0]

""" Executes a policy in a specified environment and stores replay data in the buffer """
def collect_step(environment, policy, buffer):
  time_step = environment.current_time_step()
  action_step = policy.action(time_step)
  next_time_step = environment.step(action_step.action)
  traj = trajectory.from_transition(time_step, action_step, next_time_step)

  # Add trajectory to the replay buffer
  buffer.add_batch(traj)

""" Collects replay data for a specified number of trials """
def collect_data(env, policy, buffer, steps):
  for _ in range(steps):
    collect_step(env, policy, buffer)
