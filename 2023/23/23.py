from collections import defaultdict

def parse(file):
    path = {}
    first = False
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            for x, c in enumerate(line.strip()):
                if c in ".<>v^":
                    path[x, y] = c
                    if not first:
                        first = x, y
                    last = x, y
    return path, first, last

def all_neighbours(path, h):
    x, y = h
    ns = [
        (x+1, y),
        (x-1, y),
        (x, y+1),
        (x, y-1),
    ]

    for n in ns:
        if path.get(n) is None:
            continue
        if path.get(n) in ".<>^v":
            yield n

def downhill_neighbours(path):
    def f(p):
        x, y = p
        ns = [
            ((x+1, y), (x+2, y), ">"),
            ((x-1, y), (x-2, y), "<"),
            ((x, y+1), (x, y+2), "v"),
            ((x, y-1), (x, y-2), "^"),
        ]

        for n, nn, d in ns:
            if path.get(n) is None:
                continue
            if path.get(n) == ".":
                yield n, 1
            if path.get(n) in "<>^v":
                if path.get(nn) == "." and d == path.get(n):
                    yield n, 1
                continue
    return f

def longest_path(start, end, neighbours):
    lengths = set()
    paths = [(start, set(), end, 0)]
    while paths:
        new_paths = []
        for current, seen, end, steps in paths:
            s = seen.copy()
            s.add(current)

            for n, d in neighbours(current):
                if n == end:
                    lengths.add(steps + d)
                    continue

                if n in s:
                    continue

                new_paths.append((n, s, end, steps + d))

        paths = new_paths
    return max(lengths)

def skip_neighbours(start, end, path):
    junctions = {start, end}
    for p, v in path.items():
        ns = list(all_neighbours(path, p))
        if len(ns) > 2:
            junctions.add(p)

    # Distance between junctions
    graph = defaultdict(dict)
    for j in junctions:
        horizon = {j}
        seen = set()
        steps = 0

        while horizon:
            new_horizon = set()
            for h in horizon:
                seen.add(h)

                for n in all_neighbours(path, h):
                    if n in seen:
                        continue
                    if n in junctions:
                        graph[j][n] = steps + 1
                        continue

                    new_horizon.add(n)

            horizon = new_horizon
            steps += 1

    for k, v in graph[end].items():
        last = k
        extra = v

    for k, v in graph[start].items():
        first = k
        extra += v

    def graph_neighbours(p):
        return graph[p].items()

    return graph_neighbours, first, last, extra

path, start, end = parse("input")

one = downhill_neighbours(path)
two, first, last, extra = skip_neighbours(start, end, path)

print("Part 1:", extra + longest_path(first, last, one))
print("Part 2:", extra + longest_path(first, last, two))
