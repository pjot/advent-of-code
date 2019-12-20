from collections import defaultdict
from time import sleep


def parse_file(file):
    grid = {}
    with open(file) as f:
        y = 0
        for line in f.readlines():
            x = 0
            for c in line:
                if c == '\n':
                    continue
                grid[(x, y)] = c
                x += 1
            y += 1

    return grid


def start(grid):
    for coords, v in grid.items():
        if v == 'A':
            return coords


def neighbours(point):
    x, y = point
    return [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]


def teleports_in(grid):
    teleports = defaultdict(set)
    for coords, v in grid.items():
        if v not in ['A', 'Z', ' ', '.', '#']:
            teleports[v].add(coords)
    return teleports


def explore(start, goal, grid):
    visited = set()
    horizon = [start]
    distance = -1
    teleports = teleports_in(grid)
    while horizon:
        #draw(grid, visited, horizon, distance)
        #sleep(0.1)
        new_horizon = []
        distance += 1
        for p in horizon:
            if grid.get(p) == goal:
                return distance
            visited.add(p)
            for n in neighbours(p):
                if n in visited:
                    continue
                v = grid.get(n, '#')
                if v in ['#', ' ']:
                    continue
                if v in teleports:
                    for tp in teleports[v]:
                        if tp != n:
                            new_horizon.append(tp)
                new_horizon.append(n)
        horizon = new_horizon
    return distance


def draw(grid, visited, horizon, distance):
    for y in range(102):
        print()
        for x in range(108):
            if (x, y) in horizon:
                print('O', end='')
                continue
            if (x, y) in visited:
                print('X', end='')
                continue
            c = grid.get((x, y), ' ')
            print(c, end='')
    print()
    print(distance)


g = parse_file('input.map')
current = start(g)

print(explore(current, 'Z', g))