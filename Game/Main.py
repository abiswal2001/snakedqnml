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
text_rect = text.get_rect()
text_rect.center = (windowWidth // 2, 20)
screen.blit(text, text_rect)

# Snake Body
snakeBody = [(20, 20)];

# Key Press codes
keys=pygame.key.get_pressed()

# Handles key presses
def keyPresses():
    # Stores whether or not that key has been pressed
    keys=pygame.key.get_pressed()

    # Left key press
    if keys[pygame.K_LEFT]:
        key_text = font.render("Left Key", True, black, white)
        key_text_rect = text.get_rect()
        key_text_rect.center = (windowWidth // 2, windowHeight // 2)
        screen.blit(key_text, key_text_rect)
    elif keys[pygame.K_RIGHT]:
        key_text = font.render("Right Key", True, black, white)
        key_text_rect = text.get_rect()
        key_text_rect.center = (windowWidth // 2, windowHeight // 2)
        screen.blit(key_text, key_text_rect)
    elif keys[pygame.K_UP]:
        key_text = font.render("Up Key", True, black, white)
        key_text_rect = text.get_rect()
        key_text_rect.center = (windowWidth // 2, windowHeight // 2)
        screen.blit(key_text, key_text_rect)
    elif keys[pygame.K_DOWN]:
        key_text = font.render("Down Key", True, black, white)
        key_text_rect = text.get_rect()
        key_text_rect.center = (windowWidth // 2, windowHeight // 2)
        screen.blit(key_text, key_text_rect)

def updateSnake():
    print("hello")

# Keeps screen open until you close it
running = True
while running:
    # Updates Pygame Display
    pygame.display.update()

    # Handles events
    for i in pygame.event.get():
        keyPresses()
        if i.type == pygame.QUIT:
            running = False
            pygame.quit()
