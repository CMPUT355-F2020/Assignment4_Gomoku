# Gomoku Player
# CMPUT 355 Assignment 4
# Group Name: ???

import numpy as np
import copy, pandas, random, time
from pattern_finder import Pattern
from Weights import Weights
from human_knowledge import *


player_1 = 'x'
player_2 = 'o'


# INPUT:  row and column dimensions
# OUTPUT: returns 2D board matrix
def create_board(row,col):
    board = np.full((row, col), '.')
    return board


# INPUT:  row and column dimensions
# OUTPUT: returns 2D weight matrix
def create_weight_matrix(row,col):
    weights = np.full((row, col), 0)
    return weights


# INPUT:  2D board matrix and the x and y axis labels
# OUTPUT: prints board
def display(board, x_labels, y_labels):
    print(pandas.DataFrame(board, columns=x_labels, index=y_labels))


# INPUT:  2D board matrix and the pattern_finder object
# OUTPUT: returns True if one of the players won
def found_winner(pattern, board):
    _, x_winner, _ = pattern.patternSearch(board, 'xxxxx', False)
    _, o_winner, _ = pattern.patternSearch(board, 'ooooo', False)
    
    if x_winner:
        return x_winner, player_1
    elif o_winner:
        return o_winner, player_2
    
    return False, ""


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
def alternate_moves(board, player, x_labels, weights_x, weights_o):
    
    pattern = Pattern()

    if player == player_1:  
        
        
        ## when both players are computers something goes wrong TODO- fix bug 
        ## comment out these 2 lines out if we want the computer to play itself 
        #row, col = get_user_next_move(board, x_labels, len(board[0]))
        #board[row][col] = player_1
        
        ## uncomment these 3 lines if we want the computer to play iteself
        opponent = player_2
        move = computer_player(board, pattern, player, opponent, weights_x, weights_o)
        board[move[0]][move[1]] = player_1        
        
        next_player = player_2

    elif player == player_2:
        opponent = player_1
        move = computer_player(board, pattern, player, opponent, weights_x, weights_o)
        board[move[0]][move[1]] = player_2
        next_player = player_1

    return board, next_player


# INPUT:  2D board matrix and the pattern_finder object
# OUTPUT: returns the location of the next move
def computer_player(board, pattern, player, opponent, weights_x, weights_o):

    start_time = time.time()

    op = Opening(player, opponent)
    bk = MustBlock()
    
    # 1. check opening moves 
    
    #  first move
    if op.first_move(board):
        move = [7,7]
        return move
    
    # second move
    if op.defence(board) == 1:
        for i in range(15):
            for j in range(15):
                if board[i][j] == opponent:   
                    #move = [i+1,j] #up
                    move = [i-1,j+1] #diag
                    return move
    # third move
    elif op.defence(board) == 2:
        for i in range(15):
            for j in range(15):
                if board[i][j] == opponent:   
                    if is_legal(board, [i+1, j+1]):
                        move = [i+1,j+1]
                        return move

    # 2. check winning moves
    move = check_winning_move(board, pattern, player)

    # 3. check defensive moves
    if move == None: 
        move = get_defensive_move(board, pattern, player)

    # 4. check must-block case moves
    if move == None:
        if player == player_1: block = bk.player_1[0]
        elif player == player_2: block = bk.player_2[0]
        move = get_chain_location(pattern, board, block)

    # 5. make move based on trained weights 
    if move == None:

        board_weights = assign_weights(board, player, opponent, weights_x, weights_o)
        #print(str(board_weights))
        move = max_move(board_weights, board)        

    #print("Computer chose row "+ str(move[0]) + " and column " + str(move[1]))
    #print("Computer took", str(time.time() - start_time), "to make a move")
    
    #print("IS LEGAL:"+str(is_legal(board, move)))

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
def get_chain_location(pattern, board, chains):
    for chain in chains:
        chain_locations, found, num_chains = pattern.patternSearch(board, chain, False)
        if found:
            loc = get_empty_cell(board, chain_locations)
            break
    if not found: loc = None
    if not is_legal(board, loc): loc = None 
    return loc


# INPUT:  2D board matrix and the pattern_finder object
# OUTPUT: returns the location of the next move
def check_winning_move(board, pattern, player):
    wn = Winning()
    if player == player_1: winning_moves = wn.player_1
    elif player == player_2: winning_moves = wn.player_2
    return get_chain_location(pattern, board, winning_moves)


# INPUT:  2D board matrix and the pattern_finder object
# OUTPUT: returns the location of the next best defensive move if it exists
def get_defensive_move(board, pattern, player):
    bk = MustBlock()
    if player == player_1: defensive_cells = bk.player_1[1]
    elif player == player_2: defensive_cells = bk.player_2[1]
    return get_chain_location(pattern, board, defensive_cells)


# INPUT:  2D board matrix (matrix)
# OUTPUT: board_weights (matrix) with the weights filled in
def assign_weights(board, player, opponent, w_x, w_o):   # TODO- clean this fxn 
    
    # TODO- check hr around latest move only 
    
    board_weights = create_weight_matrix(len(board),len(board[0]))
    
    # commented so that find_winner() in GA.py can send a weight class
    #w = Weights()
    
    Wx = np.array([w_x.w_1, w_x.w_2, w_x.w_3, w_x.w_4, w_x.w_5, w_x.w_6])
    Wo = np.array([w_o.w_1, w_o.w_2, w_o.w_3, w_o.w_4, w_o.w_5, w_o.w_6])
        
    for row in range(0, board_weights.shape[0]):
        for col in range(0, board_weights.shape[1]): 
            if is_legal(board, [row, col]):
                temp_board = copy.deepcopy(board)
                temp_board[row, col] = player 
                
                # player o 
                features_1, features_2 = check_chain_length(3,  temp_board, row, col, player)
                features_3, features_4 = check_chain_length(2,  temp_board, row, col, player)
                features_5, features_6 = check_chain_length(1,  temp_board, row, col, player)
                
                features = np.array([features_1, features_2,
                                     features_3, features_4,
                                     features_5, features_6])
                heuristic_o = np.dot(features, Wo)
                
                
                # player x
                features_1, features_2 = check_chain_length(3,  temp_board, row, col, opponent)
                features_3, features_4 = check_chain_length(2,  temp_board, row, col, opponent)
                features_5, features_6 = check_chain_length(1,  temp_board, row, col, opponent)
                
                features = np.array([features_1, features_2,
                                     features_3, features_4,
                                     features_5, features_6])
                heuristic_x = np.dot(features, Wx)
                
                board_weights[row][col] = heuristic_o - heuristic_x # fraction of x?
                
            elif not is_legal(board, [row, col]): 
                board_weights[row, col] = -1000000 # TODO - set to None
   
    return board_weights


# INPUT: the length of the chain to check, the location (x, y), and the current player
# OUTPUT: the number of chains of length n with 1 and 2 open ends 
def check_chain_length(n, board, x, y, player):
    board_subset = get_board_subset(board, x, y, (5,5))
    match = ""
    for _ in range(n):
        match += player
    match_2end = "." + match + "."
    match_1end = "." + match
    pattern = Pattern()
    if board_subset.shape[0] == 0 or board_subset.shape[1] == 0: board_subset = board
    _, _, num_chains_1_open_end = pattern.patternSearch(board_subset, match_1end, True)
    _, _, num_chains_2_open_ends = pattern.patternSearch(board_subset, match_2end, True)
    return num_chains_1_open_end, num_chains_2_open_ends


# INPUT: the board and its desired shape (surrounding locations x,y)
# OUTPUT: returns a subset of the board
def get_board_subset(board, x, y, new_shape):
    cropped_board = board[x - new_shape[0] - 1 : x + new_shape[0], y - new_shape[1] - 1 : y + new_shape[1]]
    return cropped_board


# INPUT:  2D board weight matrix
# OUTPUT: returns the location of the best offensive move 
def max_move(board_weights, board):

    max = board_weights.max()
    max_moves = []
    count = 0
    array_count = -1
    item_count = -1
    for array in board_weights:
        array_count += 1
        for item in array:
            item_count += 1
            if item_count > 15:
                item_count = item_count % 15
            if item == max and is_legal(board, [array_count, item_count ]):
                count += 1
                move = (array_count, item_count)
                max_moves.append(move)

    random_number = random.randint(0, count-1)
    random_max = max_moves[random_number]

    return random_max 


# Whenever we are training weights using weight_comparison.py, make sure main() is commented out 
"""
def main():

    # initialize variables
    row = 15
    col = 15
    x_labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    y_labels = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14', '15']
    pattern = Pattern()

    # set up the starting conditions
    game_continue = True
    current_player = player_1 # TODO - first player chosen randomly 
    current_board_state = create_board(row,col)
    display(current_board_state, x_labels, y_labels)

    # play game
    weights = Weights()
    while game_continue:
        print ("Player " + current_player +"'s turn")
        current_board_state, current_player = alternate_moves(current_board_state, current_player, x_labels, weights, weights)
        display(current_board_state, x_labels, y_labels)
        
        isWin, winner =   found_winner(pattern, current_board_state)
        
        if isWin:
            print("Game Over")
            game_continue = False

main()
"""