# Simple Snake Game

# Necessary Imports
import pygame
import time

pygame.init()

# Setting up the window
screen = pygame.display.set_mode([500, 500])
for i in range(10):
    print("Hello World" + str(time.perf_counter()))
    time.sleep(1)
