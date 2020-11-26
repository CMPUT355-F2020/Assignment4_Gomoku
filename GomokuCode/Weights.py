class Weights:# To be trained
    def __init__(self):
        # for playing
        self.w_1 = 6  # length 3 with 1 open end 
        self.w_2 = 100 # length 3 with 2 open ends
        self.w_3 = 10  # length 2 with 1 open end
        self.w_4 = 50  # length 2 with 2 open ends---->attack
        self.w_5 = 1  # length 1 with 1 open end
        self.w_6 = 2  # length 1 with 2 open ends

        # for training
        self.fitness = 0 # evaluation
        self.win = 0 # number of winning games