import math

def parse(file):
    grid = set()
    start = (0, 0)
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            for x, c in enumerate(line.strip()):
                if c == "#":
                    grid.add((x, y))
                if c == "S":
                    start = x, y
    return grid, start

def neighbours(h):
    x, y = h
    return [
        (x+1, y),
        (x-1, y),
        (x, y+1),
        (x, y-1),
    ]

def is_hedge(grid, p, size):
    x, y = p
    xmi, xma, ymi, yma = size

    while x > xma:
        x -= xma
    while x < xmi:
        x += xma

    while y > yma:
        y -= yma
    while y < ymi:
        y += yma

    return (x, y) in grid

def boundary(grid):
    ys = set(y for x, y in grid)
    xs = set(x for x, y in grid)

    return (
        min(xs),
        max(xs) + 2,
        min(ys),
        max(ys) + 2
    )

def reachable_after(grid, start, steps):
    horizon = {start}
    even = set()
    odd = set()

    size = boundary(grid)

    for i in range(steps+1):
        new_horizon = set()

        for h in horizon:
            if h in even:
                continue
            if h in odd:
                continue

            if i % 2 == 0:
                even.add(h)
            else:
                odd.add(h)

            for n in neighbours(h):
                if is_hedge(grid, n, size):
                    continue
                if n in even:
                    continue
                if n in odd:
                    continue

                new_horizon.add(n)

        horizon = new_horizon

    if steps % 2 == 0:
        return len(even)
    else:
        return len(odd)
    return vs

def reduce_fraction(a, b):
    g = math.gcd(a, b)
    return a // g, b // g

def formula(grid, start):
    x1, x2, y1, y2 = boundary(grid)
    step = x2 - x1 + 1
    offset = step // 2

    x1, x2, x3 = [offset + step * i for i in [0, 1, 2]]
    y1, y2, y3 = [reachable_after(grid, start, x) for x in [x1, x2, x3]]

    """
    Solve linear eq. system dy = ax² + bx + c
    making sure to keep everything as ints.

    This is not general, but assumes that a, b, c all divide into d
    """
    a, d = reduce_fraction(
        y3 - y2 - y2 + y1,
        x3*x3 - x2*x2 - x2*x2 + x1*x1
    )

    b, _ = reduce_fraction(
        (y2 - y1) * d - a * (x2 * x2 - x1 * x1),
        d * (x2 - x1)
    )

    c, _ = reduce_fraction(y1 * d - a * x1 * x1 - x1 * b, d)

    def f(x):
        return (x * x * a + x * b + c) // d
    return f

grid, start = parse("input")

print("Part 1:", reachable_after(grid, start, 64))
f = formula(grid, start)
print("Part 2:", f(26501365))
