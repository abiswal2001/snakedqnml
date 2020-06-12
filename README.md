# snakedqnml
While this application can be used in multiple ways, the primary
purpose of this application is to run allow the computer to learn 
how to play snake on its own. The user can also choose to play 
snake on their own however that is a side feature that was 
implemented for initial testing purposes. 

## Running the program
There are 2 ways in which someone can run the application
where the computer learns to play snake. First, regardless of 
which way they want to run the program, the user should 
install tensorflow, tf-agents, and pygame to their computer and 
create a virtual environment which can be used to run tensorflow.
Then the user can either run the Main.py file or they can run
load the Computer.py file. If they run the Main.py file, they 
should then click the "Computer" button which will show up in the
top right of their screen. If the Computer.py file was run, the
user should then run the "simulate" method which will start the 
simulation. 

## The Simulation
As the simulation runs, it will tell the user how many steps of 
data have been collected by the agent and how well the agent is 
doing in evaluation games which are run every time the agent
collects 5000 steps of data. The simulation runs for a total of 
30000 steps, and the agent evaluates a total of 35 games. On 
average the simulation takes around 5 to 10 minutes to run in total
and after around 10000 steps the snake will average around 30 total
fruit when evaluating afterwards. The highest score the snake ever
achieved in our runs was 70 fruit and this run is saved in the 
simulation file which is in our latest commit. After the simulation 
finishes running, a matlab plot will be displayed of the evaluation
results of our simulation.

## Persistence
All of the runs by the agent will be saved to the file in the 
simulations folder. For the user to actually see what the computer
did during these runs, they can run the Persistence.py file which
will display a GUI which will show the computer playing the game
in a very sped up version. 
