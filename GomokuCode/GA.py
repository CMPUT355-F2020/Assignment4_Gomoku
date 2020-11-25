import matplotlib.pyplot as plt
from Weights import Weights
from weight_comparison import compare_weights 
import numpy as np
import random 

def plot_fitness(fitness):
    plt.plot(fitness)
    plt.ylabel('fitness')
    plt.show(block=True)
    plt.interactive(False)

def fitness(fitness_brain1,fitness_brain2,win_cost_brain1,win_cost_brain2,cost,parent_brains):
    s = (cost) * (parent_brains - 1)
    fitness_brain1 += (win_cost_brain1**2)/s
    fitness_brain2 += (win_cost_brain2**2)/s
    return fitness_brain1,fitness_brain2

def crossover(brain1,brain2,rate):
    if np.random.randint(0,1/rate) == 1:
        temp = brain1.w_1
        brain1.w_1 = brain2.w_1
        brain2.w_1 = temp
    if np.random.randint(0,1/rate) == 1:
        temp = brain1.w_2
        brain1.w_2 = brain2.w_2
        brain2.w_2 = temp
    if np.random.randint(0,1/rate) == 1:
        temp = brain1.w_3
        brain1.w_3 = brain2.w_3
        brain2.w_3 = temp
    if np.random.randint(0,1/rate) == 1:
        temp = brain1.w_4
        brain1.w_4 = brain2.w_4
        brain2.w_4 = temp
    if np.random.randint(0,1/rate) == 1:
        temp = brain1.w_5
        brain1.w_5 = brain2.w_5
        brain2.w_5 = temp
    if np.random.randint(0,1/rate) == 1:
        temp = brain1.w_6
        brain1.w_6 = brain2.w_6
        brain2.w_6 = temp
    return brain1,brain2


def mutation(brain): #no mutation right now
    return brain

def brain_init(parent_brains):
    brains = []
    for _ in range(parent_brains):
        w = Weights()
        w.w_1 = np.random.randint(0, 100)
        w.w_2 = np.random.randint(0, 100)
        w.w_3 = np.random.randint(0, 100)
        w.w_4 = np.random.randint(0, 100)
        w.w_5 = np.random.randint(0, 100)
        w.w_6 = np.random.randint(0, 100)
        brains.append(w)
    return brains

def train():
    generation = 0
    parent_brains = 10 # search space
    games = 0 # number of games between parents--games = win_brain1 + win_brain2
    win_brain1 = 0 #number of games won by brain 1
    win_brain2 = 0 #number od games won by brain 2
    cost = 0 # total number of moves in all the games
    win_cost_brain1 = 0 # total number of moves in the games won by brain1
    win_cost_brain2 = 0 # total number of moves in the games won by brain2
    crossover_rate = 0.01

    brains = brain_init(parent_brains)
    pass #TO BE FINISHED


# arguments are 2 weight classes 
def find_winner(weights_x, weights_o):
    
    player_1 = 'x'
    player_2 = 'o'
    
    board, winner = compare_weights(weights_x, weights_o)
    
    if winner == player_1:
        weight_winner = weights_x
    elif winner == player_2: 
        weight_winner = weights_o
    else: # tie game 
        weight_winner = random.choice([weights_x, weights_o])
    
    num_moves_x, num_moves_o = 0, 0
    for i in range(0, board.shape[0]):
        for j in range(0, board.shape[1]): 
            if board[i][j] == player_1:
                num_moves_x += 1
            elif board[i][j] == player_2:
                num_moves_o += 1
    
    return weight_winner, num_moves_x, num_moves_o 


crossover(0.5)