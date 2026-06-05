import pandas
import matplotlib.pyplot as plt
import numpy
import argparse
from scipy.optimize import curve_fit

def prepare_data(data: pandas.DataFrame):
    return data
        
def plot_q(ax, data, zc=1200, name: str = '', shift: int=0):
    pl = ax.plot(data['Potential vs ref [V]'], (zc - data['N_e [e]'] + data['Charge on slab [e]']) / 2, 's--', label=name, color='C{}'.format(shift))

def get_limits(inp: str):
    try:
        limits = [float(x) for x in inp.split(':')]
    except ValueError:
        raise argparse.ArgumentTypeError('`limits` must contain float')
    
    if len(limits) != 2:
        raise argparse.ArgumentTypeError('`limits` must contain 2 elements')
        
    return limits

parser = argparse.ArgumentParser()
parser.add_argument('inputs', nargs='*')
parser.add_argument('-n', '--names', nargs='*')
parser.add_argument('-l', '--limits', default='-4:0.5', type=get_limits)
parser.add_argument('-o', '--output', default='Data_EC.pdf')
parser.add_argument('--zc', type=int, required=True)

args = parser.parse_args()

if len(args.inputs) != len(args.names):
    raise Exception('inputs and names should have the same size')

figure = plt.figure(figsize=(7, 4))
ax = figure.subplots()

ax.hlines([0, 1, 2], *args.limits, color='cyan', ls='--')

i = 0
for inp, name in zip(args.inputs, args.names):
    data = prepare_data(pandas.read_csv(inp))
    plot_q(ax, data, zc=args.zc, name=name, shift=1+i)
    i += 1

ax.set_xlim(*args.limits)
ax.set_ylabel('F (eV)')
ax.legend(ncol=2)

ax.set_ylabel('$q${solvated species}')
ax.set_xlabel('E$^0_{rel}$ (V vs SHE)')

plt.tight_layout()
figure.savefig(args.output, dpi=300)
