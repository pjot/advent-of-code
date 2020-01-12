def power(x, y, s):
    r = x + 10
    return (r * (r * y + s) // 100) % 10 -5

def make_grid(s):
    grid = {}
    for x in range(1, 301):
        for y in range(1, 301):
            grid[x, y] = power(x, y, s)
    return grid

def sum_at(x0, y0, size, grid):
    s = 0
    for x in range(x0, x0 + size):
        for y in range(y0, y0 + size):
            s += grid[x, y]
    return s

def largest_square_3(grid):
    coords = ''
    largest = 0
    for x in range(1, 298):
        for y in range(1, 289):
            s = sum_at(x, y, 3, grid)
            if s > largest:
                coords = '{},{}'.format(x, y)
                largest = s
    return coords

def largest_square(grid):
    coords = ''
    largest = 0
    for x in range(1, 298):
        for y in range(1, 289):
            d = max(x, y)
            for i in range(min(300 - d, 18)):
                s = sum_at(x, y, i, grid)
                if s > largest:
                    coords = '{},{},{}'.format(x, y, i)
                    largest = s
    return coords

grid = make_grid(8444)
print('Part 1:', largest_square_3(grid))
print('Part 2:', largest_square(grid))