""" Snake game without the GUI"""

# Necessary Imports
import random
import abc
import tensorflow as tf
import numpy as np
import pickle
import math

# Importing tf agents
from tf_agents.environments import py_environment
from tf_agents.environments import tf_environment
from tf_agents.environments import tf_py_environment
from tf_agents.environments import utils
from tf_agents.specs import array_spec
from tf_agents.environments import wrappers
from tf_agents.environments import suite_gym
from tf_agents.trajectories import time_step as ts

tf.compat.v1.enable_v2_behavior()

class Snake(py_environment.PyEnvironment):
    """A class which plays the primary portion of the snake game while
    receiving moves to play from other player classes. """

    """ Setup for the simulation which will run multiple games."""
    def __init__(self, num_iterations = 20000):
        self._action_spec = array_spec.BoundedArraySpec((), dtype=np.int32, minimum=0, maximum=3, name='action')
        self._observation_spec = array_spec.BoundedArraySpec((7,), dtype=np.int32, minimum=[0, -1, -1, 0, 0, 0, 0], maximum=[4, 1, 1, 1, 1, 1, 1], name='observation')
        self._state = [0, 1, 0, 1, 1, 1, 1]
        self.max_iterations = num_iterations - 1
        self.move_limit = 1000
        self.curr_moves = 0
        self.num_games = -1
        self.fruit_locations = []
        self.all_fruit = []
        self.all_moves = []
        self.all = []
        self.newGame()

    def action_spec(self):
        return self._action_spec

    def observation_spec(self):
        return self._observation_spec

    """ Creates a new game with the snake and fruit in the default positions. """
    def newGame(self):
        # Snake Body which only contains the head at this point
        self.snakeBody = [[20, 20]]

        # Initial Fruit Location
        self.fruit = [25, 20]

        # A dictionary which contains all possible locations that a fruit can be at.
        self.openLocations = {}
        for i in range(30):
            for j in range(30):
                self.openLocations[i + 30 * j] = [i + 5, j + 5]

        # Default direction which the snake will be moving in
        self.dir = 1

        # Set initial score to 1
        self.score = 1

        # Set the snake to be alive.
        self.dead = False

        # List of all the moves
        self.moves = []

        # Creates an array with all the fruit locations stored
        self.fruit_locations = []
        self.fruit_locations.append(self.fruit[:])

        # Sets the number of moves for this turn to 0
        self.curr_moves = 0


    """ Restarts the game with the initial conditions of the snake and fruit.
    Also (reset)s the state variable to represent the current locations. """
    def _reset(self):
        # Resets the state to the initial state
        self._state = np.array([0, 1, 0, 1, 1, 1, 1], dtype=np.int32)

        # Makes the snake alive again
        self.dead = False

        # Writes the moves to the persistence file so we can see what the computer did later.
        if ((self.num_games % 10 == 0) or self.score >= 4):
           self.all_moves.append(self.moves)
           self.all_fruit.append(self.fruit_locations)
           self.all = [self.all_moves, self.all_fruit]
           self.persistence()

        # Increments num_games because a game just ended.
        self.num_games += 1

        # Resets the parameters of the snake to the initial parameters
        self.newGame()

        # Tells tensor flow to restart with the new state
        return ts.restart(self._state)

    """ Method which is called on when the snake is going to make a move. """
    def _step(self, action):
        # Starts a new game if the snake is
        action = action + 1
        if self.dead:
            return self.reset()

        # Action represents the direction that the snake will move in.
        elif action >= 1 and action <= 4:
            self.setDir(action)

        # Error if an illegal move was passed in.
        else:
            raise ValueError('Direction must be between 1 and 4')

        # Reward represents the score of the snake in the current position.
        reward = 0.0
        discount = 0.0

        # Checks to see if the snake head reaches a fruit
        eaten = self.checkFruit()

        # Moves the snake based on the current direction. Head is a copy
        #(different pointer) of the array in snakeBody[0].
        head = self.snakeBody[0][:]

        oldDistance = self.fruitDistance(head)

        # Right
        if (self.dir == 1):
            head[0] += 1
        # Left
        elif (self.dir == 2):
            head[0] -= 1
        # Down
        elif (self.dir == 3):
            head[1] -= 1
        # Up
        else:
            head[1] += 1

        # Adds to the number of moves after a move is made.
        self.curr_moves += 1

        newDistance = self.fruitDistance(head)

        # Distance reward, not sure if it worked or not.
        """ if (newDistance < oldDistance):
            reward -= 0.5
        elif (newDistance > oldDistance):
            reward += 0.5 """
            
        # Adds the next move to the list of all the moves that were made.
        self.moves.append(self.dir)

        # Inserts the new head as the first item of snakeBody to represent a move.
        self.snakeBody.insert(0, head)

        # Only continues if game has not ended
        if ((not self.checkLose()) and (self.curr_moves < self.move_limit)):
            # Removes head from openLocations to represent that that square is taken.
            key = convertToKey(head)
            self.openLocations.pop(convertToKey(head))

             # Removes last body part if fruit was not eaten
            if (not eaten):
                removed = self.snakeBody.pop()
                self.openLocations[convertToKey(removed)] = removed

            # Creates a new fruit if the fruit was eaten and increments score and reward.
            else:
                self.fruit = self.newFruit()
                self.fruit_locations.append(self.fruit[:])
                self.updateScore()
                reward -= 10.0

            # Assign the state to be the new state based on the snake head's new location
            fruit_dir_arr = self.dirFruit()
            # Array of the current danger conditions based on the location of the snake head.
            danger_arr = self.danger(action)
            self._state = np.array([action - 1, fruit_dir_arr[0], fruit_dir_arr[1], danger_arr[0], danger_arr[1], danger_arr[2], danger_arr[3]], dtype=np.int32)
            return ts.transition(self._state, reward, discount=1.0)

        # If the snake has lost the game, this is ran
        else:
            self.dead = True
            reward += 5.0
            return ts.termination(self._state, reward)


    """ Calculates direction of fruit, returns array storing horiz, vert direction. Follows cartesian plane conventions """
    def dirFruit(self):
        retDir = [0, 0]
        head = self.snakeBody[0][:]
        fruit = self.fruit[:]
        if head[0] < fruit[0]:
            retDir[0] = 1
        elif head[0] > fruit[0]:
            retDir[0] = -1
        if head[1] < fruit[1]:
            retDir[1] = 1
        elif head[1] > fruit[1]:
            retDir[1] = -1
        return retDir

    """ Returns direction in which the snake will self-destruct, if snake length is longer than 1 """
    def dangerDir(self, currD):
        #if len(self.snakeBody) < 2:
        #    return -1
        if currD == 1:
            return 2
        elif currD == 2:
            return 1
        elif currD == 3:
            return 4
        elif currD == 4:
            return 3


    """ Danger value based on self-collision and wall collision.
    0 for danger, 1 for no danger. Returns an array which has
    stored all those danger values."""
    def danger(self, currD):
        head = self.snakeBody[0][:]
        neighborUp = int(convertToKey([head[0], head[1] + 1]) in self.openLocations)
        neighborDown = int(convertToKey([head[0], head[1] - 1]) in self.openLocations)
        neighborLeft = int(convertToKey([head[0] - 1, head[1]]) in self.openLocations)
        neighborRight = int(convertToKey([head[0] + 1, head[1]]) in self.openLocations)
        selfDestructDir = self.dangerDir(currD)
        arr = [neighborRight, neighborLeft, neighborDown, neighborUp]
        #if selfDestructDir > -1:
        arr[selfDestructDir - 1] = 0
        return np.array(arr, dtype=np.int32)

    """ Increments the score """
    def updateScore(self):
        self.score += 1

    """ Changes the direction that the snake moves in.
    This essentially represents players playing the game. """
    def setDir(self, dir):
        self.dir = dir

    """ Checks to see if the game is over """
    def checkLose(self):
        head = self.snakeBody[0]

        # Checks to see if the snake collides without itself or goes out of bounds
        if (head[0] < 5 or head[0] > 34 or head[1] < 5 or head[1] > 34
                or not convertToKey(head) in self.openLocations):
            self.dead = True
            return True
    
    def fruitDistance(self, head):
        return math.sqrt((head[0] - self.fruit[0])**2 + (head[1] - self.fruit[1])**2)

    """ Checks to see if the snake has eaten a fruit or not """
    def checkFruit(self):
        # Returns True if the snake head is at a fruit location
        return self.snakeBody[0] == self.fruit

    """ Returns location of where the next fruit should be. """
    def newFruit(self):
        return random.choice(list(self.openLocations.values()))

    """ Sets up persistence of the stored moves."""
    def persistence(self):
        with open('Simulations/simulation1test.txt', 'wb') as sim_moves:
            pickle.dump(self.all, sim_moves)

""" Converts a given location to a key for openLocations dictionary.
NOT A CLASS METHOD!"""
def convertToKey(location):
    return location[0] - 5 + 30 * (location[1] - 5)
