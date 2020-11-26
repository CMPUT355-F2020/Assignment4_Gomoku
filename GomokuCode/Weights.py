class Weights:# To be trained
    def __init__(self):
        # for playing
        self.w_1 = 22.72 # length 3 with 1 open end 
        self.w_2 = 49.26 # length 3 with 2 open ends
        self.w_3 = 15.72 # length 2 with 1 open end
        self.w_4 = 26.64 # length 2 with 2 open ends---->attack
        self.w_5 = 4.49  # length 1 with 1 open end
        self.w_6 = 7.11  # length 1 with 2 open ends

        # for training
        self.fitness = 0 # evaluation
        self.win = 0 # number of winning games
        
