# Gomoku Player 
# CMPUT 355 Assignment 4 

import numpy as np
import pandas
import random
from pattern_finder import GFG

def create_board(row,col): 
    return np.full((row, col), '.') 


def display(board, x, y):
    print(pandas.DataFrame(board, columns=x, index=y))
    
def making_dict(board, x, y):


    game_dict = {'a0': 0, 'a1': 0, 'a2': 0, 'a3': 0, 'a4': 0, 'a5': 0, 'a6': 0, 'a7': 0, 'a8': 0, 'a9': 0, 'a10': 0,
            'a11': 0,'a12': 0,'a13': 0,'a14': 0,
            'b0': 0, 'b1': 0, 'b2': 0, 'b3': 0, 'b4': 0, 'b5': 0, 'b6': 0, 'b7': 0, 'b8': 0, 'b9': 0, 'b10': 0,
            'b11': 0,'b12': 0,'b13': 0,'b14': 0,
            'c0': 0, 'c1': 0, 'c2': 0, 'c3': 0, 'c4': 0, 'c5': 0, 'c6': 0, 'c7': 0, 'c8': 0, 'c9': 0, 'c10': 0,
            'c11': 0,'c12': 0,'c13': 0,'c14': 0,
            'd0': 0, 'd1': 0, 'd2': 0, 'd3': 0, 'd4': 0, 'd5': 0, 'd6': 0, 'd7': 0, 'd8': 0, 'd9': 0, 'd10': 0,
            'd11': 0,'d12': 0,'d13': 0,'d14': 0,
            'e0': 0, 'e1': 0, 'e2': 0, 'e3': 0, 'e4': 0, 'e5': 0, 'e6': 0, 'e7': 0, 'e8': 0, 'e9': 0, 'e10': 0,
            'e11': 0,'e12': 0,'e13': 0,'e14': 0,
            'f0': 0, 'f1': 0, 'f2': 0, 'f3': 0, 'f4': 0, 'f5': 0, 'f6': 0, 'f7': 0, 'f8': 0, 'f9': 0, 'f10': 0,
            'f11': 0,'f12': 0,'f13': 0,'f14': 0,
            'g0': 0, 'g1': 0, 'g2': 0, 'g3': 0, 'g4': 0, 'g5': 0, 'g6': 0, 'g7': 0, 'g8': 0, 'g9': 0, 'g10': 0,
            'g11': 0,'g12': 0,'g13': 0,'g14': 0,
            'h0': 0, 'h1': 0, 'h2': 0, 'h3': 0, 'h4': 0, 'h5': 0, 'h6': 0, 'h7': 0, 'h8': 0, 'h9': 0, 'h10': 0,
            'h11': 0,'h12': 0,'h13': 0,'h14': 0,
            'i0': 0, 'i1': 0, 'i2': 0, 'i3': 0, 'i4': 0, 'i5': 0, 'i6': 0, 'i7': 0, 'i8': 0, 'i9': 0, 'i10': 0,
            'i11': 0,'i12': 0,'i13': 0,'i14': 0,
            'j0': 0, 'j2': 0, 'j2': 0, 'j3': 0, 'j4': 0, 'j5': 0, 'j6': 0, 'j7': 0, 'j8': 0, 'j9': 0, 'j10': 0,
            'j11': 0,'j12': 0,'j13': 0,'j14': 0,
            'k0': 0, 'k1': 0, 'k2': 0, 'k3': 0, 'k4': 0, 'k5': 0, 'k6': 0, 'k7': 0, 'k8': 0, 'k9': 0, 'k10': 0,
            'k11': 0,'k12': 0,'k13': 0,'k14': 0,
            'l0': 0, 'l1': 0, 'l2': 0, 'l3': 0, 'l4': 0, 'l5': 0, 'l6': 0, 'l7': 0, 'l8': 0, 'l9': 0, 'l10': 0,
            'l11': 0,'l12': 0,'l13': 0,'l14': 0,
            'm0': 0, 'm1': 0, 'm2': 0, 'm3': 0, 'm4': 0, 'm5': 0, 'm6': 0, 'm7': 0, 'm8': 0, 'm9': 0, 'm10': 0,
            'm11': 0,'m12': 0,'m13': 0,'m14': 0,
            'n0': 0, 'n1': 0, 'n2': 0, 'n3': 0, 'n4': 0, 'n5': 0, 'n6': 0, 'n7': 0, 'n8': 0, 'n9': 0, 'n10': 0,
            'n11': 0,'n12': 0,'n13': 0,'n14': 0,
            'o0': 0, 'o1': 0, 'o2': 0, 'o3': 0, 'o4': 0, 'o5': 0, 'o6': 0, 'o7': 0, 'o8': 0, 'o9': 0, 'o10': 0,
            'o11': 0,'o12': 0,'o13': 0,'o14': 0,
    }
    # size of board
    size = 15

    legal_moves = {}
    row_num = -1 
    col_num = -1
    items = 0 
    for row in board:
        row_num = (row_num + 1) # +97 if we want to have the letters- converting with ascii
        # print('row: ', row_num) 

        for item in row:
            col_num = ((col_num + 1) % size)
            # print('col: ', col_num)

            if item == '.':
                items += 1 # this tells us that the code is reading all the right positions 
                action = str(row_num) + ', ' + str(col_num)
                legal_moves[action] = 0

    print('items: ', items)
    # for move in legal_moves:
    #     print(move)
    print(legal_moves)
    return legal_moves
    # now we must call another function to ge the weights of the positions above- basically the entire board

def chain_lens(board, player):
    # if player is x, then we are checking for number of x's in a row; else we check the o's
    # player is 1 or 2- let's check what that means
    # 1 is player while 2 is the computer
    # i would think that we just need to worry about the computer, so that would be 2; if i have this wrong, 
    # this would be a quick fix so theis is not a big deal 

    # so this fucntion will only be called when it is the computer's turn to play- so we probably do not need to 
    # pass player into this function 

    # if we are searching for computer, then we only need to be looking for o's - also a quick fix
    # finding the len of a chain- first horizontal and then vertical 
    count = 0 
    for row in board:
        for item in row:
            if item == 'x':
                count += 1
                # the count is being incremented regardless of which row the x is in. we can change this by 
                # adding the count to a list, and then chaning the count to 0 after that row. 
                # this way we can store the value of the count and keep track/row
    print(board)
    print(count)
    return None
def found_winner(gfg, board):
    return gfg.patternSearch(board, 'xxxxx') or gfg.patternSearch(board, 'ooooo')
    

# human is player 1 (x) and computer is player 2 (o)
# TODO: add error handling
        # if they do not enter a valid row or column, ask again
        # if they choose an occupied cell, ask again 
def make_move(board, player):
    
    if player == 1:
        # move = input('Please enter a move: ')
        # col_move = move[0]
        # row_move = int(move[1])
        row_move = int(input("Choose a row: "))
        col_move = int(input("Choose a column: "))
        board[row_move][col_move] = 'x'
        next_player = 2
        
    elif player == 2: 
        row_move, col_move = computer_player_random(board)
        #computer_player_ai(board)
        #row_move, col_move = computer_player_mimimax(board)
        board[row_move][col_move] = 'o'
        next_player = 1
    
    return board, next_player


def computer_player_random(board):
    print("Computer is thinking... ")
    done = False 
    while not done:
        row = random.randint(0, 14)
        col = random.randint(0, 14)
        if board[row][col] == '.':
            done = True
    print("Computer chose row "+ str(row) + " and column " + str(col))
    return row, col

    
"""
STEP 1 - defence (check if human has 3 in a row, if yes, block them)
STEP 2 - offence
         
         We want to track two things:
               1. the number of x's in each chain  
               2. the number of open ends for each chain (can I build off of this chain?)
        
        LATER - track my x positions using a dictionary for optimization
         
         track the number of x's I have in a row (1,2,3,4) and build off of them, if possible
         focus on the longest chain 
         see if we can add to the open end 
         if small chain - use minimax/alphabeta to make best decision 
         
"""

# currently in progress
def computer_player(board):
    
    # if gfg.patternSearch(board, 'ooo'): 
        # defend

    return 
    # else: 
    #     offend()

# def offend():
#          if chain_length == 4 and open_ends == True: #CAN WIN
         
#          elif chain_length == 3 and open_ends == True: #put x on one of the open ends to make chain of 4 
         
#          elif chain_length == 2 and open_ends == True: #use alpha beta to make best decision 
         
#          else: use alpha beta to make best decision 
        
"""
"""

def offend():
    pass 

    
def main():
     
    # initialize variables
    row = 15
    col = 15
    x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    y = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14']
    gfg = GFG()
    
    # set up the starting conditions
    game_continue = True 
    player = 1
    current_board_state = create_board(row,col)
    display(current_board_state, x, y)
    
    # play game 
    while game_continue:
        
        print ("Player " + str(player) +"'s turn")
        
        current_board_state, player = make_move(current_board_state, player)
        display(current_board_state, x, y)
        making_dict(current_board_state, x, y)
        # chain_lens(current_board_state, player)
        
        if found_winner(gfg, current_board_state):
            print("Game Over")
            game_continue = False 
            
main()    