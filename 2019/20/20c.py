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

def inner(point):
    x, y = point
    return 4 < x < 95 and 4 < y < 95


def build_graph(grid):
    graph = {}

    teleports = teleports_in(grid)

    for level in range(15):
        for coords, char in grid.items():
            neighs = set()
            for n in neighbours(coords):
                v = grid.get(n, '#')
                if v not in ['#', ' ']:
                    if level > 0 and v in ['A', 'Z']:
                        continue
                    neighs.add((*n, level))

            if char in teleports:
                for tp in teleports[char]:
                    if tp != coords:
                        if inner(n):
                            if level < 15:
                                neighs.add((*tp, level + 1))
                        else:
                            if level > 0:
                                neighs.add((*tp, level -1))
            graph[(*coords, level)] = neighs
    return graph


def teleports_in(grid):
    teleports = defaultdict(set)
    for coords, v in grid.items():
        if v not in ['A', 'Z', ' ', '.', '#']:
            teleports[v].add(coords)
    return teleports


def explore(start, goal, graph, grid):
    visited = set()
    horizon = [start]
    distance = -1
    while horizon:
        '''
        draw(
            grid,
            visited,
            horizon
        )
        sleep(0.2)
        '''
        new_horizon = []
        distance += 1
        for point in horizon:
            x, y, level = point
            if grid.get((x, y)) == goal and level == 0:
                return distance
            visited.add(point)
            neighbours = graph.get(point)
            if neighbours:
                for np in neighbours:
                    if np in visited:
                        continue
                    new_horizon.append(np)
        horizon = new_horizon
    return distance


def draw(grid, visited, horizon):
    for y in range(34):
        print()
        for i in range(4):
            for x in range(45):
                if (x, y, i) in horizon:
                    print('O', end='')
                    continue
                if (x, y, i) in visited:
                    print('x', end='')
                    continue
                c = grid.get((x, y), ' ')

                print(c, end='')
        print('   ', end='')

    for y in range(34):
        print()
        for i in range(4, 8):
            for x in range(45):
                if (x, y, i) in horizon:
                    print('O', end='')
                    continue
                if (x, y, i) in visited:
                    print('x', end='')
                    continue
                c = grid.get((x, y), ' ')

                print(c, end='')
        print('   ', end='')

    for y in range(34):
        print()
        for i in range(8, 12):
            for x in range(45):
                if (x, y, i) in horizon:
                    print('O', end='')
                    continue
                if (x, y, i) in visited:
                    print('x', end='')
                    continue
                c = grid.get((x, y), ' ')

                print(c, end='')
        print('   ', end='')


grid = parse_file('med.map')
current = start(grid)

graph = build_graph(grid)
print(graph[17, 32, 0])
print(explore((*current, 0), 'Z', graph, grid))
