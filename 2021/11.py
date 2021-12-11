from collections import defaultdict

def parse(file):
    grid = {}
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            line = line.strip()
            if len(line) == 0:
                continue
            for x, c in enumerate(line):
                grid[x, y] = int(c)
    return grid

def flashing_neighbours(point, grid):
    deltas = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0), (1, 0),
        (-1, 1), (0, 1), (1, 1),
    ]
    x, y = point
    for dx, dy in deltas:
        p = (x + dx, y + dy)
        if p in grid and grid[p] > 0:
            yield p

def step(grid):
    grid = {k: v + 1 for k, v in grid.items()}
    flashed = set()

    while any(v > 9 for v in grid.values()):
        increase = defaultdict(int)

        for p, v in grid.items():
            if v > 9 and p not in flashed:
                flashed.add(p)
                for n in flashing_neighbours(p, grid):
                    increase[n] += 1

        for i, n in increase.items():
            if grid[i] != 0:
                grid[i] += n

        for f in flashed:
            grid[f] = 0

    return grid, len(flashed)

grid = parse('input.txt')
grid_count = len(grid)
flash_count = 0

flashes = 0
steps = 0
while grid_count != flash_count:
    steps += 1
    grid, flash_count = step(grid)
    if steps < 101:
        flashes += flash_count

print("Part 1:", flashes)
print("Part 2:", steps)
