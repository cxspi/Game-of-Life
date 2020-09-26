'''
This is our main driver file. It'll be responsible for displaying the Current Game state, and execution of the game.
'''
import sys
import pygame as pg
import golengine

WIDTH = HEIGHT = 1024
DIMENSION = 64 # Please choose powers of 2 (or change the WIDTH and HEIGHT)
SQ_SIZE = WIDTH/DIMENSION
MAX_FPS = 15

WHITE = (255,255,255)
BLACK = (0,0,0)


def main():
	pg.init()
	screen = pg.display.set_mode((WIDTH, HEIGHT))
	gs = golengine.GameState(nrows=DIMENSION)
	Cell = golengine.Cell()
	clock = pg.time.Clock()
	running = True
	while running:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				running == False
				pg.quit()
				quit()

		drawUpdate(screen, gs, pg)
		yet_to_be(gs, screen) # Runs only once. At beginning we only want to choose white squares once!
		Cell.nchecker(gs.board)
		Cell.god(gs.board)
		gs.update(Cell.cells)
		drawUpdate(screen, gs, pg)
		clock.tick(MAX_FPS)


@golengine.RunOnce
def yet_to_be(gs, screen):
	run = True
	print('Press \'z\' to start game')
	while run:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				run = False
				pg.quit()
				sys.exit()
			elif event.type == pg.MOUSEBUTTONDOWN:
				location = pg.mouse.get_pos() # x, y pos location of the mouse
				col = int(location[0]//SQ_SIZE)
				row = int(location[1]//SQ_SIZE)
				print(col, row)
				gs.set_white((col, row))
				drawUpdate(screen, gs, pg)
			elif event.type == pg.KEYDOWN:
				if event.key == pg.K_z:
					print('Worked!')
					run = False

def drawUpdate(screen, gs, pygame): # Combines the update screen function and redrawing it.
	draw_game(screen, gs)
	pygame.display.update()

def draw_game(screen, gs): # Draws onto the screen
	draw_squares(screen, gs)
	draw_lines(screen)

def draw_squares(screen, gs): # Draws squares on the screen(black = dead, white = alive)
	for r in range(DIMENSION):
		for c in range(DIMENSION):
			if gs.board[r][c] == 1: # Checks the state of the cell
				pg.draw.rect(screen, WHITE, pg.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
			else:
				pg.draw.rect(screen, BLACK, pg.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def draw_lines(screen):
	for c in range(1, DIMENSION):
		pg.draw.line(screen, WHITE, (c*SQ_SIZE, 0), (c*SQ_SIZE, WIDTH))
	for r in range(1, DIMENSION):
		pg.draw.line(screen, WHITE, (0, r*SQ_SIZE), (HEIGHT, r*SQ_SIZE))



if __name__ == "__main__":
	main()