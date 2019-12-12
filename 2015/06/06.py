from collections import defaultdict


def parse_instruction(s):
    if s.startswith('toggle'):
        mode = 2
    if s.startswith('turn on'):
        mode = 1
    if s.startswith('turn off'):
        mode = -1

    parts = s[5:].split(' ')
    first = parts[1]
    second = parts[3]

    x1, y1 = map(int, first.split(','))
    x2, y2 = map(int, second.split(','))
    return mode, x1, x2 + 1, y1, y2 + 1


with open('input.txt') as f:
    instructions = [parse_instruction(i) for i in f.readlines()]


grid_1 = defaultdict(defaultdict)
grid_2 = defaultdict(defaultdict)
for x in range(1000):
    for y in range(1000):
        grid_1[x][y] = 0
        grid_2[x][y] = 0

for mode, x1, x2, y1, y2 in instructions:
    for x in range(x1, x2):
        for y in range(y1, y2):
            grid_2[y][x] = max(grid_2[y][x] + mode, 0)
            if mode == 2:
                v = grid_1[y][x]
                if v == 0:
                    grid_1[y][x] = 1
                else:
                    grid_1[y][x] = 0
            if mode == 1:
                grid_1[y][x] = 1
            if mode == -1:
                grid_1[y][x] = 0

lights = 0
brightness = 0
for x in range(1000):
    for y in range(1000):
        lights += grid_1[x][y]
        brightness += grid_2[x][y]

print("Part 1:", lights)
print("Part 2:", brightness)