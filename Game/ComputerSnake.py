""" Snake game without the GUI"""

# Necessary Imports
import random

class Snake():
    """A class which plays the primary portion of the snake game while
    receiving moves to play from other player classes. """

    """ Creates the snake game with the given border limits and
    starts the game. """
    def __init__(self):
        # Aliveness
        self.dead = False

        # Displaying Score
        self.score = 1

        # Default fruit position
        self.fruit = [25, 20]

        # Starts a new game
        self.newGame()

    """ Increments the score """
    def updateScore(self):
        self.score += 1

    """ Changes the direction that the snake moves in.
    This essentially represents players playing the game. """
    def setDir(self, dir):
        self.dir = dir

    """ Updates snake every time a certain amount of time passes """
    def updateSnake(self):
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
        else:
            return
        # Removes last body part if fruit was not eaten
        if (not eaten):
            removed = self.snakeBody.pop()
            self.openLocations[convertToKey(removed)] = removed

        # Creates a new fruit if the fruit was eaten and increments score
        else:
            self.fruit = self.newFruit()
            self.updateScore()

    """ Checks to see if the game is over """
    def checkLose(self):
        head = self.snakeBody[0]

        # Checks to see if the snake collides without itself or goes out of bounds
        if (head[0] < 5 or head[0] > 34 or head[1] < 5 or head[1] > 34
                or not convertToKey(head) in self.openLocations):
            print(self.score - 1)
            self.newGame()
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

""" Converts a given location to a key for openLocations dictionary """
def convertToKey(location):
    return location[0] - 5 + 30 * (location[1] - 5)
