import pygame


def draw_board(screen):
    screen.fill((132, 132, 130))
    pygame.draw.rect(screen, (0,0,0), (30,30, 420,420), 1)
    pygame.draw.rect(screen, (193,154,107), (31,31,418,418))
    for pos in range(1,14):
        pygame.draw.line(screen, (0,0,0) ,(30, 30+30*pos), (449, 30+30*pos))
    for pos in range(1,14):
        pygame.draw.line(screen, (0,0,0) ,(30+30*pos, 30), (30+30*pos, 449))

def draw_piece(screen, sym, pos):
    if sym == 'x':
        clr = (0, 0, 0)
    else:
        clr = (255, 255, 255)
    loc = (30*(pos[0]+1), 30*(pos[1]+1))
    pygame.draw.circle(screen, clr, loc, 10)
    
def update_board(screen, board):
    draw_board(screen)
    for row in range(0, board.shape[0]):
        for col in range(0, board.shape[1]):
            if board[row, col] != '.':
                draw_piece(screen, board[row, col], (row, col))
                
def get_input_pos(pos, board, player):
    outer = pygame.Rect(31,31,420,420)
    if outer.collidepoint(pos[0], pos[1]):
        for row in range(0, board.shape[0]):
            for col in range(0, board.shape[1]):
                loc = (30*(row+1), 30*(col+1))
                d = (loc[0]-pos[0])**2 + (loc[1] - pos[1])**2
                if d < 10**2:
                    if board[row, col] == '.':
                        board[row,col] = player
                        return True
                    else:
                        return False
    return False