from collections import defaultdict

def parse(file):
    grid = {}
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            for x, c in enumerate(line.strip()):
                grid[x, y] = int(c)
    return grid

def neighbours(grid, x, y, d, imin, imax):
    ns = []
    if d == "|":
        l = 0
        for i in range(1, imin):
            l += grid.get((x + i, y), 0)
        for i in range(imin, imax + 1):
            l += grid.get((x + i, y), 0)
            ns.append((x + i, y, l))
        l = 0
        for i in range(1, imin):
            l += grid.get((x - i, y), 0)
        for i in range(imin, imax + 1):
            l += grid.get((x - i, y), 0)
            ns.append((x - i, y, l))
    if d == "-":
        l = 0
        for i in range(1, imin):
            l += grid.get((x, y + i), 0)
        for i in range(imin, imax + 1):
            l += grid.get((x, y + i), 0)
            ns.append((x, y + i, l))
        l = 0
        for i in range(1, imin):
            l += grid.get((x, y - i), 0)
        for i in range(imin, imax + 1):
            l += grid.get((x, y - i), 0)
            ns.append((x, y - i, l))
    return ns

def minimum_heat_loss(grid, d, a, b):
    horizon = {(0, 0, 0)}
    seen = defaultdict(lambda: float("inf"))
    xm = max(p[0] for p in grid.keys())
    ym = max(p[1] for p in grid.keys())

    while horizon:
        new_horizon = set()
        for x, y, hl in horizon:
            if grid.get((x, y)) is None:
                continue
            for n in neighbours(grid, x, y, d, a, b):
                xx, yy, ll = n
                if grid.get((xx, yy)) is None:
                    continue
                loss = ll + hl
                if loss <= seen[xx, yy, d]:
                    seen[xx, yy, d] = loss
                    new_horizon.add((xx, yy, loss))

        horizon = new_horizon

        if d == "|":
            d = "-"
        else:
            d = "|"

    return min(seen[xm, ym, d] for d in "-|")


def steps(grid, a, b):
    return min(
        minimum_heat_loss(grid, "|", a, b),
        minimum_heat_loss(grid, "-", a, b)
    )

grid = parse("input")

print("Part 1:", steps(grid, 1, 3))
print("Part 2:", steps(grid, 4, 10))
