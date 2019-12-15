from intcode import Computer, parse_file
import random


def walk(point):
    return random.choice(neighbours(point))


def neighbours(point):
    x, y = point
    return [
        (4, (x + 1, y)),
        (3, (x - 1, y)),
        (1, (x, y + 1)),
        (2, (x, y - 1)),
    ]


def draw_map(map):
    for y in range(-25, 25):
        for x in range(-25, 25):
            c = map.get((x, y), -1)
            if c == 0:
                c = '#'
            elif c == 1:
                c = '.'
            elif c == 2:
                c = 'O'
            else:
                c = ' '
            if x == 0 and y == 0:
                c = 'S'
            print(c, end='')
        print()


program = parse_file('input.intcode')
computer = Computer(program)
current = (0, 0)
oxygen = None
map = {current: 1}
for i in range(1500000):
    direction, point = walk(current)
    if map.get(point) == 0:
        continue

    computer.next_input = lambda: direction
    computer.iterate()
    if computer.output == 0:
        map[point] = computer.output
    if computer.output == 1:
        current = point
        map[current] = computer.output
    if computer.output == 2:
        current = point
        oxygen = point
        map[current] = computer.output


def bfs(graph, start, end=None):
    seen = set()
    dist = 0
    horizon = [start]
    while horizon:
        new_horizon = []
        for p in horizon:
            for _, np in neighbours(p):
                if graph.get(np, 1) == 0:
                    continue

                if end is not None and np == end:
                    return dist + 1

                if np not in seen:
                    new_horizon.append(np)

                seen.add(np)

        horizon = new_horizon
        dist += 1

    return dist


print('Oxygen at', oxygen)
for y in range(-25, 25):
    for x in range(-25, 25):
        c = map.get((x, y), -1)
        if c == 0:
            c = '#'
        elif c == 1:
            c = ' '
        elif c == 2:
            c = 'O'
        else:
            c = ' '
        if x == 0 and y == 0:
            c = 'S'
        print(c, end='')
    print()
        

print('Part 1:', bfs(map, (0, 0), oxygen))
print('Part 2:', bfs(map, oxygen) - 1)