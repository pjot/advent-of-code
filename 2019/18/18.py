DOORS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEYS = 'abcdefghijklmnopqrstuvwxyz'


def parse_map(file):
    g = {}
    robots = []
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            for x, char in enumerate(line.strip()):
                g[(x, y)] = char
                if char == '@':
                    robots.append((x, y))
    return g, tuple(robots)


def neighbours(point):
    x, y = point
    return [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]


def visible_keys(g, robots, keys):
    visible = set()
    for i, robot in enumerate(robots):
        visited = set()
        horizon = [robot]
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
                        visible.add((i, np, distance))
                    else:
                        new_horizon.append(np)
            horizon = new_horizon

    return visible


def h(keys, current):
    return current, ''.join(sorted(keys))


def explore(robots, keys=''):
    if h(keys, robots) in cache:
        return cache[h(keys, robots)]

    alternatives = visible_keys(g, robots, keys)

    if len(alternatives) > 0:
        branches = []
        for robot, point, dist in alternatives:
            rs = list(robots)
            rs[robot] = point
            rs = tuple(rs)
            s = explore(rs, keys + g[point])
            branches.append(dist + s)
        cache[h(keys, robots)] = min(branches)
        return min(branches)

    if len(alternatives) == 0:
        cache[h(keys, robots)] = 0
        return 0


cache = {}
g, robots = parse_map('input.map')
print('Part 1:', explore(robots))

cache = {}
g, robots = parse_map('input2.map')
print('Part 2:', explore(robots))
