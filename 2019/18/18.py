DOORS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEYS = 'abcdefghijklmnopqrstuvwxyz'


def parse_map(file):
    g = {}
    current = None
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            for x, char in enumerate(line.strip()):
                g[(x, y)] = char
                if char == '@':
                    current = (x, y)
    return g, current


def neighbours(point):
    x, y = point
    return [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]


def visible_keys(g, current, keys):
    visible = set()
    visited = set()
    horizon = [current]
    distance = 0
    while horizon:
        new_horizon = []
        distance += 1
        for p in horizon:
            visited.add(p)
            for np in neighbours(p):
                if np in visited:
                    continue
                char = g.get(np, '#')
                if char == '#':
                    continue
                if char in DOORS and char not in keys.upper():
                    continue
                if char in KEYS and char not in keys:
                    visible.add((np, distance))
                else:
                    new_horizon.append(np)
        horizon = new_horizon

    return visible


cache = {}


def h(keys, current):
    return current, ''.join(sorted(keys))


def explore(current, keys=''):
    if h(keys, current) in cache:
        return cache[h(keys, current)]

    alternatives = visible_keys(g, current, keys)

    if len(alternatives) > 0:
        branches = []
        for point, dist in alternatives:
            s = explore(point, keys + g[point])
            branches.append(dist + s)
        cache[h(keys, current)] = min(branches)
        return min(branches)

    if len(alternatives) == 0:
        cache[h(keys, current)] = 0
        return 0


g, current = parse_map('input.map')

print('Part 1:', explore(current))
