from intcode import Computer, parse_file

computer = Computer(parse_file("input.intcode"))
outputs = computer.run_to_output()

x, y = 0, 0
grid = {}
robot = None
for o in outputs:
    c = chr(o)
    if o == 10:
        y += 1
        x = 0
    else:
        grid[(x, y)] = c
        if c in ['v', '<', '>', '^']:
            robot = (x, y)
        x += 1
    print(c, end='')


def neighbours(point):
    x, y = point
    return [
        ('R', (x + 1, y)),
        ('L', (x - 1, y)),
        ('D', (x, y + 1)),
        ('U', (x, y - 1)),
    ]


def is_intersection(point):
    if grid[point] == '.':
        return False

    for _, n in neighbours(point):
        if grid.get(n, ".") == ".":
            return False
    return True


intersections = [point for point in grid if is_intersection(point)]
alignment_parameters = [x * y for x, y in intersections]
print("Part 1:", sum(alignment_parameters))


def straight(point, direction):
    for d, n in neighbours(point):
        if d == direction:
            return n


def turn(f, t):
    d = {
        'L': {
            'U': 'R',
            'D': 'L',
        },
        'U': {
            'R': 'R',
            'L': 'L',
        },
        'R': {
            'U': 'L',
            'D': 'R',
        },
        'D': {
            'R': 'L',
            'L': 'R',
        },
    }
    return d[f][t]


def get_path(robot, grid):
    visited = {robot}
    path = ['L']
    direction = 'L'
    steps = 0
    while True:
        visited.add(robot)

        maybe_next = straight(robot, direction)
        if grid.get(maybe_next, '.') == '#':
            steps += 1
            robot = maybe_next
            continue

        found_turn = False
        for d, n in neighbours(robot):
            if n in visited:
                continue
            if grid.get(n, '.') == '#':
                t = turn(direction, d)
                direction = d
                path.append(steps)
                path.append(t)
                steps = 0
                found_turn = True
                continue
        if not found_turn:
            return path


path = get_path(robot, grid)
p = ','.join(str(s) for s in path)
p = p.replace('L,8,R,10,L,10,L,4,L,6,L,8,L,8,R', 'A')
print(','.join([str(s) for s in path]))
print(p)

print(len(path))


program = parse_file("input.intcode")
program[0] = 2
computer = Computer(program)

