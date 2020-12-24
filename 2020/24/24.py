def parse(file):
    grid = {}
    with open(file) as f:
        for line in f.readlines():
            line = line.strip()
            d = ''
            x, y = 0, 0
            for c in line:
                d += c
                if d == 'e':
                    x, y = x + 1, y
                if d == 'w':
                    x, y = x - 1, y
                if d == 'nw':
                    x, y = x, y + 1
                if d == 'ne':
                    x, y = x + 1, y + 1
                if d == 'sw':
                    x, y = x - 1, y - 1
                if d == 'se':
                    x, y = x, y - 1
                if d in ['e', 'w', 'ne', 'nw', 'se', 'sw']:
                    d = ''
            g = grid.get((x, y), '.')
            if g == 'O':
                grid[x, y] = '.'
            else:
                grid[x, y] = 'O'
    return grid

def bounds(grid):
    minx = miny = 100
    maxx = maxy = -100
    for (x, y), c in grid.items():
        if c == '.':
            continue
        minx = min(x, minx)
        maxx = max(x, maxx)
        miny = min(y, miny)
        maxy = max(y, maxy)
    return minx, maxx, miny, maxy

def count_black(grid):
    return list(grid.values()).count('O')

def neighbours(x, y):
    return [
        (x + 1, y + 1),
        (x + 1, y),
        (x, y - 1),
        (x - 1, y - 1),
        (x - 1, y),
        (x, y + 1),
    ]

def iterate(grid):
    minx, maxx, miny, maxy = bounds(grid)
    new_grid = {}
    for x in range(minx-1, maxx+2):
        for y in range(miny-1, maxy+2):
            current = grid.get((x, y), '.')
            ns = ''
            for point in neighbours(x, y):
                ns += grid.get(point, '.')

            if current == 'O' and ns.count('O') in [1, 2]:
                new_grid[x, y] = 'O'

            if current == '.' and ns.count('O') == 2:
                new_grid[x, y] = 'O'
    return new_grid

grid = parse('input.txt')
print('Part 1:', count_black(grid))

for i in range(100):
    grid = iterate(grid)
print('Part 2:', count_black(grid))
