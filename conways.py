# ---------------------------------------------------------------------------------------
# conways.py : Conways game of life in python (7 min 50 sec) with numba and numpy (19.76)
# ---------------------------------------------------------------------------------------

import numpy as np
import argparse
from numba import jit
import time

@jit(nopython=True)
def update_world(world):

	old_world = np.copy(world)
	shape = np.shape(world)
	rows = shape[0]
	cols = shape[1]

	for i in range(rows):
		for j in range(cols):
			state = old_world[i][j]
			neis = old_world[i%rows][(j+1)%cols]\
				  +old_world[i%rows][(j-1)%cols]\
				  +old_world[(i+1)%rows][j%cols]\
				  +old_world[(i-1)%rows][j%cols]\
				  +old_world[(i+1)%rows][(j+1)%cols]\
				  +old_world[(i-1)%rows][(j-1)%cols]\
				  +old_world[(i+1)%rows][(j-1)%cols]\
				  +old_world[(i-1)%rows][(j+1)%cols]		

			if state == 1:									# Kill if alive and nei !2 or !3
				if (neis != 2) and neis != 3:
					world[i][j] = 0
			else:
				if neis == 3:								# Alive if death and nei 3
					world[i][j] = 1
															# otherwise stay dead or alive
def main():

	world = np.random.randint(0,2,(args.r,args.c))			# Initialize random world

	print('Started simulation')
	start = time.time()
	for i in range(args.f+1):
		np.savetxt(f'{i:06d}.txt', world, fmt='%d')			# Save world to a text file
		update_world(world)
	print(f'Finished simulation in: {time.time()-start:6.2f} seconds')

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Game of Life')
	parser.add_argument('r',type=int,help='number of rows')
	parser.add_argument('c',type=int,help='number of columns')
	parser.add_argument('f',type=int,help='number of frames')
	args = parser.parse_args()
	main()
