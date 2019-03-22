# DIRECTORY AND CODE STRUCTURE

## Directory structure

* `resources` contains fonts and images.
* all the Python code is located in the main directory
* `README.md` is located in the main directory

## Code structure

The game loop is located in `ping.py`. 

The ball class is located in `ball.py`.
This controls the movement and drawing of the game's ball.

The board class is located in `board.py`.
It has instances of the paddles, ball, and scoreboard and is used to interact with them.

The menu class is located in `menu.py`. 
This is the main menu at the start of the program.
It allows the user to choose from start, settings, or quit

The paddle class is located in `paddle.py`. 
This controls the movement and display of the players' paddles.

The scoreboard class is located in `scoreboard.py`.
This stores and displays each player's scores.

