def parse(file):
    grid = {}
    max_x = max_y = 0
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            for x, c in enumerate(line.strip()):
                grid[x, y] = c
                max_x = max(max_x, x)
                max_y = max(max_y, y)
    return grid, max_x, max_y

def move(grid, char, next_point):
    this = [p for p, v in grid.items() if v == char]
    new_grid = {
        k: '.' if v == char else v
        for k, v in grid.items()
    }
    for t in this:
        x, y = t
        n = next_point(x, y)

        p = n if grid[n] == '.' else t
        new_grid[p] = char

    return new_grid

def hash(grid, max_x, max_y):
    s = ''
    for x in range(max_x+1):
        for y in range(max_y+1):
            s += grid[x, y]
    return s

g, mx, my = parse('input.txt')

steps = 0
state = ''
while True:
    steps += 1

    g = move(g, '>', lambda x, y: (0 if x == mx else x + 1, y))
    g = move(g, 'v', lambda x, y: (x, 0 if y == my else y + 1))

    old_state, state = state, hash(g, mx, my)
    if old_state == state:
        break

print('Part 1:', steps)
