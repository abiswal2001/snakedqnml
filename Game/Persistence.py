import pickle
import Snake
import pygame

""" NEEDS FIXING """


""" Takes the list of moves in the snake game that was played
    and plays it to a GUI. """
def playGUI():
    # Indexes which traverse through objects
    listIndex, index = 0, 0
    game = Snake.Snake()
    game.startGame()
    all_moves = objects[0]
    all_fruit = objects[1]
    print(len(all_moves))
    for i in range(len(all_moves)):
        moves = all_moves[i]
        game.fruit_locations = all_fruit[i]
        while index < len(moves):
            # Updates Display
            pygame.display.update()
            # Handles events
            for i in pygame.event.get():
                if i.type == pygame.USEREVENT + 1:
                    # Changes direction of snake and makes
                    # a move for the snake in that direction.
                    if (index < len(moves)):
                        game.setDir(moves[index])
                        game.updateSnake()
                        index += 1
                    else:
                        break
                # Quitting out of the game
                elif i.type == pygame.QUIT:
                    running = False
                    pygame.quit()
        index = 0

objects = []

with (open("Simulations/simulation1test.txt", "rb")) as openfile:
    while True:
        try:
            objects = pickle.load(openfile)
        except EOFError:
            break
playGUI()
