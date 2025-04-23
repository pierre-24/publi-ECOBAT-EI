import pandas
import matplotlib.pyplot as plt
import numpy
import argparse
from scipy.optimize import curve_fit

def prepare_data(data: pandas.DataFrame):
    return data
    
def f(x, a, b, c, d):
    return a*x**3 + b*x**2+ c*x + d

def plot_F(ax, data, left_limit: int = -2, name: str = ''):
    pl = ax.plot(data['Potential vs ref [V]'], data['F [eV]'], 's', label=name)
    
    subdata = data[data['Potential vs ref [V]'] > left_limit]
    popt, pcov = curve_fit(f, subdata['Potential vs ref [V]'], subdata['F [eV]'])
    x = numpy.linspace(data['Potential vs ref [V]'].min() - 1, data['Potential vs ref [V]'].max() + .25, 200)
    ax.plot(x, f(x, *popt), '--', color=pl[0].get_c())
    
def lin(x, a, b):
    return a*x + b
        
def plot_q(ax, data, zc=1200, left_limit: int = -2):
    pl = ax.plot(data['Potential vs ref [V]'], data['Charge on slab [e]'] - zc, 's')
    
    subdata = data[data['Potential vs ref [V]'] > left_limit]
    popt, pcov = curve_fit(lin, subdata['Potential vs ref [V]'], subdata['Charge on slab [e]'] - zc)
    x = numpy.linspace(data['Potential vs ref [V]'].min() - 1, data['Potential vs ref [V]'].max() + .25, 200)
    ax.plot(x, lin(x, *popt), '--', color=pl[0].get_c())

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
parser.add_argument('--szc', type=int, required=True)
parser.add_argument('-L', '--left-limit', type=float, default=-2.5)

args = parser.parse_args()

if len(args.inputs) != len(args.names):
    raise Exception('inputs and names should have the same size')

figure = plt.figure(figsize=(6, 6))
axes = figure.subplots(2, sharex=True)

for inp, name in zip(args.inputs, args.names):
    data = prepare_data(pandas.read_csv(inp))

    plot_F(axes[0], data, left_limit=args.left_limit, name=name)
    plot_q(axes[1], data, zc=args.zc, left_limit=args.left_limit)

axes[0].set_xlim(*args.limits)
axes[0].set_ylabel('F (eV)')
axes[0].legend()

axes[1].set_xlabel('E$^0_{rel}$ (V vs SHE)')
axes[1].set_ylabel('N$_e$ in slab versus ZC')

plt.tight_layout()
figure.savefig(args.output, dpi=300)
