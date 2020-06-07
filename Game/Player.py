""" Player class which represents a player playing snake. """

# Necessary imports
import pygame

class Player():
    """ A class which allows the player to play the snake game
    that is passed in using arrow keys or wasd."""
    def __init__(self, game):
        self.game = game
        self.playerGame()

    """ Creates a game where a player can play snake. """
    def playerGame(self):
        self.game.startGame()
        running = True
        while running:
            # Updates Display
            pygame.display.update()

            # Handles events
            for i in pygame.event.get():
                self.keyPresses()
                # Event which occurs every second
                if i.type == pygame.USEREVENT + 1:
                    self.game.updateSnake()

                # Quitting out of the game
                elif i.type == pygame.QUIT:
                    running = False
                    pygame.quit()

    """ Handles pressed keys by the player. """
    def keyPresses(self):
        # Stores whether or not that key has been pressed
        keys=pygame.key.get_pressed()

        # Handling of directions
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
            self.game.setDir(1)
        elif (keys[pygame.K_LEFT] or keys[pygame.K_a]):
            self.game.setDir(2)
        elif (keys[pygame.K_UP] or keys[pygame.K_w]):
            self.game.setDir(3)
        elif (keys[pygame.K_DOWN] or keys[pygame.K_s]):
            self.game.setDir(4)
