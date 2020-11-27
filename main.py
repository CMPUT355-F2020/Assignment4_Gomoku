from pattern_finder import Pattern
from Weights import Weights
from gomoku import * 
import pygame
from display import *

player_1 = 'x'
player_2 = 'o'


def check_win(pattern, board, screen):
    isWin, winner = found_winner(pattern, board)
    if isWin:
        if winner == 'x':
            message = 'You Won'
        else:
            message = 'You Lost'
        font = pygame.font.SysFont('arial', 20)
        text = font.render('Game Over: '+ message, True, (0, 0, 0))
        textRect = text.get_rect()
        screen.blit(text, textRect)
        textRect.center = (300, 300)
        pygame.display.update()
        return True
    else:
        return False

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
    # play game
    weights = Weights()
    pygame.init()
    screen = pygame.display.set_mode((490, 490))
    pygame.display.set_caption("Gomoku")
    icon = pygame.image.load('assets/gomoku.png')
    pygame.display.set_icon(icon)
    while running:
        clicked = False
        got_input = False
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and game_continue:
                    got_input = get_input_pos(event.pos, current_board_state, 'x')
                    clicked = True
                    update_board(screen, current_board_state)
                    pygame.display.update()
                    game_continue = not check_win(pattern, current_board_state, screen)
        if game_continue:
            update_board(screen, current_board_state)
            pygame.display.update()
            if clicked and got_input:
                font = pygame.font.SysFont('arial', 15) 
                text = font.render('Waiting for Computer Move', True, (0, 0, 0))
                textRect = text.get_rect()
                screen.blit(text, textRect)
                textRect.center = (300, 300)
                pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                pygame.display.update()
                current_board_state, _ = alternate_moves(current_board_state, 'o', x_labels, weights, weights)
                update_board(screen, current_board_state)
                pygame.display.update()
                pygame.event.set_allowed(None)
            game_continue = not check_win(pattern, current_board_state, screen)                
main()
