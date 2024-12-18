# In this project we will study a reinforcement learning AI that plays tic-tac-toe.
# The will take advantage of the isomorphism between the tic-tac-toe board-states
# and the 3x3 magic square
# | 2 | 7 | 6 |
# | 9 | 5 | 1 |
# | 4 | 3 | 8 |
#
# Chosing an square in tic-tac-toe is equivalent to chosing a number from 1 to 9.
# A player win when they have chosen 3 numbers that add up to 15.

from itertools import combinations
import random

def linearize(l1: list, l2:list) -> list:
    """
    Takes two lists and creates a single list alternating 
    the entries between each one. Note that for zip() to work
    both lists must have the same size.
    """

    tuple_list = zip(l1, l2)
    linear_list = []
    for (a, b) in tuple_list:
        linear_list.append(a)
        linear_list.append(b)
    return linear_list


def check_win(movelist: list) -> bool:
    """Checks if a list contains 3 numbers that add up to 15."""
    found = False
    if len(movelist) < 3:
        return found
    else:
        for triple in combinations(movelist, 3):                        
            if sum(triple) == 15:
                found = True
    return found

class RandomTicTacToe:
    """
    Random game of tic-tac-toe.
    
    Methods:
    turn(): performs a random turn.
    play(): performs a sequence of random turns until the game is finished.
    result(): returns the tuple (winner, moves by player 1, moves by player 2) 
    """
    def __init__(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # the following two lists record each players move: 
        self.player1 = []
        self.player2 = []
        self.winner = None
        self.draw = False

    def turn(self):
        random_square = random.choice(self.board)
        self.board.remove(random_square)

        if len(self.player1) == len(self.player2):
            self.player1.append(random_square)
            if check_win(self.player1):
                self.winner = 1

        else:
            self.player2.append(random_square)
            if check_win(self.player2):
                self.winner = 2
        
        return None
    
    def play(self):
        while self.winner == None:
            if len(self.board) > 0:
                self.turn()
            else:
                self.draw= True
                break
        return None
    
    def result(self):
        if self.draw:
            return 0, self.player1, self.player2
        else:
            return self.winner, self.player1, self.player2
        
    def linearboardstate(self):
        # If there was an equal number of turns, then linearize works directly.
        boardstate_even = linearize(l1=self.player1, l2=self.player2)
        if len(self.player1) == len(self.player2):
            return boardstate_even
        else:
            # If player 1 had one more turn, we must add it to the end.
            boardstate_odd = boardstate_even + [self.player1[-1]]
            return boardstate_odd



class ManualTicTacToe:
    """
    Game of tic-tac-toe where moves are inputed manually.

    Methods:

    turn(square): selects the specified square for the current player and
    updates the game state.
    gamestate(): returns one of three possible game states 'in progress'/'draw'/'player X wins'.
    """
    def __init__(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        # the following two lists record each players move: 
        self.player1 = []
        self.player2 = []
        
        self.winner = None
        self.draw = False

        # if currentplayer = 0 then the game is over.
        self.currentplayer = 1
    
    def turn(self, square:int):
        if square in self.board:
            self.board.remove(square)
            if self.currentplayer == 1:
                self.player1.append(square)
                if check_win(self.player1):
                    self.winner = 1
                    self.currentplayer = False
                else:
                    self.currentplayer = 2
            else:
                self.player2.append(square)
                if check_win(self.player2):
                    self.winner = 2
                    self.currentplayer = False
                else:
                    self.currentplayer = 1
        
        # this line checks if the game ended in a draw by seeing if the 
        # board is empty.
        self.draw = not self.board
        if self.draw:
            self.currentplayer = False
        return None
    
    def gamestate(self):
        if self.currentplayer:
            return 'in progress'
        elif self.draw:
            return 'draw'
        else:
            result = 'player {} wins'.format(self.winner)
            return result
        
    def linearboardstate(self):
        # If there was an equal number of turns, then linearize works directly.
        boardstate_even = linearize(l1=self.player1, l2=self.player2)
        if len(self.player1) == len(self.player2):
            return boardstate_even
        else:
            # If player 1 had one more turn, we must add it to the end.
            boardstate_odd = boardstate_even + [self.player1[-1]]
            return boardstate_odd 



if __name__ == "__main__":
    # Quickly testing both classes:
    #
    # RTTT = RandomTicTacToe()
    # RTTT.play()
    # for x in RTTT.result():
    #     print(x)

    MTTT = ManualTicTacToe()
    moves = [5, 2, 6, 4, 9, 1, 7, 3, 8]
    for x in moves:
        MTTT.turn(x)
        print(MTTT.gamestate())
        print(MTTT.board)
        print('moves by player 1', MTTT.player1)
        print('moves by player 2', MTTT.player2)
        print('-----')
    
    print(MTTT.linearboardstate())
    pass
    
        


            





