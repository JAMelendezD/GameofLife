import numpy as np
import matplotlib.pyplot as plt
import argparse
from numba import jit
import multiprocessing
from functools import partial
from tqdm import tqdm
import time

def init_world(mode,rows,cols,type):
	if mode == 0:
		if type == 'glider':
			world = np.zeros((rows,cols))
			world[2][1] = 1
			world[3][2] = 1
			world[1][3] = 1
			world[2][3] = 1
			world[3][3] = 1

	elif mode == 1:
		world = np.random.randint(0,2,(rows,cols))
	return world

@jit(nopython=True)
def update_world(world):
	old_world = np.copy(world)
	shape = np.shape(world)
	rows = shape[0]
	cols = shape[1] 
	for i in range(rows):
		for j in range(cols):
			state = old_world[i][j]
			neis = old_world[i%rows][(j+1)%cols]+old_world[i%rows][(j-1)%cols]\
				  +old_world[(i+1)%rows][j%cols]+old_world[(i-1)%rows][j%cols]\
				  +old_world[(i+1)%rows][(j+1)%cols]+old_world[(i-1)%rows][(j-1)%cols]\
				  +old_world[(i+1)%rows][(j-1)%cols]+old_world[(i-1)%rows][(j+1)%cols]

			if state == 1:
				if neis not in (2,3):
					world[i][j] = 0
			else:
				if neis == 3:
					world[i][j] = 1

def plot_world(min_frame,max_frame,rows,cols):
	for frame in tqdm(range(min_frame,max_frame),desc='Animation',colour='Green'):
		world = np.loadtxt(f'{frame:06d}.txt')

		max_ = max(cols,rows)

		if 1 <= max_ < 61:
			size = 12
		elif 61 <= max_ < 201:
			size = 30
		else:
			size = 80

		fig = plt.figure(figsize = (size,size))
		plt.pcolormesh(world,cmap='summer',edgecolors='k', linewidth=1)
		plt.gca().invert_yaxis()
		plt.gca().set_aspect('equal')
		plt.xticks([])
		plt.yticks([])
		plt.grid()
		plt.title(f'Iteration #{(frame):6d}')
		plt.savefig(f'{frame:06d}.png',bbox_inches='tight')
		plt.close()

def main():
	world = init_world(args.mode,args.r,args.c,args.type)
	
	print('Started simulation')
	start = time.time()
	for i in range(args.f+1):
		np.savetxt(f'{i:06d}.txt', world, fmt='%d')
		update_world(world)
	print(f'Finished simulation in: {time.time()-start:6.2f} seconds')
	
	cores = multiprocessing.cpu_count()
	divide_conquer = int(np.ceil((args.f+1)/cores))
	pool = multiprocessing.Pool(cores)
	min_frames = []
	max_frames = []
	for i in range(cores):
		min_frames.append(i*divide_conquer)
		if i == cores-1:
			max_frames.append(args.f+1)
		else:
			max_frames.append((i+1)*divide_conquer)
	
	partial_plot=partial(plot_world, rows=args.r,cols=args.c)
	pool.starmap(partial_plot,zip(min_frames,max_frames))

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Dynamics')
	parser.add_argument('mode',type=int,help='mode 0  predifined, 1 random')
	parser.add_argument('--r',default=10,type=int,help='number of rows')
	parser.add_argument('--c',default=10,type=int,help='number of columns')
	parser.add_argument('--f',default=100,type=int,help='number of frames')
	parser.add_argument('--type',default='glider',type=str,help='predifined type')
	args = parser.parse_args()
	main()