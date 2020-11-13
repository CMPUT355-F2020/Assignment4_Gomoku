# An Evolutionary Approach to Gomoku
# This solver is expected to be weaker than alpha-beta (｡•́︿•̀｡) but it's fun!
# Some human-generated opening moves might be able to strengthen this solver though (ง'̀-'́)ง
# I will use Genetic Algorithm(or Neural Network) to optimize the weights
# Avoid using too many libraries
# Linhao Xian 1461630
# # # # # # # # # # # # # # # # #

# We will use a 1x5 filter to scan the board vertically/horizontally/diagonally
# (Like a convolutional layer with stride = 1)
# for a 9x9 board, there will be 4x5=20 values
board_size = 9
"""
Following weights are to be updated
"""
# These values measure the importance of each combination
# To be trained
empty = 1.1  # the 1x5 array is empty
m1 = 10  # one stone for my side
m2 = 50
m3 = 100
m4 = 1000
o1 = 10  # one stone for opponent
o2 = 50
o3 = 1000
o4 = 2000
polluted = 0 # mixed stones

'''
I am not trying to implement the rules or game
Board_matrix is for showing the current state only
Weight_matrix tracks the weight of each position
'''

# define x = my_stone
# define s = op_stone
# define 0 = empty

def gen_board(board_size):
    board_matrix = []
    weight_matrix = []
    for i in range(board_size):
        board_matrix.append([0] * board_size)
        weight_matrix.append([0.0] * board_size)
    return board_matrix, weight_matrix

def show_board(board_matrix):
    for i in range(board_size):
        print(*board_matrix[i],sep="  ")

def move(board_matrix,color,pos):
    board_matrix[pos[0]][pos[1]] = color

'''
           0 0 0 0 0
           0 0 x 0 0
           0 0 0 0 0
Scan the whole board for 1x5 arrays           
'''
def score(x,s,e):# me,op,emp
    if x == 0 and s == 0 and e == 5:
        return empty
    elif x == 1 and s == 0 and e == 4:
        return m1
    elif x == 2 and s == 0 and e == 3:
        return m2
    elif x == 3 and s == 0 and e == 2:
        return m3
    elif x == 4 and s == 0 and e == 1:
        return m4
    elif x == 0 and s == 1 and e == 4:
        return o1
    elif x == 0 and s == 2 and e == 3:
        return o2
    elif x == 0 and s == 3 and e == 2:
        return o3
    elif x == 0 and s == 4 and e == 1:
        return o4
    else:
        return polluted


''' h
board_matrix[row][col]
board_matrix[row][col+1]
board_matrix[row][col+2]
board_matrix[row][col+3]
board_matrix[row][col+4]
'''
def horizontal(board_matrix,pos):
    row, col = pos[0], pos[1]
    sum = 0
    for i in range(-4,5):
        x, s, e = 0, 0, 0  # me,op,emp counter
        # First stone
        try:first = board_matrix[row][col + i + 0]
        except:first = -1
        if first == "x":  x+=1
        elif first == "s":s+=1
        elif first == 0:  e+=1
        # Second stone
        try: second = board_matrix[row][col + i + 1]
        except:second = -1
        if second == "x":  x+=1
        elif second == "s":s+=1
        elif second == 0:  e+=1
        # Third stone
        try: third = board_matrix[row][col + i + 2]
        except:third = -1
        if third == "x":  x+=1
        elif third == "s":s+=1
        elif third == 0:  e+=1
        # Fourth stone
        try: fourth = board_matrix[row][col + i + 3]
        except:fourth = -1
        if fourth == "x":  x+=1
        elif fourth == "s":s+=1
        elif fourth == 0:  e+=1
        # Fifth stone
        try: fifth = board_matrix[row][col + i + 4]
        except:fifth = -1
        if fifth == "x":  x+=1
        elif fifth == "s":s+=1
        elif fifth == 0:  e+=1
        sum += score(x,s,e)
        print("ok")
    return sum                   # not finished yet 

def vertical(board_matrix,pos):
	pass

def diagonal1(board_matrix,pos):
	pass

def diagonal2(board_matrix,pos):
	pass

def main():
    board_matrix, weight_matrix = gen_board(board_size)
    pos = lambda row, col: [row, col]  # human indexing
    move(board_matrix,"x",pos(4,4))
    show_board(board_matrix)
    print(horizontal(board_matrix,pos(4,2))) # for testing

    #TODO: training process
main()


class GeneticAgent:
    def __init__(self):
        pass

    def corssover(self):
        pass

    def mutation(self):
        pass

    def fitness(self):
        pass

