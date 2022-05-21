import numpy as np
import matplotlib.pyplot as plt
import os
plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams.update({'font.size': 18})
plt.rcParams.update({'font.family': 'serif',"font.serif" : "Times New Roman", 
                    "text.usetex": True})


data = np.loadtxt('data.dat')

N = data[:,0]
to_plot = data[:,1:]

colors = ['dodgerblue','mediumpurple','brown','red', 'cyan', 'gold','green',
        'orange', 'purple', 'steelblue', 'grey']
labels = ['C','Fortran','Rust','Java', 'Go', 'Python*', 'Julia', 'JavaScript',
         'C\#', 'Python', 'R']

fig = plt.figure(figsize = (6,6))
ax = plt.gca()

for i, dat in enumerate(to_plot.T):
    plt.plot(N,dat, marker = 'o', markeredgecolor = 'k', color = colors[i], 
        label = labels[i], markersize = 7)
plt.plot(N,N**2/10000,  marker = 'o', ls = '--', markeredgecolor = 'k', 
        color = 'palegreen', alpha= 0.5, label = '$\mathcal{O}$($N^2$)',
        markersize = 7)
ax.set_yscale('log')
#ax.set_xscale('log')
ax.set_xlabel('Grid Size ($\\times$ $10^3$)')
ax.set_ylabel('Time (10 Iterations)')
ax.set_yticks([0.01,1,60,120,300,600,1800,3600,10800])
ax.set_yticklabels(['0.01 s','1 s','1 min','2 min', '5 min','10 min',
                '30 min','1 hr','3 hr'])
ax.set_xticks([100,2100,4100,6100,8100,10100,12100,14100])
ax.set_xticklabels(['$0.1$','$2.1$','$4.1$','$6.1$',
                '$8.1$','$10.1$','$12.1$','$14.1$'])
plt.minorticks_off()
plt.legend(ncol=1, bbox_to_anchor = [1.0, 1.03])
plt.grid()
plt.xticks(rotation = 45)
plt.ylim()
plt.savefig('./images/programs.png', dpi = 120, bbox_inches='tight')