""" Player class which represents a player playing snake. """

# Necessary imports
import random
import pickle
import ComputerSnake

class ComputerPlayer():
    """ A class which allows the player to play the snake game
    that is passed in using arrow keys or wasd."""

    def __init__(self, game):
        self.game = game

    """ Creates a game where a player can play snake. """
    def playerGame(self):
        envTrain = ComputerSnake.Snake()
        envEval = ComputerSnake.Snake()
        utils.validate_py_environment(env, episodes=5)
        train_env = tf_py_environment.TFPyEnvironment(envTrain)
        eval_env = tf_py_environment.TFPyEnvironment(envEval)
        for _ in range(self.iterations):
            # Updates Display
            dir = random.randint(1, 4)
            self.moves.append(dir)
            self.game.setDir(dir)
            self.game.updateSnake()
        self.persistence()

    """ Sets up persistence of the stored moves."""
    def persistence(self):
        with open('Simulations/simulation1test.txt', 'wb') as sim_moves:
            pickle.dump(self.moves, sim_moves)
