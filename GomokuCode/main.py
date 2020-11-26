from pattern_finder import Pattern
from Weights import Weights
from gomoku import * 
import pygame
from display import *

player_1 = 'x'
player_2 = 'o'

# main function for gomoku game 

def main():

    # initialize variables
    row = 15
    col = 15
    x_labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    y_labels = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14', '15']
    pattern = Pattern()

    # set up the starting conditions
    game_continue = True
    running = True
    current_player = player_1 # TODO - first player chosen randomly 
    current_board_state = create_board(row,col)
    display(current_board_state, x_labels, y_labels)

    # play game
    weights = Weights()
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Gomoku")
    icon = pygame.image.load('GomokuCode/assets/gomoku.png')
    pygame.display.set_icon(icon)
    while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        if game_continue:
            print ("Player " + current_player +"'s turn")
            current_board_state, current_player = alternate_moves(current_board_state, current_player, x_labels, weights, weights)
            update_board(screen, current_board_state)
            pygame.display.update()
            display(current_board_state,x_labels, y_labels)
            isWin, winner = found_winner(pattern, current_board_state)
            if isWin:
                print("Game Over")
                game_continue = False
                
main()