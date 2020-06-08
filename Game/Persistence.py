import pickle
import Snake
import pygame

""" NEEDS FIXING """


""" Takes the list of moves in the snake game that was played
    and plays it to a GUI. """
def playGUI():
    index = 0
    game = Snake.Snake()
    game.startGame()
    while index < len(objects):
        # Updates Display
        pygame.display.update()
        # Handles events
        for i in pygame.event.get():
            if i.type == pygame.USEREVENT + 1:
                game.setDir(objects[index])
                game.updateSnake()
                index += 1
            # Quitting out of the game
            elif i.type == pygame.QUIT:
                running = False
                pygame.quit()

objects = []
with (open("Simulations/simulation1test.txt", "rb")) as openfile:
    while True:
        try:
            objects = pickle.load(openfile)
        except EOFError:
            break
playGUI()
