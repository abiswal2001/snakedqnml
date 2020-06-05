""" Player class which represents a player playing snake. """

# Necessary imports
import pygame
import random


class ComputerPlayer():
    """ A class which allows the player to play the snake game
    that is passed in using arrow keys or wasd."""

    def __init__(self, game):
        self.game = game
        self.playerGame()

    """ Creates a game where a player can play snake. """

    def playerGame(self):
        running = True
        while self.game.dead is False:
            # Updates Display
            pygame.display.update()
            self.game.setDir(random.randint(1, 4))
            self.game.updateSnake()
