def parse(file):
    mappings = {}
    with open(file) as f:
        state = f.readline().strip().split(' ')[2]
        f.readline()
        for line in f.readlines():
            f, t = line.strip().split(' => ')
            mappings[f] = t
    return state, mappings


def iterate(state, mappings):
    state = {
        i: s for i, s in enumerate(state)
    }
    n = ''
    for i in range(len(state) + 2):
        a = ''.join(
            state.get(l, '.') for l in range(i-2, i+3)
        )
        n += mappings.get(a, '.')
    
    return n.rstrip('.')


s, m = parse('input')
s = '......' + s
for i in range(20):
    s = iterate(s, m)

pots = 0
for i, c in enumerate(s):
    if c == '#':
        pots += i - 6

def part_two(x):
    return 7236 + (x - 108) * 67

print('Part 1:', pots)
print('Part 2:', part_two(50000000000))