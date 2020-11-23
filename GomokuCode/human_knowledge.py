import numpy as np
'''
Apply human knowledge to strength the player and save runtime. 
'''
class Opening:
    def __init__(self):
        pass

    def defence(self):
        pass # any attached cell

    def first_move(self,board):# check whether the board is empty
        if board == np.full((15, 15),'.'):
            return True # always place the stone in the middle (8h) Best_move & Best_runtime

    def second_move_diagonal(self,board):#check whether the opponent put a stone in the diagonal directions
        if (board[7][7] + board[7][9] + board[9][7] + board[9][9]) != '....':
            return True

    def second_move_horizontal(self,board):#check whether the opponent put a stone in the horizontal directions
        if (board[7][8] + board[8][7] + board[8][9] + board[9][8]) != '....':
            return True

class Other:
    def __init__(self):
        pass