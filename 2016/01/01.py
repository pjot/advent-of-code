def parse_file(file):
    with open(file) as f:
        return [
            parse_step(step)     
            for step in f.readline().strip().split(', ')
        ]


def parse_step(step):
    return step[0], int(step[1:])


def turn(direction, turn):
    if turn == 'R':
        if direction == 'N':
            return 'E'
        if direction == 'E':
            return 'S'
        if direction == 'S':
            return 'W'
        if direction == 'W':
            return 'N'

    if turn == 'L':
        if direction == 'N':
            return 'W'
        if direction == 'E':
            return 'N'
        if direction == 'S':
            return 'E'
        if direction == 'W':
            return 'S'


def walk(steps):
    x, y = 0, 0
    seen = set((x, y))
    current_direction = 'N'
    first_seen_twice = None
    for direction, length in steps:
        dx, dy = 0, 0
        current_direction = turn(current_direction, direction)
        if current_direction == 'N':
            dy = 1
        if current_direction == 'S':
            dy = -1
        if current_direction == 'E':
            dx = 1
        if current_direction == 'W':
            dx = -1

        for i in range(length):
            x += dx
            y += dy
            if (x, y) in seen and first_seen_twice is None:
                first_seen_twice = x, y
            seen.add((x, y))
    
    return distance((x, y)), distance(first_seen_twice)


def distance(point):
    x, y = point
    return abs(x) + abs(y)


steps = parse_file('input.txt')
one, two = walk(steps)
print('Part 1:', one)
print('Part 2:', two)
