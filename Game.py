import pygame
import pickle
from string import ascii_lowercase
from pathlib import Path
import os, sys

def draw_board(screen):
    screen.fill((132, 132, 130))
    pygame.draw.rect(screen, (0,0,0), (30,30,540,540), 1)
    pygame.draw.rect(screen, (193,154,107), (31,31,538,538))
    for pos in range(1,18):
        pygame.draw.line(screen, (0,0,0) ,(30, 30+30*pos), (569, 30+30*pos))
    for pos in range(1,18):
        pygame.draw.line(screen, (0,0,0) ,(30+30*pos, 30), (30+30*pos, 569))

def load_dict():
    if not os.path.exists("assets/data.pkl"):
        gdict = init_dict()
    else:
        with open("assets/data.pkl", 'rb') as handle:
            gdict = pickle.load(handle)
    return gdict

def load_clr():
    if not os.path.exists("assets/clr.txt"):
        return (0, 0, 0)
    else:
        with open("assets/clr.txt", 'r') as handle:
            clr = handle.read()      
        if clr == 'WHITE':
            return (255, 255, 255)
        else:
            return (0, 0, 0)
    
        
def init_dict():
    gdict = {}
    horc = 0
    for letter in ascii_lowercase[:19]:
        verc = 0
        for number in range(19, 0, -1):
            gdict[letter + str(number)] = [30*(horc+1), 30*(verc+1), -1]
            verc += 1
        horc += 1
    return gdict

def draw_piece(screen, clr, pos):
    pygame.draw.circle(screen, clr, pos, 10)

def play(gdict, pos, clr):
    (gdict[pos])[2] = clr
    draw_piece(screen, clr, ((gdict[pos])[0], (gdict[pos])[1]))

def check_legal(gdict, pos):
    if gdict[pos] == -1:
        return 0
    else:
        return 1

def invert_clr(clr):
    if clr == 'WHITE':
        return 'BLACK'
    else:
        return 'WHITE'

def save_data(gdict, clr):
    with open("assets/data.pkl", 'wb') as handle:
            pickle.dump(gdict, handle, pickle.HIGHEST_PROTOCOL)
    with open("assets/clr.txt", 'w') as handle:
            handle.write(clr)

def update_board_dict(screen, gdict):
    for key in gdict.keys():
        if (gdict[key])[2] != -1:
            draw_piece(screen, (gdict[key])[2], ((gdict[key])[0], (gdict[key])[1]))

def end_game():
    if os.path.exists("assets/data.pkl"):
        os.remove("assets/data.pkl")
    else:
        print("Error: Start game first")
    if os.path.exists("assets/clr.txt"):
        os.remove("assets/clr.txt")
    sys.exit(0)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Gomoku")
    icon = pygame.image.load('assets/gomoku.png')
    pygame.display.set_icon(icon)
    running = True
    only_itr = 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if only_itr:    
            draw_board(screen)
            gdict = load_dict()
            clr = load_clr()
            update_board_dict(screen, gdict)
            pygame.display.update()
            pos = input("Enter the position you want to play: ")
            if pos == "quit":
                end_game()
            if check_legal(gdict, pos):
                play(gdict, pos, clr)    
            else:    
                print("Error: Position occupied")
            only_itr = 0
            if clr == (0, 0, 0):         
                save_data(gdict, invert_clr('BLACK'))
            else:
                save_data(gdict, invert_clr('WHITE'))
            pygame.display.update()
