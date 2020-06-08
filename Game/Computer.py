""" Player class which represents a player playing snake. """

# Necessary imports
import random
import pickle
import ComputerSnake
import utils

num_iterations = 20000 

initial_collect_steps = 1000  
collect_steps_per_iteration = 1  
replay_buffer_max_length = 100000  

batch_size = 64  
learning_rate = 1e-3 
log_interval = 200  

num_eval_episodes = 10  
eval_interval = 1000


""" Creates a game the computer can simulate snake. """
def simulate():
    envTrain = ComputerSnake.Snake()
    envEval = ComputerSnake.Snake()
    #utils.validate_py_environment(env, episodes=5)
    train_env = tf_py_environment.TFPyEnvironment(envTrain)
    eval_env = tf_py_environment.TFPyEnvironment(envEval)
    fc_layer_params = (100,)
    q_net = q_network.QNetwork(
        train_env.observation_spec(),
        train_env.action_spec(),
        fc_layer_params=fc_layer_params
    )
    optimizer = tf.compat.v1.train.AdamOptimizer(learning_rate=learning_rate)
    train_step_counter = tf.Variable(0)
    agent = dqn_agent.DqnAgent(
        train_env.time_step_spec(),
        train_env.action_spec(),
        q_network=q_net,
        optimizer=optimizer,
        td_errors_loss_fn=common.element_wise_squared_loss,
        train_step_counter=train_step_counter
    )
    agent.initialize()
    eval_policy = agent.policy
    collect_policy = agent.collect_policy
    random_policy = random_tf_policy.RandomTFPolicy(train_env.time_step_spec(),train_env.action_spec())
    
def compute_avg_return(environment, policy, num_episodes=10):
  total_return = 0.0
  for _ in range(num_episodes):

    time_step = environment.reset()
    episode_return = 0.0

    while not time_step.is_last():
      action_step = policy.action(time_step)
      time_step = environment.step(action_step.action)
      episode_return += time_step.reward
    total_return += episode_return

  avg_return = total_return / num_episodes
  return avg_return.numpy()[0]


def collect_step(environment, policy, buffer):
  time_step = environment.current_time_step()
  action_step = policy.action(time_step)
  next_time_step = environment.step(action_step.action)
  traj = trajectory.from_transition(time_step, action_step, next_time_step)

  # Add trajectory to the replay buffer
  buffer.add_batch(traj)

def collect_data(env, policy, buffer, steps):
  for _ in range(steps):
    collect_step(env, policy, buffer)


""" Sets up persistence of the stored moves."""
def persistence():
    with open('Simulations/simulation1test.txt', 'wb') as sim_moves:
        pickle.dump(moves, sim_moves)