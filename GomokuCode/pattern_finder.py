# This program searches for a given chain in a 2D grid 

# We do not take credit for this code, but we have adapted it to fit our needs
# Found this code on this website: https://www.geeksforgeeks.org/search-a-word-in-a-2d-grid-of-characters/

class GFG: 
	
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
		
	# This function searches in all 8-direction from point(row, col) in grid[][] 
	def search2D(self, grid, row, col, word): 
		
		direction = [0,0]
		
		# If first character of word doesn't match with the given starting point in grid. 
		if grid[row][col] != word[0]: return 2, 2, False
			
		# Search word in all 8 directions starting from (row, col) 
		for x, y in self.dir: 
			
			# Initialize starting point for current direction 
			rd, cd = row + x, col + y 
			flag = True
			
			# First character is already checked, match remaining characters 
			for k in range(1, len(word)): 
				
				# If out of bound or not matched, break 
				if (0 <= rd <self.R and 0 <= cd < self.C and word[k] == grid[rd][cd]): 
					
					# Moving in particular direction 
					rd += x 
					cd += y 
				else: 
					flag = False
					break
			
			# If all character matched, then value of flag must be false		 
			if flag: 
				return x, y, True
		return 2, 2, False
		
		
	# Searches given word in a given matrix in all 8 directions	
	
	### Add a flag to know if it should return or check the entire board 
	### Should return number of pattern matches found 0, 1 ... 
	def patternSearch(self, grid, word): 
		
		# Rows and columns in given grid 
		self.R = len(grid) 
		self.C = len(grid[0]) 
		
		# Consider every point as starting point and search given word 
		for row in range(self.R): 
			for col in range(self.C): 
				x_dir, y_dir, found = self.search2D(grid, row, col, word)
				if found: 
					#print("pattern found at " + str(row) + ', ' + str(col)) 
					chain_locations = [[row,col]]
					for i in range(4):
						row += x_dir
						col += y_dir
						chain_locations.append([row,col])
					#print(str(chain_locations))	
					#print("direction is " + str(x_dir) + ', ' + str(y_dir)) 
					return chain_locations, True
		return [], False 