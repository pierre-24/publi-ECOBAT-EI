import pandas
import matplotlib.pyplot as plt
import numpy
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('distances', nargs='*', type=int)
parser.add_argument('-o', '--output', default='Data_EC.pdf')
parser.add_argument('--show', action='store_true')

args = parser.parse_args()

figure = plt.figure(figsize=(8, 12))
axes = figure.subplots(3)

cmap = plt.colormaps['viridis']
colors = cmap(numpy.linspace(0, 1, len(args.distances)))

for i, dx in enumerate(args.distances):
    data_pot = pandas.read_csv('../data/work_function_conv/Ca_d_{}_potential.csv'.format(dx), names=['d', 'pot'], sep='\t')
    
    d = data_pot['d']
    axes[0].plot(d[d < 15], data_pot['pot'][d < 15], color=colors[i], label='d={} Å'.format(dx)) 
    axes[0].plot(d[d > d.max() - 15] - d.max(), data_pot['pot'][d > d.max() - 15], color=colors[i]) 
    
    data_chg = pandas.read_csv('../data/work_function_conv/Ca_d_{}_chg.csv'.format(dx), names=['d', 'chg', 'chgx', 'ichgx'], sep='\t')
    
    d = data_pot['d']
    axes[1].semilogy(d[d < 15], data_chg['chgx'][d < 15], color=colors[i]) 
    axes[1].semilogy(d[d > d.max() - 15] - d.max(), data_chg['chgx'][d > d.max() - 15], color=colors[i]) 

axes[0].set_ylabel('$E_\\infty$ (V)')
axes[0].set_xlabel('Distance from center (Å)')
axes[1].set_ylabel('Mean $\\rho(r)$ (e Å$^{-1}$)')
axes[1].set_xlabel('Distance from center (Å)')

axes[0].legend(ncol=4)

wfs = [
  1.864,
  1.860,
  1.866,
  1.873,
  1.498,
  1.501,
  1.501,
  1.501,
  1.501,
  1.501,
  1.501,
  1.501,
  1.501,
  1.501
]

axes[2].plot(args.distances, wfs, 'o-')
axes[2].set_xlabel('Interslab distance, $d$ (Å)')
axes[2].set_ylabel('$\\Phi$ (V)')

plt.tight_layout()
figure.savefig(args.output, dpi=300)

if args.show:
    plt.show()
