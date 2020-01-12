from collections import defaultdict


def parse(file):
    grid = defaultdict(set)
    with open(file) as f:
        for i, line in enumerate(f.readlines()):
            p = line.strip().replace('<', ' ').replace('>', '').split()
            x = int(p[1][:-1])
            y = int(p[2])
            dx = int(p[4][:-1])
            dy = int(p[5])
            grid[x, y].add((dx, dy))
    return grid

def draw(g):
    min_y = min(y for (x, y) in g.keys())
    min_x = min(x for (x, y) in g.keys())
    max_x = max(x for (x, y) in g.keys())
    max_y = max(y for (x, y) in g.keys())
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if g.get((x, y), '.') == '.':
                print(' ', end='')
            else:
                print('#', end='')
        print()

def area(g):
    min_y = min(y for (x, y) in g.keys())
    min_x = min(x for (x, y) in g.keys())
    max_x = max(x for (x, y) in g.keys())
    max_y = max(y for (x, y) in g.keys())
    return abs(max_x - min_x) * abs(max_y - min_y)

def iterate(g):
    n = defaultdict(set)
    for (x, y), s in g.items():
        for dx, dy in s:
            n[x + dx, y + dy].add((dx, dy))
    return n


grid = parse('input')

size = area(grid)
i = 0
while True:
    next_grid = iterate(grid)
    next_size = area(next_grid)
    if size < next_size:
        print('Part 1:', i)
        print('Part 2:')
        draw(grid)
        break
    grid = next_grid
    size = next_size
    i += 1
