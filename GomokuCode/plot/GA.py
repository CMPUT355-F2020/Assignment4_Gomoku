from Weights import Weights
import random
brains = []
for _ in range(10):
    w = Weights()
    w.w_1 = random.randint(0, 9)
    w.w_2 = random.randint(0, 9)
    w.w_3 = random.randint(0, 9)
    w.w_4 = random.randint(0, 9)
    w.w_5 = random.randint(0, 9)
    w.w_6 = random.randint(0, 9)
    brains.append(w)

def corssover(self):
    pass

def mutation(self):
    pass

def fitness(self):
    pass