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
    return [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]


def hash(grid):
    points = []
    for x in range(5):
        for y in range(5):
            points.append(grid[x, y])
    return ''.join(points)


def iterate(grid):
    new = {}
    for point, value in grid.items():
        bugs = sum(
            1 for n in neighbours(point)
            if grid.get(n, '.') == '#'
        )
        if value == '.':
            if bugs in [1, 2]:
                new[point] = '#'
            else:
                new[point] = '.'

        if value == '#':
            if bugs == 1:
                new[point] = '#'
            else:
                new[point] = '.'
    return new


def first_repeating(grid):
    seen = set()
    while True:
        grid = iterate(grid)
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


grid = parse_file('input.map')
draw(grid)

grid = first_repeating(grid)
draw(grid)

print("Part 1:", biodiversity(grid))