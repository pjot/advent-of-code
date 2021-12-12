from collections import defaultdict

def parse(file):
    nodes = defaultdict(list)
    with open(file) as f:
        for line in f.readlines():
            a, b = line.strip().split('-')
            nodes[a].append(b)
            nodes[b].append(a)
    return nodes

def two(cave, path):
    if cave in path and cave.lower() == cave:
        lower_parts = [p for p in path.split(',') if p.lower() == p]
        return len(lower_parts) != len(set(lower_parts))

    return False

def one(cave, path):
    return cave in path and cave.lower() == cave

def paths(nodes, exclude):
    paths = set()
    horizon = {(n, 'start') for n in nodes['start']}

    while horizon:
        new_horizon = set()
        for cave, path in horizon:
            if exclude(cave, path):
                continue

            path += ',' + cave

            if cave == 'end' and not path in paths:
                paths.add(path)
                continue

            for n in nodes[cave]:
                if n == 'start':
                    continue
                new_horizon.add((n, path))
        horizon = new_horizon

    return len(paths)


n = parse('input.txt')

print("Part 1:", paths(n, one))
print("Part 2:", paths(n, two))
