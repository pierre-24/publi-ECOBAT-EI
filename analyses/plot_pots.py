import pandas
import matplotlib.pyplot as plt
import numpy
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('distances', nargs='*', type=int)
parser.add_argument('-o', '--output', default='Data_EC.pdf')
parser.add_argument('--show', action='store_true')

args = parser.parse_args()

figure = plt.figure(figsize=(8, 8))
axes = figure.subplots(2, sharex=True)

cmap = plt.colormaps['viridis']
colors = cmap(numpy.linspace(0, 1, len(args.distances)))

SMAX = 65.45/2

for i, dx in enumerate(args.distances):
    data_pot = pandas.read_csv('../data/work_function_conv/Ca_d_{}_potential.csv'.format(dx), names=['d', 'pot'], sep='\t')
    
    d = data_pot['d']
    axes[0].plot(d[d < SMAX], data_pot['pot'][d < SMAX], color=colors[i], label='d={} Å'.format(dx)) 
    axes[0].plot(d[d > d.max() - SMAX] - d.max(), data_pot['pot'][d > d.max() - SMAX], color=colors[i]) 
    
    data_chg = pandas.read_csv('../data/work_function_conv/Ca_d_{}_chg.csv'.format(dx), names=['d', 'chg', 'chgx', 'ichgx'], sep='\t')
    
    d = data_pot['d']
    axes[1].semilogy(d[d < SMAX], data_chg['chgx'][d < SMAX], color=colors[i]) 
    axes[1].semilogy(d[d > d.max() - SMAX] - d.max(), data_chg['chgx'][d > d.max() - SMAX], color=colors[i]) 

axes[0].set_ylabel('Mean $E_\\infty$(V)')
axes[1].set_ylabel('Mean $\\rho(r)$ (e Å$^{-1}$)')
axes[1].set_xlabel('Distance from center (Å)')

plt.tight_layout()
figure.savefig(args.output, dpi=300)

if args.show:
    plt.show()
