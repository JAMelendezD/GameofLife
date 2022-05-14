import numpy as np
import matplotlib.pyplot as plt
import argparse
import multiprocessing
from functools import partial
from tqdm import tqdm

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
	parser = argparse.ArgumentParser(description='Game of Life')
	parser.add_argument('r',type=int,help='number of rows')
	parser.add_argument('c',type=int,help='number of columns')
	parser.add_argument('f',type=int,help='number of frames')
	args = parser.parse_args()
	main()