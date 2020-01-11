from collections import defaultdict


def parse(file):
    nodes = {}
    with open(file) as f:
        for i, line in enumerate(f.readlines()):
            x, y = map(int, line.strip().split(', '))
            nodes[x, y] = i
    return nodes

def distance(f, t):
    x0, y0 = f
    x1, y1 = t
    return abs(x0-x1) + abs(y0-y1)

def build_grid(nodes):
    grid = {}
    max_x = max(map(lambda p: p[0], nodes.keys()))
    max_y = max(map(lambda p: p[1], nodes.keys()))
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            per_distance = defaultdict(set)
            for coord, n in nodes.items():
                per_distance[distance(coord, (x, y))].add(n)

            closest = per_distance[min(per_distance)]
            if len(closest) == 1:
                grid[x, y] = closest.pop()
            else:
                grid[x, y] = '.'
    return grid, max_x, max_y


def along_edges(grid, max_x, max_y):
    along = set()
    for x in range(max_x):
        along.add(grid.get((x, 0), '.'))
        along.add(grid.get((x, max_y), '.'))

    for y in range(max_y):
        along.add(grid.get((0, y), '.'))
        along.add(grid.get((max_x, y), '.'))
    return along

nodes = parse('input')

grid, max_x, max_y = build_grid(nodes)
edges = along_edges(grid, max_x, max_y)
found = defaultdict(int)
for v in grid.values():
    if v not in edges:
        found[v] += 1

print('Part 1:', max(found.values()))

in_region = 0
for x in range(max_x):
    for y in range(max_y):
        total = sum(distance(n, (x, y)) for n in nodes)
        if total < 10000:
            in_region += 1

print('Part 2:', in_region)