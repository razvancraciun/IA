# Missionaries And Cannibals

  This is a simulation of playing the Missionaries and Cannibals game.
  
  [Wikipedia](https://en.wikipedia.org/wiki/Missionaries_and_cannibals_problem)
  
## Prerequisites
- Python3

## Usage
Run main.py with the following arguments:
 - ``` -m ``` or ``` --missionaries ```  __REQUIRED__ : Number of missionaries in the game.
 - ``` -c ``` or ``` --cannibals ``` __REQUIRED__ : Number of cannibals in the game.
 - ``` -b ``` or ``` --boat_size ``` __REQUIRED__ : Number of people that can fit in the boat.
 - ``` -s ``` or ``` --strategy ``` __REQUIRED__ : Strategy to be used. This can take one of three values: ```random```, ```bkt``` or ```iddfs```
 - ``` --depth ``` __Optional (default = 3)__ : Depth of a step. __Only has effect with IDDFS strategy.__ 
 - ``` -d ``` or ``` --display ``` __Optional (default = console)__: Way in which the results will be dispalyed: ```console``` or ```gui```. __NOTE: GUI display is not implemented yet___
 
 ### Example
  - ```python3 main.py -c 3 -m 3 -b 2 -s bkt```
  
  ## Encoding
  The output for the console display of the program will be a list of states of the following form:
  
     (n_m_left, n_c_left, boat_side, n_m_right, n_c_right)
  
  Where:

  -  ``` n_m_left ``` : Number of missionaries on the left side
  -  ``` n_c_left ``` : Number of cannibals on the left side
  -  ``` boat_side ``` : 1 if boat is on the left side, 2 if boat is on the right side
  -  ``` n_m_right ``` : Number of missionaries on the right side
  -  ``` n_c_right ``` : Number of cannibals on the right side
  
  This list contains the series of states that the game needs to go through from the initial state to get to the final state.
