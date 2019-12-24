from collections import defaultdict


def parse_file(file):
    grid = {}
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            for x, c in enumerate(line.strip()):
                grid[x, y] = c
    return grid


def draw(grid):
    for y in range(5):
        for x in range(5):
            print(grid[x, y], end='')
        print()
    print()


def neighbours(point):
    x, y = point
    ns = {
        (x + 1, y, 0),
        (x - 1, y, 0),
        (x, y + 1, 0),
        (x, y - 1, 0),
    }
    ns.discard((2, 2, 0))
    if x == 0:
        ns.add((1, 2, 1))
    if y == 0:
        ns.add((2, 1, 1))
    if y == 4:
        ns.add((2, 3, 1))
    if x == 4:
        ns.add((3, 2, 1))
    if point == (1, 2):
        for y in range(5):
            ns.add((0, y, -1))
    if point == (2, 1):
        for x in range(5):
            ns.add((x, 0, -1))
    if point == (3, 2):
        for y in range(5):
            ns.add((4, y, -1))
    if point == (2, 3):
        for x in range(5):
            ns.add((x, 4, -1))
    return ns


def iterate(grids):
    new = defaultdict(dict)
    for level, grid in grids.items():
        for point, value in grid.items():
            if point == (2, 2):
                new[level][point] = '?'
                continue
            bugs = sum(
                1 for x, y, n_level in neighbours(point)
                if grids.get(level + n_level, {}).get((x, y), '.') == '#'
            )
            if value == '.':
                if bugs in [1, 2]:
                    new[level][point] = '#'
                else:
                    new[level][point] = '.'

            if value == '#':
                if bugs == 1:
                    new[level][point] = '#'
                else:
                    new[level][point] = '.'
    return new


def count_bugs(grids):
    bugs = 0
    for grid in grids.values():
        for value in grid.values():
            if value == '#':
                bugs += 1
    return bugs


grid = parse_file('input2.map')
grids = {}
for level in range(-200, 201):
    grids[level] = {point: '.' for point in grid.keys()}
grids[0] = grid

for i in range(200):
    grids = iterate(grids)

print("Part 2:", count_bugs(grids))
