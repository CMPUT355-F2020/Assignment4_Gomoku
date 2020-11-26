# An Evolutionary Approach to optimize the weights (ง'̀-'́)ง

import matplotlib.pyplot as plt
from Weights import Weights
from weight_comparison import compare_weights
from itertools import combinations
import numpy as np
import random 

def plot_fitness(fitness):
    plt.plot(fitness)
    plt.ylabel('fitness')
    plt.show(block=True)
    plt.interactive(False)

#The fitness function evaluate the performance of each brain
def fitness(fitness_brain1,fitness_brain2,win_cost_brain1,win_cost_brain2,cost,parent_brains):
    s = (cost) * (parent_brains - 1)
    fitness_brain1 += (win_cost_brain1**2)/s
    fitness_brain2 += (win_cost_brain2**2)/s
    return fitness_brain1,fitness_brain2

'''
w_1 # length 3 with 1 open end 
w_2 # length 3 with 2 open ends
w_3 # length 2 with 1 open end
w_4 # length 2 with 2 open ends---->attack
w_5 # length 1 with 1 open end
w_6 # length 1 with 2 open ends
Note that the player can be strengthened by adding more w_i   
'''

# The crossover function swaps the wights of two brains regarding the crossover_rate
def crossover(brain1,brain2,rate):
    if np.random.randint(0, 1 / rate) == 1: brain1.w_1, brain2.w_1 = brain2.w_1, brain1.w_1
    if np.random.randint(0, 1 / rate) == 1: brain1.w_2, brain2.w_2 = brain2.w_2, brain1.w_2
    if np.random.randint(0, 1 / rate) == 1: brain1.w_3, brain2.w_3 = brain2.w_3, brain1.w_3
    if np.random.randint(0, 1 / rate) == 1: brain1.w_4, brain2.w_4 = brain2.w_4, brain1.w_4
    if np.random.randint(0, 1 / rate) == 1: brain1.w_5, brain2.w_5 = brain2.w_5, brain1.w_5
    if np.random.randint(0, 1 / rate) == 1: brain1.w_6, brain2.w_6 = brain2.w_6, brain1.w_6
    return brain1,brain2

# The mutation function slightly adjusts the weights
def mutation(brain, stable_rate): # epsilon greedy decision
    if random.random() < stable_rate: # ~1:stable ~0:unstable
        brain.w_1 += 0.5
        brain.w_2 += 1.2
        brain.w_3 += 0.3
        brain.w_4 += 0.5
        brain.w_5 += 0.1
        brain.w_6 += 0.2
    else: # add a normally distributed noise to the weights
        brain.w_1 += np.random.normal(0,1)
        brain.w_2 += np.random.normal(0,1)
        brain.w_3 += np.random.normal(0,1)
        brain.w_4 += np.random.normal(0,1)
        brain.w_5 += np.random.normal(0,1)
        brain.w_6 += np.random.normal(0,1)
    return brain

# Initialize two brains and assign random weights to them
def brain_init(parent_brains):
    brains = []
    for _ in range(parent_brains):
        w = Weights()
        w.w_1 = np.random.randint(0, 20)
        w.w_2 = np.random.randint(0, 20)
        w.w_3 = np.random.randint(0, 20)
        w.w_4 = np.random.randint(0, 20)
        w.w_5 = np.random.randint(0, 20)
        w.w_6 = np.random.randint(0, 20)
        brains.append(w)
    return brains

# arguments are 2 weight classes
def find_winner(weights_x, weights_o):
    player_1 = 'x'
    player_2 = 'o'

    board, winner = compare_weights(weights_x, weights_o)

    if winner == player_1:
        weight_winner = weights_x
    elif winner == player_2:
        weight_winner = weights_o
    else:  # tie game
        weight_winner = random.choice([weights_x, weights_o])

    winner_move = 0
    win1_move = 0
    win2_move = 0
    num_moves_x, num_moves_o = 0, 0
    for i in range(0, board.shape[0]):
        for j in range(0, board.shape[1]):
            if board[i][j] == player_1:
                num_moves_x += 1
            elif board[i][j] == player_2:
                num_moves_o += 1

    winner_move = num_moves_x if winner == player_1 else num_moves_o
    win1_move = num_moves_x if winner == player_1 else 0
    win2_move = num_moves_o if winner == player_2 else 0
    return weight_winner, num_moves_x, num_moves_o, winner_move, win1_move, win2_move

# Select two strong brains as parents and the weakest brain as elimination
def selection(brain_list,mode):# mode = elimination or parent
    f_list = []
    for i in brain_list:
        f_list.append(i.fitness)
    if mode == "p":
        p1,p2 = sorted(range(len(f_list)), key=lambda i: f_list[i], reverse=True)[:2]
        return brain_list[p1],brain_list[p2]
    if mode == "e":
        e = sorted(range(len(f_list)), key=lambda i: f_list[i], reverse=False)[:1]
        return brain_list[e[0]]

# This function returns the best weights so far
def optimal_weights(brain_list,fitness_list):
    max_value = max(fitness_list)
    max_index = fitness_list.index(max_value)
    return brain_list[max_index]

def train():
    generation = 0 # number of generations
    parent_brains = 2 # init search space
    crossover_rate = 0.3
    mutation_stable_rate = 0.95
    fitness_track = [] # track all the fitness value so far
    brain_track = [] # track all the brains in history

    brains = brain_init(parent_brains)  # a list of random brains
    population = brains
    while generation < 3:
        pairs = list(combinations(population, 2))  # a list of tuples i.e [(a,b),(b,c),(a,c)]
        print("Training......")
        # update fitness value for each weights
        for i in pairs:
            i = list(i)

            # win1: total number of moves in the games won by brain1
            # win2: total number of moves in the games won by brain2
            # cost: total number of moves in all the games
            x,y,z,win,win1,win2 = find_winner(i[0],i[1]) # weight_winner, num_moves_x, num_moves_o, winner_move
            cost = y + z
            f1,f2 = fitness(i[0].fitness,i[1].fitness,win1,win2,cost,parent_brains)
            i[0].fitness,i[1].fitness = f1,f2
            fitness_track.append(i[0].fitness)
            fitness_track.append(i[1].fitness)
            brain_track.append(i[0])
            brain_track.append(i[1])
            plot_fitness(fitness_track)
            best = optimal_weights(brain_track, fitness_track)
            print("The best weights so far:", best.w_1, best.w_2, best.w_3, best.w_4, best.w_5, best.w_6)

        # Evolution start
        e = selection(population,"e") # worst brain
        p1,p2 = selection(population,"p") # best two brains
        temp1,temp2 = crossover(p1,p2,crossover_rate)
        temp1 = mutation(temp1,mutation_stable_rate)
        temp2 = mutation(temp2,mutation_stable_rate)
        population.remove(e)
        population.append(temp1)
        population.append(temp2)

        # one generation ended
        generation += 1
        print("End of generation "+str(generation)+"----------------------------------------------------------")

train()
