# Simple Snake Game

# Necessary Imports
import pygame
import time

# Initialize Game
pygame.init()

# Change Title of Game
pygame.display.set_caption('Snake')


# Setting up the window
windowWidth = 800
windowHeight = 800
screen = pygame.display.set_mode([windowWidth, windowHeight])
white = [255, 255, 255]
screen.fill(white)

# Displaying Score
score = 0
black = (0, 0, 0)
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Total Score: ' + str(score), True, black, white)
textRect = text.get_rect()
textRect.center = (windowWidth // 2, 20)
screen.blit(text, textRect)

# Updates Pygame Display
pygame.display.update()

# Keeps screen open until you close it
running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
            pygame.quit()
