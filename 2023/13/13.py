def parse(file):
    grids = []
    with open(file) as f:
        for part in f.read().split("\n\n"):
            grid = {}
            for y, line in enumerate(part.splitlines()):
                for x, c in enumerate(line):
                    grid[x, y] = c
            grids.append(grid)
    return grids

def is_reflection(lines, p):
    first = list(reversed(lines[:p]))
    rest = lines[p:]
    for a, b in zip(first, rest):
        if a != b:
            return False
    return True

def value(grid, p, o):
    if grid[p] == "#":
        return "0" if p == o else "1"
    return "1" if p == o else "0"

def reflection_points(lines):
    for p in range(1, len(lines)):
        if is_reflection(lines, p):
            yield p

def reflections(grid, ox=-1, oy=-1):
    res = set()
    max_x = max([p[0] for p in grid.keys()]) + 1
    max_y = max([p[1] for p in grid.keys()]) + 1
    override = (ox, oy)

    rows = []
    for y in range(max_y):
        row = ""
        for x in range(max_x):
            row += value(grid, (x, y), override)
        rows.append(int(row, 2))

    for r in reflection_points(rows):
        res.add(r * 100)

    cols = []
    for x in range(max_x):
        col = ""
        for y in range(max_y):
            col += value(grid, (x, y), override)
        cols.append(int(col, 2))

    for r in reflection_points(cols):
        res.add(r)

    return res

def with_replacement(grid):
    r1 = reflections(grid)

    for x, y in grid.keys():
        r = reflections(grid, x, y)
        if r - r1:
            return (r - r1).pop()

grids = parse("input")

one = two = 0
for g in grids:
    one += reflections(g).pop()
    two += with_replacement(g)

print("Part 1:", one)
print("Part 2:", two)


