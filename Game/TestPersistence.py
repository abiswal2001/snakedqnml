import Computer
import pickle

objects = []
with (open("Simulations/simulation1test.txt", "rb")) as openfile:
    while True:
        try:
            objects = pickle.load(openfile)
        except EOFError:
            break
print(objects)