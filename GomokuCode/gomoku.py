# Gomoku Player
# CMPUT 355 Assignment 4
# Group Name: ???

import numpy as np
import copy
import pandas
import random
from pattern_finder import Pattern
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
    locations, x_winner, num_chains = gfg.patternSearch(board, 'xxxxx', False)
    locations, o_winner, num_chains = gfg.patternSearch(board, 'ooooo', False)
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
        move = computer_player(board, gfg, board_weights)
        board[move[0]][move[1]] = 'o'
        next_player = 1

    return board, board_weights, next_player


# INPUT:  2D board matrix and the pattern_finder object
# OUTPUT: returns the location of the next move
def computer_player(board, gfg, board_weights):

    start_time = time.time()
    
    move = check_winning_move(board, gfg)

    if move == None:
        move = get_defensive_move(board, gfg)

    if move == None: # special cases 
        move = get_chain_location(gfg, board, ['.x.xx.','.ooo..'])
    
    if move == None:
        board_weights = assign_weights(board, board_weights)
        move = max_move(board_weights)        

    print("Computer chose row "+ str(move[0]) + " and column " + str(move[1]))
    print("Computer took", str(time.time() - start_time), "to make a move")

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
        chain_locations, found, num_chains = gfg.patternSearch(board, chain, False)
        if found:
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

class Weights:# To be trained
    def  __init__(self):
        self.w_1 = 1
        self.w_2 = 1
        self.w_3 = 1
        self.w_4 = 1
        self.w_5 = 1
        self.w_6 = 1
        
# INPUT:  2D board matrix (matrix)
#         board_weights (matrix)
# OUTPUT: board_weights (matrix) with the weights filled in
def assign_weights(board, board_weights): 

    player = 'o' # TODO- pass player to this fxn
    w = Weights()
    W = np.array([w.w_1,w.w_2,w.w_3,w.w_4,w.w_5,w.w_6])
    for row in range(0, board_weights.shape[0]):
        for col in range(0, board_weights.shape[1]): 
            if is_legal(board, [row, col]):
                temp_board = copy.deepcopy(board)
                temp_board[row, col] = 'o'
                features_1, features_2 = check_chain_length(3,  temp_board, row, col, player)
                features_3, features_4 = check_chain_length(2,  temp_board, row, col, player)
                features_5, features_6 = check_chain_length(1,  temp_board, row, col, player)
                features = np.array([features_1, features_2,
                                    features_3, features_4,
                                    features_5, features_6])
                board_weights[row][col] = np.dot(features, W)
            else: 
                board_weights[row, col] = -1
    return board_weights


# INPUT:  
# OUTPUT: 
def check_chain_length(n, board, x, y, player):
    board_subset = get_board_subset(board, x, y, (5,5))
    
    match = ""
    for _ in range(n):
        match += player
    match_2end = "." + match + "."
    match_1end = "." + match
    pattern = Pattern()
    _, _, num_chains_1_open_end = pattern.patternSearch(board_subset, match_1end, True)
    _, _, num_chains_2_open_ends = pattern.patternSearch(board_subset, match_2end, True)
    return num_chains_1_open_end, num_chains_2_open_ends


# INPUT: the board and its desired shape (surrounding locations x,y)
# OUTPUT: returns a 5by5 subset of the board
def get_board_subset(board, x, y, new_shape):
    cropped_board = board[x - new_shape[0] - 1 : x + new_shape[0], y - new_shape[1] - 1 : y + new_shape[1]]
    return cropped_board


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
    gfg = Pattern()

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
