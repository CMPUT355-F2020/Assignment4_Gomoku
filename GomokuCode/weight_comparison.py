# This program is a replacement of the main() function in gomoku.py meant for weight training 
# It's purpose is to run the game based on a specific weight class and report the winner and 

from pattern_finder import Pattern
from Weights import Weights
from gomoku import * 

player_1 = 'x'
player_2 = 'o'

def compare_weights(weights_x, weights_o):
    
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
        current_board_state, current_player = alternate_moves(current_board_state, current_player, x_labels, weights_x, weights_o)
        display(current_board_state, x_labels, y_labels)
        
        isWin, winner =   found_winner(pattern, current_board_state)
        
        if isWin:
            print("Game Over")
            game_continue = False

    return current_board_state, winner 