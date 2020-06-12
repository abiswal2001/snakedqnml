""" Simple Snake Game which is run for persistence."""

# Necessary Imports
import pygame
import os
import random


class Snake():
    """A class which plays the primary portion of the snake game while
    receiving moves to play from other player classes. """

    """ Creates the snake game with the given border limits and
    starts the game. """
    def __init__(self):
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
        self.red = (255, 0, 0)
        self.fruitColor = [255, 0, 0]
        self.apple = pygame.image.load(os.getcwd() + '/apple.png')
        self.screen.fill(self.white)
        self.dead = False

        # Draw game border
        pygame.draw.rect(self.screen, self.black, (145, 145, 610, 610), 5)

        # Main font to be used in this application
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        # Displaying Score
        self.score = 0
        self.score_text, self.score_text_rect = "", ""

        # Default fruit position + Default fruit array
        self.fruit = [20, 15]
        self.fruit_index = 0

        # Snake Body
        self.snakeBody = [[14, 15]]

        # Starts a new game
        self.newGame()

    """ Updates score text at the top of the screen and adds one to the score """
    def updateScore(self):
        # Clears the screen
        pygame.draw.rect(self.screen, self.white, (0, 0, 700, 100), 5)

        # Updates the text box to have the new text
        self.score_text = self.font.render('Total Score: ' +
            str(self.score), True, self.black, self.white)
        self.score_text_rect = self.score_text.get_rect()
        self.score_text_rect.center = (self.windowWidth // 2, 20)

        # Prints the text to the screen
        self.screen.blit(self.score_text, self.score_text_rect)
        self.score += 1

    """ Changes the direction that the snake moves in.
    This essentially represents players playing the game. """
    def setDir(self, dir):
        self.dir = dir

    """ Updates snake every time a certain amount of time passes """
    def updateSnake(self):
        # Checks to see if the snake head reaches a fruit
        eaten = self.checkFruit()

        # Erase previous snake body
        for body in self.snakeBody:
            pygame.draw.rect(self.screen, self.white,
                (body[0] * 30, body[1] * 30, 27, 27), 0)

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
            # Exits from the method if the game is over and starts a new game.
            return

        # Removes last body part if fruit was not eaten
        if (not eaten):
            removed = self.snakeBody.pop()
            self.openLocations[convertToKey(removed)] = removed

        # Creates a new fruit if the fruit was eaten and increments score
        else:
            self.fruit = self.newFruit()
            self.updateScore()

        # Draws the fruit location
        self.displayFruit()

        # Draws the snake after it moved
        for body in self.snakeBody:
            pygame.draw.rect(self.screen, self.green,
                (body[0] * 30, body[1] * 30, 27, 27), 0)

    """ Checks to see if the game is over """
    def checkLose(self):
        head = self.snakeBody[0]

        # Checks to see if the snake collides without itself or goes out of bounds
        if (not convertToKey(head) in self.openLocations or self.curr_moves > self.move_limit):
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

    """ Code which prints out the apple which represents the fruit on the screen """
    def displayFruit(self):
        self.screen.blit(pygame.transform.scale(self.apple,
            (27, 27)), (self.fruit[0] * 30, self.fruit[1] * 30))

    """ Erases the fruit from the GUI. """
    def eraseFruit(self):
        pygame.draw.rect(self.screen, self.white,
            (self.fruit[0] * 30, self.fruit[1] * 30, 30, 30), 0)

    """ Returns location of where the next fruit should be. """
    def newFruit(self):
        return random.choice(list(self.openLocations.values()))

    """ Creates a new game with the snake and fruit in the default positions. """
    def newGame(self):
        # Erases whatever fruit was on the board previously.
        self.eraseFruit()

        # Displays initial score of 0
        self.score = 0
        self.updateScore()

        # Snake Body
        self.snakeBody = [[14, 15]]

        # Initial Fruit Location
        self.fruit = [20, 15]

        # A dictionary which contains all possible locations that a fruit can be at.
        self.openLocations = {}
        for i in range(20):
            for j in range(20):
                self.openLocations[i + 400 * j] = [i + 5, j + 5]

        # Default direction which the snake will be moving in
        self.dir = 1

        # Move limits for the computer version of the simulation
        self.move_limit = 1000
        self.curr_moves = 0

        # Prints the snake to the board
        self.updateSnake()

        # Reset the fruit index
        self.fruit_index = 0

    """ Starts the actual snake game."""
    def startGame(self):
        # Start Timer
        pygame.time.set_timer(pygame.USEREVENT + 1, 200)

""" Converts a given location to a key for openLocations dictionary """
def convertToKey(location):
    return location[0] - 5 + 400 * (location[1] - 5)
