file = 'input.txt'
grid = {}
with open(file) as f:
    for y, line in enumerate(f.readlines()):
        for x, c in enumerate(line.strip()):
            grid[x, y] = int(c)


def neighbours(point, grid):
    x, y = point
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in deltas:
        p = (x + dx, y + dy)
        n = grid.get(p)
        if n is not None:
            yield p, n

def is_low_point(point, grid):
    value = grid[point]
    for _, neighbour in neighbours(point, grid):
        if neighbour <= value:
            return False
    return True

low_points = [
    (point, value)
    for point, value in grid.items()
    if is_low_point(point, grid)
]

print("Part 1:", sum(v + 1 for _, v in low_points))

basins = []
for point, _ in low_points:
    seen = set()
    horizon = [point]
    while len(horizon) > 0:
        current = horizon.pop()
        value = grid[current]
        seen.add(current)

        for n, neighbour in neighbours(current, grid):
            if 9 > neighbour >= value and n not in seen:
                horizon.append(n)

    basins.append(len(seen))

basins = sorted(basins, reverse=True)
print("Part 2:", basins[0] * basins[1] * basins[2])


