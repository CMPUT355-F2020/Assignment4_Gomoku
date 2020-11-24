# We found the base for this code online (URL is below)
# https://www.geeksforgeeks.org/search-a-word-in-a-2d-grid-of-characters/
# Note however, that we changed the code quite a bit to fit our needs

# This program searches for a given chain in the board

class Pattern: 
	
	def __init__(self): 
		self.R = None
		self.C = None
		self.dir = [[-1, 0],   # upwards vertically
		            [1, 0],    # downwards vertically 
		            [1, 1],    # downwards diagonally to the right
		            [1, -1],   # downwards diagonally to the left
		            [-1, -1],  # upwards diagonally to the left
		            [-1, 1],   # upwards diagonally to the right
		            [0, 1],    # left horizontally 
		            [0, -1]]   # right horizontally 		
		
		
	# the search function searches all 8 directions for a chain in the board at location (row, col)  
	def search(self, board, row, col, chain, full_search): 
		number_chains = 0
		direction_x = 2
		direction_y = 2
		found = False 
		direction = [0,0]
		# if first character doesn't match, stop
		if board[row][col] != chain[0]: 
			return 2, 2, False, 0
			#return direction_x, direction_y, found, number_chains
			
		# search all 8 directions 
		for x, y in self.dir: 
			
			row_next, col_next = row + x, col + y 
			flag = True
			
			# first character checked, match rest of chain 
			for k in range(1, len(chain)): 
				
				if (0 <= row_next < self.R and 0 <= col_next < self.C and chain[k] == board[row_next][col_next]): 
					# move in particular direction 
					row_next += x 
					col_next += y 
				else: 
					# if out of bound or no match found, break
					flag = False
					break
			
			if flag: 
				if full_search == False: return x, y, True, 1
				
				flag = False 
				found = True 
				direction_x = x
				direction_y = y 
				number_chains += 1
				
		return direction_x, direction_y, found, number_chains
	
	
	# patternSearch function searches for the first instance of the chain in the entire board	
	def patternSearch(self, board, chain, search_full_board): 
		
		self.R = len(board) 
		self.C = len(board[0]) 
		
		# iterate through the board until we find the first instance of the chain 
		if not search_full_board:
			for row in range(self.R): 
				for col in range(self.C): 
					x_dir, y_dir, found, num_chains = self.search(board, row, col, chain, search_full_board)
					if found: 
						chain_locations = [[row,col]]
						for _ in range(len(chain)-1):
							row += x_dir
							col += y_dir
							chain_locations.append([row,col])
						return chain_locations, True, 0
			return [], False, 0
		
		# iterate through every cell in board to search for all instances of the chain 
		else:
			counter = 0
			for row in range(self.R): 
				for col in range(self.C): 
					x_dir, y_dir, found, num_chains = self.search(board, row, col, chain, search_full_board)
					if found: counter += num_chains
			return [], counter>0, counter//2 		