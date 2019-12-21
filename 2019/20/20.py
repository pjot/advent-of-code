from collections import defaultdict


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

    return grid, x, y


def neighbours(point):
    x, y = point
    return [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]


def inner(point, w, h):
    x, y = point
    return 4 < x < w - 4 and 4 < y < h - 4


def teleports_in(grid):
    teleports = defaultdict(list)
    for coords, v in grid.items():
        if v not in ['A', 'Z', ' ', '.', '#']:
            teleports[v].append(coords)

    out = {}
    for t in teleports.values():
        assert len(t) == 2, t
        out[t[0]] = t[1]
        out[t[1]] = t[0]

    return out


def explore(start, goal, grid, w, h, recurse=False):
    visited = set()
    horizon = [start]
    distance = 0
    portals = teleports_in(grid)
    while horizon:
        new_horizon = []
        distance += 1
        for point in horizon:
            x, y, level = point
            visited.add(point)
            for n in neighbours((x, y)):
                if (*n, level) in visited:
                    continue
                if n not in grid:
                    continue
                if grid[n] == 'Z' and level == 0:
                    return distance
                if grid[n] == '.':
                    new_horizon.append((*n, level))
                if n in portals:
                    if recurse:
                        delta = 1 if inner(n, w, h) else -1
                    else:
                        delta = 0
                    if 0 <= level + delta < 100:
                        new_horizon.append((*portals[n], level + delta))
        horizon = new_horizon
    return distance


def find(start, end, recurse):
    grid, width, height = parse_file('input.map')
    for coords, v in grid.items():
        if v == start:
            current = (*coords, 0)

    return explore(
        current, end, grid, width, height, recurse
    )


print("Part 1:", find('A', 'Z', recurse=False))
print("Part 2:", find('A', 'Z', recurse=True))
