""" Snake game without the GUI"""

# Necessary Imports
import random
import abc
import tensorflow as tf
import numpy as np

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

    """ Creates the snake game with the given border limits and
    starts the game. """

    def __init__(self):
        self._action_spec = array_spec.BoundedArraySpec((), dtype=np.int32, minimum=1, maximum=4, name='action')
        self._observation_spec = array_spec.BoundedArraySpec((9,), dtype=np.int32, minimum=[5, 5, 1, 5, 5, 0, 0, 0, 0], maximum=[34, 34, 4, 34, 34, 1, 1, 1, 1], name='observation')
        self._state = [20, 20, 1, 25, 20, 0, 0, 0, 0]
        self.setup()
        
    def action_spec(self):
        return self._action_spec

    def observation_spec(self):
        return self._observation_spec

    def setup(self):
        # Initialize Game
        pygame.init()

        # Change Title of Game
        pygame.display.set_caption('Snake')

        # Setting up the window
        self.windowWidth = 800
        self.windowHeight = 800
        self.screen = pygame.display.set_mode([self.windowWidth,
                                               self.windowHeight])
        self.white = [255, 255, 255]
        self.black = (0, 0, 0)
        self.green = (46, 135, 58)
        self.fruitColor = [255, 0, 0]
        self.apple = pygame.image.load(os.getcwd() + '/apple.png')
        self.screen.fill(self.white)
        self.dead = False

        # Draw game border
        pygame.draw.rect(self.screen, self.black, (95, 95, 610, 610), 5)

        # Main font to be used in this application
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        # Displaying Score
        self.score = 1
        self.score_text, self.score_text_rect = "", ""

        # Start Timer
        pygame.time.set_timer(pygame.USEREVENT + 1, 300)

        # Default fruit position
        self.fruit = [25, 20]

        # Starts a new game
        self.newGame()


    def _reset(self):
        self._state = np.array([20, 20, 1, 25, 20, 0, 0, 0, 0], dtype=np.int32)
        self.dead = False
        self.newGame()
        return ts.restart(self._state)

    def _step(self, action):
        if self.dead:
            return self.reset()
        if action >= 1 and action <= 4:
            self.setDir(action)
        else:
            raise ValueError('action must be between 1 and 4')

        reward = 0.0
        discount = 0.0
        # Checks to see if the snake head reaches a fruit
        eaten = self.checkFruit()
        # Moves the snake based on the current direction
        head = self.snakeBody[0][:]
        if (self.dir == 1):
            head[0] += 1
        elif (self.dir == 2):
            head[0] -= 1
        elif (self.dir == 3):
            head[1] -= 1
        else:
            head[1] += 1
        self.snakeBody.insert(0, head)
        # Only continues if game has not ended
        if (not self.checkLose()):
            key = convertToKey(head)
            self.openLocations.pop(convertToKey(head))
             # Removes last body part if fruit was not eaten
            if (not eaten):
                removed = self.snakeBody.pop()
                self.openLocations[convertToKey(removed)] = removed
            # Creates a new fruit if the fruit was eaten and increments score
            else:
                self.fruit = self.newFruit()
                self.updateScore()
                reward += 5.0
            danger_arr = self.danger()
            self._state = np.array([self.head[0], self.head[1], action, self.fruit[0], self.fruit[1], danger[0], danger[1], danger[2], danger[3]], dtype=int32)
            return ts.transition(self._state, reward, discount=1.0)
        else:
            self.dead = True
            reward -= 10.0
            return ts.termination(self._state, reward, discount=1.0) 

    """ Danger value based on self-collision and wall collision. 0 for danger, 1 for no danger   """
    def danger(self):
        neighborUp = int(convertToKey([head[0], head[1] + 1]) in self.openLocations)
        neighborDown = int(convertToKey([head[0], head[1] - 1]) in self.openLocations)
        neighborLeft = int(convertToKey([head[0] - 1, head[1]]) in self.openLocations)
        neighborRight = int(convertToKey([head[0] + 1, head[1]]) in self.openLocations)
        return np.array([neighborUp, neighborDown, neighborLeft, neighborRight], dtype=int32)

     """ Creates a new game with the snake and fruit in the default positions. """
    def newGame(self):
        # Displays initial score of 0
        self.updateScore()

        # Snake Body
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
        self.dead = False
        
        
    """ Increments the score """
    def updateScore(self):
        self.score += 1

    """ Changes the direction that the snake moves in.
    This essentially represents players playing the game. """
    def setDir(self, dir):
        self.dir = dir

    """ Updates snake every time a certain amount of time passes """
    def updateSnake(self):
        

    """ Checks to see if the game is over """
    def checkLose(self):
        head = self.snakeBody[0]

        # Checks to see if the snake collides without itself or goes out of bounds
        if (head[0] < 5 or head[0] > 34 or head[1] < 5 or head[1] > 34
                or not convertToKey(head) in self.openLocations):
            print(self.score - 1)
            self._reset()
            self.dead = True
            return True

    """ Checks to see if the snake has eaten a fruit or not """
    def checkFruit(self):
        # pygame.draw.rect(screen, fruitColor, (fruit[0] * 20, fruit[1] * 20, 18, 18), 0)
        if (self.snakeBody[0] == self.fruit):
            return True
        return False

    """ Returns location of where the next fruit should be. """
    def newFruit(self):
        return random.choice(list(self.openLocations.values()))

   

""" Converts a given location to a key for openLocations dictionary """
def convertToKey(location):
    return location[0] - 5 + 30 * (location[1] - 5)
