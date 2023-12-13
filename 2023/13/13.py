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

def value(grid, p, flip):
    v = 1 if grid[p] == "#" else -1
    if p == flip:
        v *= -1
    return v

def reflection_points(lines):
    for p, _ in enumerate(lines):
        if p == 0:
            continue
        if is_reflection(lines, p):
            yield p

def reflections(grid, flip=None):
    res, xs, ys = set(), set(), set()

    for x, y in grid.keys():
        xs.add(x)
        ys.add(y)
    xs = sorted(list(xs))
    ys = sorted(list(ys))

    rows = []
    for y in ys:
        rows.append([
            value(grid, (x, y), flip)
            for x in xs
        ])

    for r in reflection_points(rows):
        res.add(r * 100)

    cols = []
    for x in xs:
        cols.append([
            value(grid, (x, y), flip)
            for y in ys
        ])

    for r in reflection_points(cols):
        res.add(r)

    return res

def with_replacement(grid):
    old = reflections(grid)

    for flip in grid.keys():
        new = reflections(grid, flip)
        if new - old:
            return (new - old).pop()

grids = parse("input")

one = two = 0
for g in grids:
    one += reflections(g).pop()
    two += with_replacement(g)

print("Part 1:", one)
print("Part 2:", two)


