import itertools
import copy


DOORS = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'


def parse_map(file):
    KEYS = 'abcdefghijklmnopqrstuvxyz'
    grid = {}
    keys = set()
    current = None
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            for x, char in enumerate(line.strip()):
                grid[(x, y)] = char
                if char == '@':
                    current = (x, y)
                if char in KEYS:
                    keys.add((x, y))
    return grid, current, keys


def neighbours(point):
    x, y = point
    return [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]


def visible_keys(grid, current, remaining_keys):
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
                char = grid.get(np, '#')
                if char in DOORS:
                    continue
                if char != '#':
                    new_horizon.append(np)
                    if np in remaining_keys:
                        visible.add((np, distance))
        horizon = new_horizon

    return visible


def pick_prefered(prefered, alternatives):
    for p in prefered:
        for al, d in alternatives:
            if al == p:
                return p, d


def explore(g, keys, current, steps=0, pick=None):
    g = copy.deepcopy(g)
    current = copy.deepcopy(current)
    keys = copy.deepcopy(keys)

    while keys:
        alternatives = visible_keys(g, current, keys)
        if len(alternatives) > 1:
            if pick is not None:
                point, distance = pick
                pick = None
            else:
                print('creating', len(alternatives), 'branches:', [g[p] for p, _ in alternatives])
                branches = [
                    explore(g, keys, current, steps, copy.deepcopy(pick))
                    for pick in alternatives
                ]
                return min(branches)

        if len(alternatives) == 1:
            point, distance = alternatives.pop()

        current = point
        steps += distance
        keys.remove(current)
        door = g[current].upper()

        for p in g.keys():
            if g[p] == door:
                g[p] = '.'
    return steps


grid, current, keys = parse_map('input.map')
print('number of keys', len(keys))

s = explore(grid, keys, current)
print(s)
'''
steps = float('inf')
for prefered in itertools.permutations(keys):
    pref = list(grid.get(p) for p in prefered)
    s = explore(
        copy.deepcopy(grid),
        copy.deepcopy(current),
        copy.deepcopy(keys),
        list(prefered)
    )
    if pref == ['b', 'a', 'c', 'd', 'f', 'e', 'g']:
        print(s)
    if s > 0:
        steps = min(steps, s)

print('min-steps', steps)
'''