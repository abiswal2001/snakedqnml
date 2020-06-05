""" Main class which runs the machine learning snake
program or it allows the player to play snake. """

# Necessary imports
import Snake
import pygame
import Player

# Creates the snake game.
game = Snake.Snake()

# Run the player Game
Player.Player(game)
