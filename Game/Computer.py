""" Player class which represents a player playing snake. """

# Necessary imports
import pygame
import random
import Snake

class ComputerPlayer():
    """ A class which allows the player to play the snake game
    that is passed in using arrow keys or wasd."""

    def __init__(self, game):
        self.game = game
        self.moves = []
        self.playerGame()

    """ Creates a game where a player can play snake. """
    def playerGame(self):
        running = True
        while self.game.dead is False:
            # Updates Display
            dir = random.randint(1, 4)
            self.moves.append(dir)
            self.game.setDir(dir)
            self.game.updateSnake()
        self.playGUI()

    """ Takes the list of moves in the snake game that was played
    and plays it to a GUI. """
    def playGUI(self):
        index = 0
        self.game = Snake.Snake()
        while index < len(self.moves):
            # Updates Display
            pygame.display.update()

            # Handles events
            for i in pygame.event.get():
                if i.type == pygame.USEREVENT + 1:
                    self.game.updateSnake()
                    self.game.setDir(self.moves[index])
                # Quitting out of the game
                elif i.type == pygame.QUIT:
                    running = False
                    pygame.quit()
            index += 1
