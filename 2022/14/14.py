import itertools

def sign(n):
    if n == 0:
        return 0
    return abs(n) // n

def delta(a, b):
    x1, y1 = a
    x2, y2 = b
    return sign(x2 - x1), sign(y2 - y1)

def add(a, b):
    ax, ay = a
    bx, by = b
    return ax + bx, ay + by

def points_between(a, b):
    d = delta(a, b)
    yield a
    while a != b:
        a = add(a, d)
        yield a

def parse(file):
    grid = {}
    with open(file) as f:
        for line in f.readlines():
            line = line.strip()
            moves = line.split(" -> ")
            scan = []
            for move in moves:
                x, y = move.split(",")
                scan.append((int(x), int(y)))
            for a, b in itertools.pairwise(scan):
                for p in points_between(a, b):
                    grid[p] = "#"
    grid[500, 0] = "+"
    return grid

def y_range(grid):
    ys = ([p[1] for p in grid.keys()])
    return min(ys), max(ys)

def is_air(grid, point):
    return grid.get(point, ".") == "."

def is_sand(grid, point):
    return grid.get(point, ".") == "o"

def drop_sand(grid):
    sand = (500, 0)
    _, limit = y_range(grid)

    while True:
        b = add(sand, (0, 1))
        dl = add(sand, (-1, 1))
        dr = add(sand, (1, 1))

        if is_air(grid, b):
            sand = b

        elif is_air(grid, dl):
            sand = dl

        elif is_air(grid, dr):
            sand = dr

        elif is_sand(grid, sand):
            return grid, True

        else:
            grid[sand] = "o"
            return grid, False

        if sand[1] > limit + 3:
            return grid, True

def one(grid):
    done = False
    while not done:
        grid, done = drop_sand(grid)

    return len([p for p in grid.values() if p == "o"])

def add_floor(grid):
    min_y, max_y = y_range(grid)
    height = max_y - min_y
    min_x = 500 - height - 3
    max_x = 500 + height + 4
    for x in range(min_x, max_x):
        grid[x, max_y + 2] = "#"
    return grid

def two(grid):
    grid = add_floor(grid)
    return one(grid)

print("Part 1:", one(parse("input.txt")))
print("Part 2:", two(parse("input.txt")))

