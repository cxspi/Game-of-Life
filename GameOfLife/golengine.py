'''
This is our game engine. It is responsible for determining for storing all the information about the current state of the game.
And setting the rules the game must follow.
'''
import numpy

class GameState():
	# Creating the board of the game
	def __init__(self, nrows=10):
		self.board = [[0 for n in range(nrows)] for x in range(nrows)]

	def set_white(self, mouse_pos): # At the beginning set black cells to white
		self.board[mouse_pos[1]][mouse_pos[0]] = 1
		
	def update(self, source): # Source is a dictionary which contains the state of the cell and the amount of neighbours
		for r in range(len(self.board)):
			for c in range(len(self.board)):
				self.board[r][c] = source[(r,c)][1]


class RunOnce(object):  # At beginning we only want to choose white squares once!
    def __init__(self, func):
        self.func = func
        self.ran = False

    def __call__(self, gs, screen):
        if not self.ran:
            self.func(gs, screen) 
            self.ran = True


class Cell():
	def __init__(self):
		# Cells is adictionary with all items inside the board with value of their dead neighbours.
		self.cells =  {}



	def nchecker(self, board): # Checks for the amout of living neighbours around a cell 
		for r in range(len(board)):
			for c in range(len(board)):
				self.cells[(r,c)] = [0, board[r][c]]
				try:
					if board[r-1][c-1] == 1:
						self.cells[(r,c)][0] += 1
				except:
					pass
				try:
					if board[r][c-1] == 1:
						self.cells[r,c][0] += 1
				except:
					pass
				try:
					if board[r+1][c-1] == 1:
						self.cells[r,c][0] += 1
				except:
					pass
				try:
					if board[r-1][c] == 1:
						self.cells[r,c][0] += 1
				except:
					pass
				try:
					if board[r+1][c] == 1:
						self.cells[r,c][0] += 1
				except:
					pass
				try:
					if board[r-1][c+1] == 1:
						self.cells[r,c][0] += 1
				except:
					pass
				try:
					if board[r][c+1] == 1:
						self.cells[r,c][0] += 1
				except:
					pass
				try:
					if board[r+1][c+1] == 1:
						self.cells[r,c][0] += 1
				except:
					pass
		
	def god(self, board): # If number of neighbours is eaquls to 3 revive dead cell
		for r in range(len(board)):
			for c in range(len(board)):
				if board[r][c] == 0 and self.cells[(r,c)][0] == 3:
					self.cells[(r,c)][1] = 1
				elif board[r][c] == 1 and self.cells[(r,c)][0] < 2 or self.cells[(r,c)][0] > 3:
					self.cells[(r,c)][1] = 0
				else:
					pass

	def kill(): # If number of neighbours is lower than 2 or higher than 3 (x != [2,3]) kills the cell
		pass


board = GameState()

papa = Cell()
x = 1
'''while True:
	papa.nchecker(board.board)
	papa.god(board.board)
	board.update(papa.cells)
	for r in range(len(board.board)):
		for c in range(len(board.board)):
			print(board.board[r][c] , papa.cells[(r,c)], x)
			x += 1

'''