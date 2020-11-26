import pygame


def draw_board(screen):
    screen.fill((132, 132, 130))
    pygame.draw.rect(screen, (0,0,0), (30,30,540,540), 1)
    pygame.draw.rect(screen, (193,154,107), (31,31,538,538))
    for pos in range(1,18):
        pygame.draw.line(screen, (0,0,0) ,(30, 30+30*pos), (569, 30+30*pos))
    for pos in range(1,18):
        pygame.draw.line(screen, (0,0,0) ,(30+30*pos, 30), (30+30*pos, 569))

def draw_piece(screen, sym, pos):
    if sym == 'x':
        clr = (255, 255, 255)
    else:
        clr = (0, 0, 0)
    loc = (30*(pos[0]+1), 30*(pos[1]+1))
    pygame.draw.circle(screen, clr, loc, 10)
    
def update_board(screen, board):
    draw_board(screen)
    for row in range(0, board.shape[0]):
        for col in range(0, board.shape[1]):
            if board[row, col] != '.':
                draw_piece(screen, board[row, col], (row, col))
                