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
score_text, score_text_rect = 0, 0

# Updates score every time the snake eats a something
def updateScore():
    global score_text, text_rect, score
    score_text = font.render('Total Score: ' + str(score), True, black, white)
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (windowWidth // 2, 20)
    screen.blit(score_text, score_text_rect)
    score += 1

# Displays initial score of 0
updateScore()

# Snake Body
snakeBody = [[20, 20]];

# Start Timer
pygame.time.set_timer(pygame.USEREVENT + 1, 500)

# Default direction which the snake will be moving in
dir = 1

#
def keyPresses():
    global dir
    # Stores whether or not that key has been pressed
    keys=pygame.key.get_pressed()

    # Left key press
    if keys[pygame.K_RIGHT]:
        dir = 1
    elif keys[pygame.K_LEFT]:
        dir = 2
    elif keys[pygame.K_UP]:
        dir = 3
    elif keys[pygame.K_DOWN]:
        dir = 4

# Updates snake every time a certain amount of time passes
def updateSnake():
    # Erase previous snake body
    for body in snakeBody:
        pygame.draw.rect(screen, white, (body[0] * 20, body[1] * 20, 18, 18), 0)

    # Moves the snake based on the current direction
    if (dir == 1):
        for body in snakeBody:
            body[0] += 1
    elif (dir == 2):
        for body in snakeBody:
            body[0] -= 1
    elif (dir == 3):
        for body in snakeBody:
            body[1] -= 1
    else:
        for body in snakeBody:
            body[1] += 1

    # Draws the snake after it moved
    for body in snakeBody:
        pygame.draw.rect(screen, black, (body[0] * 20, body[1] * 20, 18, 18), 0)

    #checkFruit()
    checkLose()

# Checks to see if the game is over
def checkLose():
    if (score == -1):
        running = False
        pygame.quit()

# Checks to see if the snake has eaten a fruit or not
#def checkFruit():


# Keeps screen open until you close it
running = True
while running:
    # Updates Pygame Display
    pygame.display.update()

    # Handles events
    for i in pygame.event.get():
        keyPresses()
        if i.type == pygame.USEREVENT + 1:
            updateSnake()
        if i.type == pygame.QUIT:
            running = False
            pygame.quit()
