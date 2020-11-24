import numpy as np
'''
Apply human knowledge to strength the player and save runtime. 
'''
class Opening:
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent 

    def defence(self,board):
        count = 0
        for i in range(15):
            for j in range (15):
                if board[i][j] == self.opponent: # opponent, remove hard coded values
                    count += 1
        if count < 3 and count >= 0:
            return count

    #Attack
    def first_move(self,board):# check whether the board is empty
        count = 0
        for i in range(15):
            for j in range (15):
                if board[i][j] == self.opponent or board[i][j] == self.player:
                    count += 1
        if count == 0:
            return True # always place the stone in the middle (8h) Best_move & Best_runtime
        return False 

    def second_move_diagonal(self,board):#check whether the opponent put a stone in the diagonal directions
        if (board[7][7] + board[7][9] + board[9][7] + board[9][9]) != '....':
            return True

    def second_move_horizontal(self,board):#check whether the opponent put a stone in the horizontal directions
        if (board[7][8] + board[8][7] + board[8][9] + board[9][8]) != '....':
            return True

class MustBlock:
    def __init__(self):
        self.player_1 = [['.x.xx.','.xxx..'],['.oooo', 'o.ooo', 'oo.oo', '.o.oo.', '.ooo..']]
        self.player_2 = [['.o.oo.','.ooo..'],['.xxxx', 'x.xxx', 'xx.xx', '.x.xx.', '.xxx..']]

class Winning:
    def __init__(self):
        self.player_1 = ['.xxxx', 'x.xxx', 'xx.xx']
        self.player_2 = ['.oooo', 'o.ooo', 'oo.oo']

class Other:
    def __init__(self):
        pass