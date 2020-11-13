# Gomoku Player 
# CMPUT 355 Assignment 4 


import numpy as np
import pandas
import random
from pattern_finder import GFG


def create_board(row,col): 
    return np.full((row, col), '.') 


def display(board, x_labels, y_labels):
    print(pandas.DataFrame(board, columns=x_labels, index=y_labels))
    
 
def found_winner(gfg, board):
    return gfg.patternSearch(board, 'xxxxx') or gfg.patternSearch(board, 'ooooo')
    

# human is player 1 (x) and computer is player 2 (o)
# TODO: add error handling
        # if they do not enter a valid row or column, ask again
        # if they choose an occupied cell, ask again         
def alternate_moves(board, player, x_labels):
    
    if player == 1:
        col_letter = input("Choose a column: ").lower()
        col_number = x_labels.index(col_letter)
        row_move = int(input("Choose a row: "))
        board[row_move][col_number] = 'x'
        next_player = 2
        
    elif player == 2: 
        row_move, col_move = computer_player_random(board)
        #location = computer_player(board)
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

# INPUT:  2D board matrix
# OUTPUT: returns a location for next move (use alpha-number format, for example: a0)
def computer_player(board):
    
    move = check_winning_move(board)
    
    if move == None:
            move = get_defensive_move(board)
    
    if move == None:
        move = make_offensive_move(board)
    
    return move


# INPUT:  2D board matrix
# OUTPUT: returns a location  (use alpha-number format, for example: a0)
def check_winning_move(board):
    pass


# INPUT:  2D board matrix
# OUTPUT: returns a location  (use alpha-number format, for example: a0)
def get_defensive_move(board):
    pass


# INPUT:  2D board matrix (list)
#         distance_from_node (integer) - how far out we want to look to make chain bigger
# OUTPUT: returns dict_promising_cells (dictionary) - dict of {location:weight}
#         initialize all weights to 0  
def find_promising_cells(board, distance_from_node):
    pass
    
    
# INPUT:  2D board matrix (list)
#         dict_promising_cells (dictionary) - dict of {location:weight}
# OUTPUT: dict_promising_cells (dictionary) with the weights filled in
def assign_weights(board, dict_promising_cells):
    pass
    
    
# INPUT:  2D board matrix
#         dict_promising_cells (dictionary) - dict of {location:weight}
# OUTPUT: returns the location of the best move (use alpha-number format, for example: a0)
def best_move(board, dict_promising_cells):
    pass

    
def main():
     
    # initialize variables
    row = 15
    col = 15
    x_labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    y_labels = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14']
    gfg = GFG()
    
    # set up the starting conditions
    game_continue = True 
    player = 1
    current_board_state = create_board(row,col)
    display(current_board_state, x_labels, y_labels)
    
    # play game 
    while game_continue:
        
        print ("Player " + str(player) +"'s turn")
        
        current_board_state, player = alternate_moves(current_board_state, player, x_labels)
        display(current_board_state, x_labels, y_labels)
        
        if found_winner(gfg, current_board_state):
            print("Game Over")
            game_continue = False 
            
main()    