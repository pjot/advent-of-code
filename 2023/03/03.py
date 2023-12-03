def parse(file):
    grid = {}
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            for x, c in enumerate(line.strip()):
                if c != ".":
                    grid[x, y] = c
    return grid

def full_number(grid, p):
    n = grid[p]

    x, y = p
    left = x - 1, y
    right = x + 1, y

    while grid.get(left, ".").isdigit():
        n = grid.get(left) + n
        left = left[0] - 1, y

    while grid.get(right, ".").isdigit():
        n = n + grid.get(right)
        right = right[0] + 1, y

    return int(n), left

def adjacent_parts(grid, c):
    deltas = [
        (-1, -1),
        (0, -1),
        (1, -1),

        (-1, 0),
        (1, 0),

        (-1, 1),
        (0, 1),
        (1, 1),
    ]
    x, y = c

    parts = set()
    for dx, dy in deltas:
        p = x + dx, y + dy

        if grid.get(p, ".").isdigit():
            parts.add(full_number(grid, p))

    return list(parts)

grid = parse("input")

gears = []
parts = []
seen = set()

for c, v in grid.items():
    if not v.isdigit():
        adjacent = adjacent_parts(grid, c)

        for n, c in adjacent:
            if c not in seen:
                parts.append(n)
                seen.add(c)

        if v == "*" and len(adjacent) == 2:
            ns = [a[0] for a in adjacent]
            gears.append(ns[0] * ns[1])

print("Part 1:", sum(parts))
print("Part 2:", sum(gears))
