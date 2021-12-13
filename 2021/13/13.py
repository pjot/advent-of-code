def parse(file):
    grid = {}
    folds = []
    with open(file) as f:
        for line in f.readlines():
            line = line.strip()

            if len(line) == 0:
                continue
            elif line.startswith('fold'):
                _, __, fold = line.split()
                coordinate, num = fold.split('=')
                folds.append((coordinate, int(num)))
                continue
            else:
                x, y = [int(i) for i in line.split(',')]
                grid[x, y] = '#'

    return grid, folds

def fold(grid, f):
    coordinate, at = f
    new_grid = {}
    for x, y in grid.keys():
        if coordinate == 'y' and y > at:
            y = 2 * at - y
        if coordinate == 'x' and x > at:
            x = 2 * at - x
        new_grid[x, y] = '#'
    return new_grid

def display(grid):
    max_x = max_y = 0
    for x, y in grid.keys():
        max_x = max(x, max_x)
        max_y = max(y, max_y)

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            print(grid.get((x, y), ' '), end='')
        print()

grid, folds = parse('input.txt')

for i, f in enumerate(folds):
    grid = fold(grid, f)
    if i == 0:
        print('Part 1:', len(grid))

print('Part 2:')
display(grid)
