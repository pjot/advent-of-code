from collections import defaultdict


def parse(file):
    grid = defaultdict(set)
    with open(file) as f:
        for line in f.readlines():
            p = line.strip().split(' ')
            x0, y0 = map(int, p[2][:-1].split(','))
            dx, dy = map(int, p[3].split('x'))
            for x in range(x0, x0 + dx):
                for y in range(y0, y0 + dy):
                    grid[x, y].add(p[0])
    return grid


g = parse('input')
print('Part 1:', sum(1 for v in g.values() if len(v) > 1))

def is_unique(k, values):
    for v in values:
        if k in v and len(v) > 1:
            return False
    return True

values = g.values()
options = set()
for vs in values:
    options |= vs

for v in options:
    if is_unique(v, values):
        print('Part 2:', v)
        break