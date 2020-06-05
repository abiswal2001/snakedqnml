# Simple Snake Game

# Necessary Imports
import pygame
import time
import os
import random

# Initialize Game
pygame.init()

# Change Title of Game
pygame.display.set_caption('Snake')

# Setting up the window
windowWidth = 800
windowHeight = 800
screen = pygame.display.set_mode([windowWidth, windowHeight])
white = [255, 255, 255]
black = (0, 0, 0)
green = (46, 135, 58)
fruitColor = [255, 0, 0]
apple = pygame.image.load(os.getcwd() + '/apple.png')
screen.fill(white)

# Draw game border
pygame.draw.rect(screen, black, (100, 100, 600, 600), 5)

# Displaying Score
score = 0
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
snakeBody = [[20, 20]]

# Initial Fruit Location
fruit = [25, 20]

# A dictionary which contains all possible locations that a fruit can be at.
openLocations = {}
for i in range(30):
    for j in range(30):
        openLocations[i + 30 * j] = [i + 5, j + 5]

# Start Timer
pygame.time.set_timer(pygame.USEREVENT + 1, 300)

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
    global fruit

    # Checks to see if the snake head reaches a fruit
    eaten = checkFruit()

    # Erase previous snake body
    for body in snakeBody:
        pygame.draw.rect(screen, white, (body[0] * 20, body[1] * 20, 18, 18), 0)

    # Moves the snake based on the current direction
    head = snakeBody[0][:]
    if (dir == 1):
        head[0] += 1
    elif (dir == 2):
        head[0] -= 1
    elif (dir == 3):
        head[1] -= 1
    else:
        head[1] += 1
    snakeBody.insert(0, head)

    # Only continues if game has not ended
    if (not checkLose()):
        key = convertToKey(head)
        openLocations.pop(convertToKey(head))
    else:
        return

    # Removes last body part if fruit was not eaten
    if (not eaten):
        removed = snakeBody.pop()
        openLocations[convertToKey(removed)] = removed

    # Creates a new fruit if the fruit was eaten and increments score
    else:
        fruit = newFruit()
        updateScore()

    # Draws the fruit location
    displayFruit()

    # Draws the snake after it moved
    for body in snakeBody:
        pygame.draw.rect(screen, green, (body[0] * 20, body[1] * 20, 18, 18), 0)

# Checks to see if the game is over
def checkLose():
    head = snakeBody[0]
    lose = False
    if (head[0] < 5 or head[0] > 34 or head[1] < 5 or head[1] > 34 or not convertToKey(head) in openLocations):
        running = False
        print(score)
        pygame.quit()
        return True

# Checks to see if the snake has eaten a fruit or not
def checkFruit():
    # pygame.draw.rect(screen, fruitColor, (fruit[0] * 20, fruit[1] * 20, 18, 18), 0)
    if (snakeBody[0] == fruit):
        return True
    return False

def displayFruit():
    screen.blit(pygame.transform.scale(apple, (18, 18)), (fruit[0] * 20, fruit[1] * 20))

# Converts a given location to a key for openLocations dictionary
def convertToKey(location):
    return location[0] - 5 + 30 * (location[1] - 5)

# Returns location of where the next fruit should be.
def newFruit():
    return random.choice(list(openLocations.values()))

# Keeps screen open until you close it
running = True
while running:
    # Updates Display
    pygame.display.update()

    # Handles events
    for i in pygame.event.get():
        keyPresses()
        if i.type == pygame.USEREVENT + 1:
            updateSnake()
        elif i.type == pygame.QUIT:
            running = False
            pygame.quit()
