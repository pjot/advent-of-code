def parse(file):
    grid = {}
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            for x, c in enumerate(line.strip('\n')):
                grid[x, y] = c
    return grid


def m(p, d):
    x, y = p
    if d == 'S':
        return x, y + 1
    if d == 'E':
        return x + 1, y
    if d == 'N':
        return x, y - 1
    if d == 'W':
        return x - 1, y


def turns(d):
    if d in ['S', 'N']:
        return ['E', 'W']
    if d in ['E', 'W']:
        return ['S', 'N']


def move(grid, current, direction):
    n = m(current, direction)
    if grid.get(n, ' ') != ' ':
        return n, direction
    else:
        for d in turns(direction): 
            n = m(current, d)
            if grid.get(n, ' ') != ' ':
                return n, d
    return None, None


def follow(file):
    grid = parse(file)
    direction = 'S'
    picked_up = ''
    y = 0
    steps = 0
    for x in range(100):
        if grid.get((x, y)) == '|':
            current = (x, y)
            break
    while True:
        if grid[current] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            picked_up += grid[current]

        current, direction = move(grid, current, direction)

        steps += 1
        if current is None:
            return picked_up, steps


a, b = follow('input')
print('Part 1:', a)
print('Part 2:', b)