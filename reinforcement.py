# Coding a reinforcement algorithm inspire by MENACE (Matchbox Educable Noughts and Crosses Engine).
# This script is for the first player, since the code here relies on there being an even number of moves made. 

from itertools import combinations, permutations
# import time


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


def deinterlace(movelist:list) -> tuple:
    """
    Inverse to linearize(): takes a single list a separates it into 
    two lists. Each list has the moves of a single player.
    """
    l1 = movelist[::2]
    l2 = movelist[1::2]
    return l1, l2

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


def check_win_linear(movelist:list)-> bool:
    """Receives the linearized list of both player's moves and checks if any has won."""
    l1, l2 = deinterlace(movelist=movelist)
    return check_win(l1) or check_win(l2)


def boardstate_lastmove(movelist:list)-> tuple:
    """
    Takes a move list an returns the last move by the first player and the board state preceeding it.
    Output: boardstate, lastmove.
    """
    # Check if player 1 made last move:
    if len(movelist) % 2 == 1:
        return movelist[:-1], movelist[-1]
    
    # If player 2 made last move, remove it from list and reset.
    else:
        return boardstate_lastmove(movelist=movelist[:-1])

def boardstates_moves(movelist: list) -> dict:
    """
    Returns a dictionary with each board state before player 1 made a move as the keys, and their
    subsequent move as the respective value.
    """
    D = {}
    moves = movelist
    while moves:
        boardstate, lastmove = boardstate_lastmove(movelist=moves)
        D[tuple(boardstate)] = lastmove
        moves = boardstate
    return D


class Matchboxes:
    """
    Simulates MENACE: Matchbox Educable Noughts and Crosses Engine.
     
    Atributes:
    
    gamestateboxes (dict): simulates the matchboxes in MENACE. It is essentially a dictionary of 
    dictionaries. At the first level the keys are number of moves the first player has already 
    made, i.e. 0, 1, 2, 3 or 4. Given i in {0, 1, 2, 3, 4}, gamestateboxes[i] is a dictionary whose 
    keys are all possible board states before player 1 makes their (i+1)th move, and the values 
    simulate the colored beads in MENACE, i.e. a list of moves that have been reinforced based on 
    whether they lead to wins, draws or loses.

    (win/loss/draw)reinforcefactor: factor by which the moves are reinforced by the reinforce method.

    Methods:

    reinforce: this method receives two inputs. The first is a list of moves from a concluded game; 
    the second represents the result (1 = win, 2 = loss, 0 = draw). It then updates gamestateboxes
    according to the MENACE algorithm.
    """

    def __init__(self):
        self.gamestateboxes = dict.fromkeys(range(5))

        self.winreinforcefactor = +3
        self.lossreinforcefactor = -1
        self.drawreinforcefactor = 1

        for i in range(5):
            n = 2*i
            self.gamestateboxes[i] = {tuple(movelist): [] 
                                  for movelist in permutations(range(1, 10), n) 
                                  if not check_win_linear(movelist)}

    def reinforce_win(self, movelist:list):
        D = boardstates_moves(movelist=movelist)
        for brdst in D.keys():
            i = len(brdst)/2
            self.gamestateboxes[i][brdst] = self.gamestateboxes[i][brdst] + self.winreinforcefactor*[D[brdst]]
        return None

    def reinforce_draw(self, movelist:list):
        D = boardstates_moves(movelist=movelist)
        for brdst in D.keys():
            i = len(brdst)/2
            self.gamestateboxes[i][brdst] = self.gamestateboxes[i][brdst] + self.drawreinforcefactor*[D[brdst]]
        return None  

    def reinforce_loss(self, movelist:list):
        D = boardstates_moves(movelist=movelist)
        for brdst in D.keys():
            i = len(brdst)/2
            for j in range(abs(self.lossreinforcefactor)):
                if D[brdst] in self.gamestateboxes[i][brdst]:
                    self.gamestateboxes[i][brdst].remove(D[brdst])
        return None  

    def reinforce(self, movelist:list, winner:int):
        if winner == 1:
            self.reinforce_win(movelist=movelist)
        elif winner == 2:
            self.reinforce_loss(movelist=movelist)
        else:
            self.reinforce_draw(movelist=movelist)
        return None


if __name__ == '__main__':
    # MB = Matchboxes()

    # result1 = ([2, 8, 9, 1, 4], 1)
    # result2 = ([2, 8, 9, 4, 7, 3], 2)
    # MB.reinforce(*result1)
    # MB.reinforce(*result2)
    # for i in range(5):
    #     for (key, value) in MB.gamestates[i].items():
    #         if value:
    #             print(key, value)

    MB = Matchboxes()

    for i in range(5):
        print(i, len(MB.gamestateboxes[i]))

    pass
    

