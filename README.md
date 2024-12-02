## Intro

In this project we will study a reinforcement learning AI that plays tic-tac-toe as the first player. We will be inplementing the MENACE (Matchbox Educable Noughts and Crosses Engine) algorithm (see https://en.wikipedia.org/wiki/Matchbox_Educable_Noughts_and_Crosses_Engine).


We will take advantage of the isomorphism between the tic-tac-toe board-states
and the 3x3 magic square

| 2 | 7 | 6 |

| 9 | 5 | 1 |

| 4 | 3 | 8 |

Chosing an square in tic-tac-toe is equivalent to chosing a number from 1 to 9. A player win when they have chosen 3 numbers that add up to 15.

## Files

### players.py 
This file contains two main classes, RandomTicTacToe and ManualTicTacToe. One similates a random player, and the other allows you to input moves yourself.

### reinforcement.py
This file contains the class Matchboxes that implements the MENACE algorithm. The heirarchy of matchboxes and their contents are modeled using a dictionary of dictionaries.

