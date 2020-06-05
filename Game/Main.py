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
snakeBody = [(20, 20)];

# Start Timer
pygame.time.set_timer(pygame.USEREVENT + 1, 1000)

# Handles key presses
def keyPresses():
    # Stores whether or not that key has been pressed
    keys=pygame.key.get_pressed()

    # Left key press
    if keys[pygame.K_LEFT]:
        print("1")
    elif keys[pygame.K_RIGHT]:
        print("2")
    elif keys[pygame.K_UP]:
        print("3")
    elif keys[pygame.K_DOWN]:
        print("4")

# Updates snake every time a certain amount of time passes
def updateSnake():
    print("hi")

# Keeps screen open until you close it
running = True
while running:
    # Updates Pygame Display
    pygame.display.update()

    # Handles events
    for i in pygame.event.get():
        keyPresses()
        if i.type == pygame.USEREVENT + 1:
            updateScore();
        if i.type == pygame.QUIT:
            running = False
            pygame.quit()
