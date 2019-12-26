X, Y = 50, 6

with open('input') as f:
    instructions = []
    for line in f.readlines():
        instructions.append(line.strip())


def parse_instruction(i):
    parts = i.split(' ')
    if parts[0] == 'rect':
        sub = parts[1].split('x')
        return ('rect', int(sub[0]), int(sub[1]))
    if parts[1] == 'column':
        sub = parts[2].split('=')
        return('column', int(sub[1]), int(parts[4]))
    if parts[1] == 'row':
        sub = parts[2].split('=')
        return('row', int(sub[1]), int(parts[4]))


def draw(grid):
    for y in range(Y):
        for x in range(X):
            print(grid[x, y], end='')
        print()


grid = {}
for x in range(X):
    for y in range(Y):
        grid[x, y] = ' '

for instruction in instructions:
    kind, a, b = parse_instruction(instruction)
    if kind == 'rect':
        for x in range(a):
            for y in range(b):
                grid[x, y] = '#'
    if kind == 'row':
        new_row = [
            grid.get(((x-b) % X, a)) for x in range(X)
        ]
        for x, v in enumerate(new_row):
            grid[x, a] = v
    if kind == 'column':
        new_column = [
            grid.get((a, (y-b) % Y)) for y in range(Y)
        ]
        for y, v in enumerate(new_column):
            grid[a, y] = v


lit = len([p for p in grid.values() if p == '#'])
print('Part 1:', lit)
print('Part 2:')
draw(grid)