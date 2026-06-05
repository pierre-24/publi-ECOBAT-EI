import sys

symbols = []

with open(sys.argv[1]) as f:
    lines = f.readlines()
    for line in lines[1:]:
        chunks = line.split()
        symbols.append(chunks[0])

fragments = {}

with open(sys.argv[2]) as f:
    for line in f.readlines():
        chunks = line.split()
        name = chunks[0]
        indices = [int(i) for i in chunks[1:]]
        
        fragments[name] = indices

charges = []

with open(sys.argv[3]) as f:
    lines = f.readlines()
    for line in lines[2:-4]:
        chunks = line.split()
        charges.append(float(chunks[4]))

VALZ = {'C': 4., 'O': 6., 'H': 1., 'Ca': 10.}

for name, indices in fragments.items():
    total_charge = .0
    for i in indices:
        total_charge +=  VALZ[symbols[i]] - charges[i - 1]
    
    print('{} {: .3f}'.format(name, total_charge))
