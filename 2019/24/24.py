from collections import defaultdict


def parse_file(file):
    grid = {}
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            for x, c in enumerate(line.strip()):
                grid[x, y] = c
    return grid


def neighbours(point, recurse=False):
    x, y = point
    ns = {
        (x + 1, y, 0),
        (x - 1, y, 0),
        (x, y + 1, 0),
        (x, y - 1, 0),
    }
    if not recurse:
        return ns
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

def hash(grid):
    points = []
    for x in range(5):
        for y in range(5):
            points.append(grid[x, y])
    return ''.join(points)


def new_value(value, bugs):
    if value == '.' and bugs in [1, 2]:
        return '#'

    if value == '#' and bugs == 1:
        return '#'

    return '.'


def iterate_single(grid):
    new = {}
    for point, value in grid.items():
        bugs = sum(
            1 for x, y, _ in neighbours(point)
            if grid.get((x, y), '.') == '#'
        )
        new[point] = new_value(value, bugs)
    return new


def iterate_multiple(grids):
    new = defaultdict(dict)
    for level, grid in grids.items():
        for point, value in grid.items():
            if point == (2, 2):
                new[level][point] = '?'
                continue
            bugs = sum(
                1 for x, y, n_level in neighbours(point, True)
                if grids.get(level + n_level, {}).get((x, y), '.') == '#'
            )
            new[level][point] = new_value(value, bugs)
    return new


def first_repeating(grid):
    seen = set()
    while True:
        grid = iterate_single(grid)
        h = hash(grid)
        if h in seen:
            return grid
        seen.add(h)


def biodiversity(grid):
    multiplier = 1
    value = 0
    for y in range(5):
        for x in range(5):
            if grid[x, y] == '#':
                value += multiplier
            multiplier *= 2
    return value


def count_bugs(grids):
    bugs = 0
    for grid in grids.values():
        for value in grid.values():
            if value == '#':
                bugs += 1
    return bugs


def part_one():
    grid = parse_file('input.map')
    grid = first_repeating(grid)
    return biodiversity(grid)


def part_two():
    grid = parse_file('input2.map')
    grids = {}
    for level in range(-200, 201):
        grids[level] = {point: '.' for point in grid.keys()}
    grids[0] = grid

    for i in range(200):
        grids = iterate_multiple(grids)

    return count_bugs(grids)


print('Part 1:', part_one())
print('Part 2:', part_two())
