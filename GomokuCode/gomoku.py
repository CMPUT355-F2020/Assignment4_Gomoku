# Gomoku Player 
# CMPUT 355 Assignment 4 

"""
TO DO LIST:

     1. implement function to calculate weights and fill the weight matrix
     2. test out player, optimize program if it's slow 
     3. make prettier (merge the Game.py code that uses pygame)

"""

import numpy as np
import pandas
import random
from pattern_finder import GFG
import time


# INPUT:  row and column dimensions 
# OUTPUT: returns 2D board matrix
def create_board(row,col): 
    board = np.full((row, col), '.')
    weights = np.full((row, col), 0)
    return board, weights


# INPUT:  2D board matrix and the x and y axis labels  
# OUTPUT: prints board
def display(board, x_labels, y_labels):
    print(pandas.DataFrame(board, columns=x_labels, index=y_labels))
    

# INPUT:  2D board matrix and the pattern_finder object  
# OUTPUT: returns True if one of the players won
def found_winner(gfg, board):
    locations, x_winner = gfg.patternSearch(board, 'xxxxx')
    locations, o_winner = gfg.patternSearch(board, 'ooooo')
    return x_winner or o_winner


# INPUT:  the x labels and the row size 
# OUTPUT: the row and column for the human players' next move 
def get_user_next_move(board, x_labels, row_size):
    valid = False 
    while not valid:
        col = input("Choose a column: ").lower()
        row = input("Choose a row: ")
        
        if (col in x_labels) and (row.isdigit()) and (int(row) <= row_size) and (int(row) >= 1) and (is_legal(board, [int(row)-1, x_labels.index(col)])):
            valid = True
        else:
            print("You chose an invalid location, choose again.")
    
    return int(row)-1, x_labels.index(col)


# INPUT:  2D board matrix, cell location 
# OUTPUT: returns True if that cell is empty (i.e. a move can be made) 
def is_legal(board, cell):
    if cell != None:
        return board[cell[0], cell[1]] == "."
    return False


# INPUT:  2D board matrix, current player, the x labels, and the pattern_finder object 
# OUTPUT: the new state of the board and the next player 
def alternate_moves(board, player, x_labels, gfg, board_weights):
    
    # human is player 1 (x)
    if player == 1:
        row, col = get_user_next_move(board, x_labels, len(board[0]))
        board[row][col] = 'x'
        next_player = 2
        
    # computer is player 2 (o)
    elif player == 2: 
        move = computer_player_random(board, gfg, board_weights) 
        #move = computer_player(board, gfg, board_weights)
        board[move[0]][move[1]] = 'o'
        next_player = 1
    
    return board, board_weights, next_player


# INPUT:  2D board matrix and the pattern_finder object 
# OUTPUT: returns the location of the next move 
def computer_player_random(board, gfg, board_weights):
    
    start_time = time.time()
    print("Computer is thinking... ")
    move = check_winning_move(board, gfg)
     
    if move == None: 
        move = get_defensive_move(board, gfg)
    
    if move == None:
        while not is_legal(board, move):
            move = random.randint(0, 14), random.randint(0, 14)
                    
    print("Computer chose row "+ str(move[0]) + " and column " + str(move[1]))
    print("Computer took", str(time.time() - start_time), "to make a move")
    
    return move


# INPUT:  2D board matrix and the pattern_finder object 
# OUTPUT: returns the location of the next move 
def computer_player(board, gfg, board_weights):
    
    start_time = time.time()
    print("Computer is thinking... ")
    distance_from_node = 5
    
    move = check_winning_move(board, gfg)
    
    if move == None:
            move = get_defensive_move(board, gfg)
    
    if move == None:
        board_weights = assign_weights(board, board_weights)
        move = max_move(board_weights)
    
    print("Computer chose row "+ str(move[0]) + " and column " + str(move[1]))
    print("Computer took", str(time.time() - start_time), "seconds to make a move")    
    
    return move


# INPUT:  2D board matrix, chain_locations
# OUTPUT: returns the location of the next move
def get_empty_cell(board, chain_locations):
    for location in chain_locations:
        if board[location[0], location[1]] == ".":
            return location
    return [-1,-1]


# INPUT:  2D board matrix, the pattern_finder object, and a list of chain locations to search through 
# OUTPUT: returns the location of the empty cell in the chain if it exists
def get_chain_location(gfg, board, chains):
    for chain in chains:
        chain_locations, found = gfg.patternSearch(board, chain)
        if found: 
            print("found chain: " + chain)  
            loc = get_empty_cell(board, chain_locations)
            break 
    if not found: loc = None  
    return loc 


# INPUT:  2D board matrix and the pattern_finder object
# OUTPUT: returns the location of the next move
def check_winning_move(board, gfg):
    winning_moves = ['.oooo', 'o.ooo', 'oo.oo']
    return get_chain_location(gfg, board, winning_moves)


# INPUT:  2D board matrix and the pattern_finder object 
# OUTPUT: returns the location of the next best defensive move if it exists 
def get_defensive_move(board, gfg):
    defensive_cells = ['.xxxx', 'x.xxx', 'xx.xx', '.x.xx.', '.xxx..']
    return get_chain_location(gfg, board, defensive_cells)
    
    
# INPUT:  2D board matrix (matrix)
#         board_weights (matrix) 
# OUTPUT: board_weights (matrix) with the weights filled in
def assign_weights(board, board_weights):
    pass
    
    
# INPUT:  2D board weight matrix
# OUTPUT: returns the location of the best offensive move 
def max_move(board_weights):
    return np.unravel_index(board_weights.argmax(), board_weights.shape)

    
def main():
     
    # initialize variables
    row = 15
    col = 15
    x_labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    y_labels = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14', '15']
    gfg = GFG()
    
    # set up the starting conditions
    game_continue = True 
    player = 1
    current_board_state, board_weights = create_board(row,col)
    display(current_board_state, x_labels, y_labels)
    
    # play game 
    while game_continue:
        print ("Player " + str(player) +"'s turn")
        current_board_state, board_weights, player = alternate_moves(current_board_state, player, x_labels, gfg, board_weights)
        display(current_board_state, x_labels, y_labels)
        if found_winner(gfg, current_board_state):
            print("Game Over")
            game_continue = False 
            
main()    