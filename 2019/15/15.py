from intcode import Computer, parse_file
import random
from os import system


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
    for y in range(-21, 22):
        for x in range(-21, 21):
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


def build_grid(program):
    def next_point(steps):
        computer = Computer(program)
        for step in steps:
            computer.next_input = lambda: step
            computer.iterate()
        return computer.output

    program = parse_file('input.intcode')
    oxygen = None

    current = (0, 0)
    grid = {current: 1}
    horizon = [(current, [])]
    while horizon:
        system('clear')
        draw_map(grid)
        new_horizon = []
        for p, steps in horizon:
            for direction, point in neighbours(p):
                this_steps = steps + [direction]
                if point in grid:
                    continue
                else:
                    value = next_point(this_steps)
                    grid[point] = value

                    if value == 2:
                        oxygen = point

                    if value != 0:
                        new_horizon.append((point, this_steps))
        horizon = new_horizon

    draw_map(grid)
    return oxygen, grid


def bfs(grid, start, end=None):
    visited = set()
    distance = 0
    horizon = [start]
    while horizon:
        new_horizon = []
        for p in horizon:
            for _, np in neighbours(p):
                if grid.get(np, 1) == 0:
                    continue

                if end is not None and np == end:
                    return distance + 1

                if np not in visited:
                    new_horizon.append(np)

                visited.add(np)

        horizon = new_horizon
        distance += 1

    return distance


oxygen, grid = build_grid(parse_file("input.intcode"))
print('Part 1:', bfs(grid, (0, 0), oxygen))
print('Part 2:', bfs(grid, oxygen) - 1)
