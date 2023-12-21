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

def f(x):
    """
    3 points obtained using:

    l = width(grid) # 131
    xs = [65, 65+l, 65+2*l]
    ys = [ra(x) for x in xs]

    Quadratic parameters from Wolfram Alpha given points:
    (65, 3734)
    (196, 33285)
    (327, 92268)

    for equation:

    y = (ax^2 + bx + c) / d

    """
    a = 14716
    b = 30305
    c = -65751
    d = 17161

    return (x * x * a + x * b + c) // d

grid, start = parse("input")

print("Part 1:", reachable_after(grid, start, 64))
print("Part 2:", f(26501365))
