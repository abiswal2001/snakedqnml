# Main class which runs the machine learning snake program.

# Necessary imports
import Snake
import pygame

game = Snake.Snake()

running = True
while running:
    # Updates Display
    pygame.display.update()

    # Handles events
    for i in pygame.event.get():
        game.keyPresses()
        # Event which occurs every second
        if i.type == pygame.USEREVENT + 1:
            if (game.updateSnake()):
                running = False
                break
        # Quitting out of the game
        elif i.type == pygame.QUIT:
            running = False
            pygame.quit()
