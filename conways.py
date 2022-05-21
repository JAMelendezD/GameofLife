# ------------------------------------------------------------------------------
# conways.py : Conways game of life in python with numba and numpy (19.76)
# ------------------------------------------------------------------------------

import numpy as np
import argparse
from numba import jit
import time

@jit(nopython = True)
def update_world(rows, cols, world):

	old_world = np.copy(world)
	
	for i in range(rows):
		for j in range(cols):
			state = old_world[i][j]
			neis = old_world[i % rows][(j + 1) % cols]\
				  +old_world[i % rows][(j - 1) % cols]\
				  +old_world[(i + 1) % rows][j % cols]\
				  +old_world[(i - 1)%rows][j % cols]\
				  +old_world[(i + 1) % rows][(j + 1) % cols]\
				  +old_world[(i - 1) % rows][(j - 1) % cols]\
				  +old_world[(i + 1) % rows][(j - 1) % cols]\
				  +old_world[(i - 1) % rows][(j + 1) % cols]		

			if state == 1:									
				if (neis != 2 and neis != 3):
					world[i][j] = 0
			else:
				if neis == 3:								
					world[i][j] = 1

def main():

	rows = args.r
	cols = args.c
	frames = args.f
	world = np.random.randint(0, 2, (rows, cols))
	
	np.savetxt(f'{0:06d}.txt', world, fmt='%d')
	
	print('Started simulation')
	start = time.time()
	for i in range(1, frames + 1):
		update_world(rows, cols, world)
		np.savetxt(f'{i:06d}.txt', world, fmt='%d')
	print(f'Finished simulation in: {time.time() - start:6.2f} seconds')

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = 'Game of Life')
	parser.add_argument('r', type=int, help='number of rows')
	parser.add_argument('c', type=int, help='number of columns')
	parser.add_argument('f', type=int, help='number of frames')
	args = parser.parse_args()
	main()
