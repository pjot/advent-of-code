def parse(file):
    grid = {}
    max_x = max_y = 0
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            max_y = max(max_y, y)
            for x, c in enumerate(line.strip()):
                grid[x, y] = c
                max_x = max(max_x, x)
    return grid, max_x, max_y


def direct_neighbours(point, grid):
    x, y = point
    ns = [
        (x - 1, y + 1), (x, y + 1), (x + 1, y + 1),
        (x - 1, y), (x + 1, y),
        (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
    ]
    return [n for n in ns if n in grid]

def los_neighbours(max_x, max_y):
    def inner(point, grid):
        x, y = point
        directions = [
            (-1, 1), (0, 1), (1, 1),
            (-1, 0), (1, 0),
            (-1, -1), (0, -1), (1, -1),
        ]
        ns = []
        for dx, dy in directions:
            nx, ny = x, y
            while True:
                nx, ny = nx + dx, ny + dy
                if (nx, ny) not in grid:
                    break
                if grid[nx, ny] != '.':
                    ns.append(grid[nx, ny])
                    break
        return ns
    return inner

def iterate(grid, neighbours, occupied):
    new_grid = {}
    for point in grid:
        seat = grid[point]
        ns = neighbours(point, grid)
        if seat == 'L' and ns.count('#') == 0:
            new_grid[point] = '#'
        elif seat == '#' and ns.count('#') > occupied:
            new_grid[point] = 'L'
        else:
            new_grid[point] = seat
    return new_grid

def p(grid, max_y, max_x):
    for y in range(max_y):
        for x in range(max_x):
            print(grid[x, y], end='')
        print()
    print()

def h(grid):
    return list(grid.values())

grid, max_x, max_y = parse('input.txt')
for i in range(100):
    prev = h(grid)
    grid = iterate(grid, direct_neighbours, 3)
    if h(grid) == prev:
        print('Part 1:', h(grid).count('#'))
        break

grid, max_x, max_y = parse('input.txt')
for i in range(100):
    prev = h(grid)
    grid = iterate(grid, los_neighbours(max_x, max_y), 4)
    if h(grid) == prev:
        print('Part 2:', h(grid).count('#'))
        break

