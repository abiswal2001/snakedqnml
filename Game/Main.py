""" Main class which runs the machine learning snake
program or it allows the player to play snake. """

# Necessary imports
import Snake
import pygame
import Player
import Computer
import ComputerSnake

# Creates the snake game.
game = ComputerSnake.Snake()

# Run the player Game
Computer.ComputerPlayer(game)
