""" Main class which runs the machine learning snake
program or it allows the player to play snake. """

# Necessary imports
import Computer
import ComputerSnake
import pygame
import Snake
import Player

intro = True

# Creates the snake game.
game = Snake.Snake()

# Creates rectangle for the player game button
player_text = game.font.render("Player", True, game.black, game.green)
player_text_rect = player_text.get_rect()
player_text_rect.center = (game.windowWidth // 4, 60)
game.screen.blit(player_text, player_text_rect)

# Creates rectangle for the computer game button
computer_text = game.font.render("Computer", True, game.black, game.red)
computer_text_rect = computer_text.get_rect()
computer_text_rect.center = (game.windowWidth // 4 * 3, 60)
game.screen.blit(computer_text, computer_text_rect)
pygame.display.update()

""" Clears the display buttons"""
def clearButtons():
    # Updates player button to be white
    player_text = game.font.render("Computer", True, game.white, game.white)
    game.screen.blit(player_text, player_text_rect)

    # Updates computer button to be white
    computer_text = game.font.render("Computer", True, game.white, game.white)
    game.screen.blit(computer_text, computer_text_rect)

""" Starts a game which the player can play. """
def playerGame():
    # Run the player Game
    Player.Player(game)

def computerGame():
    # Runs the computer game
    print('running')
    pygame.quit()
    game = ComputerSnake.Snake()
    Computer.ComputerPlayer(game)


while intro:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.MOUSEBUTTONUP:
            click = pygame.mouse.get_pos()
            if (click[0] > 150 and click[1] > 45 and click[0] < 250 and click[1] < 80):
                clearButtons()
                playerGame()
                intro = False
            elif(click[0] > 520 and click[1] > 45 and click[0] < 680 and click[1] < 80):
                clearButtons()
                computerGame()
                intro = False
        elif event.type == pygame.QUIT:
            intro = False
            pygame.quit()
