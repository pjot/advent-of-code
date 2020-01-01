import itertools


grid = {}
specials = {}
with open('input') as f:
    for y, line in enumerate(f.readlines()):
        for x, char in enumerate(line.strip()):
            grid[x, y] = char
            if char not in ['.', '#']:
                specials[char] = (x, y)


def neighbours(x, y):
    return [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]


def bfs(grid, start, end):
    seen = set()
    horizon = {start}
    distance = 0
    while len(horizon) > 0:
        #draw(grid, seen)
        new_horizon = set()
        distance += 1
        for h in horizon:
            seen.add(h)
            for n in neighbours(*h):
                if n in seen:
                    continue
                if grid.get(n, '#') == '#':
                    continue
                if n == end:
                    return distance
                new_horizon.add(n)

        horizon = new_horizon


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def distance_between(start, end):
    return bfs(grid, specials[start], specials[end])


distances = {}
for a, b in itertools.combinations(specials.keys(), 2):
    d = distance_between(a, b)
    distances[a, b] = d
    distances[b, a] = d

min_distance = float('inf')
for combo in itertools.permutations(specials.keys(), len(specials)):
    if combo[0] != '0':
        continue
    d = 0
    for a, b in pairwise(combo):
        d += distances[a, b]
    min_distance = min(d, min_distance)

print('Part 1:', min_distance)


min_distance = float('inf')
for combo in itertools.permutations(specials.keys(), len(specials)):
    if combo[0] != '0':
        continue
    d = 0
    combo = (*combo, '0')
    for a, b in pairwise(combo):
        d += distances[a, b]
    min_distance = min(d, min_distance)

print('Part 2:', min_distance)