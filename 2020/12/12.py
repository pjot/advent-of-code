def parse(file):
    instructions = []
    with open(file) as f:
        for line in f.readlines():
            kind = line[0]
            length = int(line[1:])
            if kind == 'R':
                kind = 'L'
                length = 360 - length
            instructions.append((kind, length))
    return instructions

def rotate(current, degrees):
    rot = {
        'E': 'N',
        'N': 'W',
        'W': 'S',
        'S': 'E',
    }
    while degrees > 0:
        current = rot[current]    
        degrees -= 90
    return current

def move(x, y, direction, length):
    if direction == 'N':
        dx, dy = 0, 1
    elif direction == 'S':
        dx, dy = 0, -1
    elif direction == 'E':
        dx, dy = 1, 0
    elif direction == 'W':
        dx, dy = -1, 0

    x += dx * length
    y += dy * length
    return x, y

def follow(instructions):
    facing = 'E'
    x, y = 0, 0
    for kind, length in instructions:
        if kind == 'L':
            facing = rotate(facing, length)
            continue

        if kind == 'F':
            kind = facing

        x, y = move(x, y, kind, length)

    return abs(x) + abs(y)

def rotate2(x, y, degrees):
    while degrees > 0:
        x, y = -y, x
        degrees -= 90
    return x, y

def follow2(instructions):
    x, y = 0, 0
    wpx, wpy = 10, 1
    for kind, length in instructions:
        if kind == 'L':
            wpx, wpy = rotate2(wpx, wpy, length)
            continue

        if kind == 'F':
            x += wpx * length
            y += wpy * length
            continue

        wpx, wpy = move(wpx, wpy, kind, length)

    return abs(x) + abs(y)

instr = parse('input.txt')
print('Part 1:', follow(instr))
print('Part 2:', follow2(instr))
