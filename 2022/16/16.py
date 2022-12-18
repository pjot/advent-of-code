import itertools
import functools
from collections import defaultdict

def parse(file):
    valves = {}
    with open(file) as f:
        for line in f.readlines():
            line = line.strip()
            p = line.split()
            name = p[1]
            rate = int(p[4].replace(";", "").split("=").pop())
            neighbours = []
            while True:
                v = p.pop()
                if v.startswith("valve"):
                    break
                else:
                    neighbours.append(v.replace(",", ""))
            valves[name] = (rate, neighbours)
    return valves

def distance(a, b, distances):
    horizon = [(0, a)]
    seen = set()
    best = 10000
    while horizon:
        new_horizon = []
        for d, h in horizon:
            seen.add(h)
            for n, di in distances[h].items():
                if n in seen:
                    continue
                if n == b:
                    distance = d + di
                    if distance < best:
                        best = distance
                        continue
                new_horizon.append((d + di, n))
        horizon = new_horizon
    return best

def calculate_distances(valves):
    pumps = {
        v for v, (rate, _) in valves.items()
        if rate > 0
    }
    pumps.add("AA")
    all_distances = {
        v: { n: 1 for n in ns }
        for v, (_, ns) in valves.items()
    }
    valve_distances = defaultdict(dict)
    for a in valves.keys():
        if a not in pumps:
            continue
        for b in valves.keys():
            if b not in pumps or b == "AA":
                continue
            if a == b:
                continue
            valve_distances[a][b] = distance(a, b, all_distances)

    return valve_distances


def generate_paths(limit):
    paths = set()
    horizon = [(limit, ["AA"])]
    while horizon:
        new_horizon = []
        for time, path in horizon:
            current = path[-1]
            paths.add(tuple(path))
            for n, d in valve_distances[current].items():
                if n in path:
                    continue
                if time - d - 2 < 0:
                    continue
                new_horizon.append((time - d - 1, path + [n]))
        horizon = new_horizon
    return paths

def highest_pressure(paths, limit=30):
    highest = 0
    for path in paths:
        pressure = pressure_for_path(path, limit)
        highest = max(pressure, highest)
    return highest

@functools.cache
def pressure_for_path(path, limit):
    path = list(path)
    pressure = 0
    minute = 0
    current = path.pop(0)
    while path and limit > minute:
        n = path.pop(0)
        # move
        minute += valve_distances[current][n]
        # open valve
        minute += 1

        rate, _ = valves[n]
        pressure += (limit - minute) * rate

        current = n
    return pressure

valves = parse("input.txt")
valve_distances = calculate_distances(valves)
paths = generate_paths(30)

print("Part 1:", highest_pressure(paths))

paths = generate_paths(26)
best = 0
for a, b in itertools.combinations(paths, 2):
    if set(a) & set(b) == {"AA"}:
        pressure = (
            pressure_for_path(a, 26) +
            pressure_for_path(b, 26)
        )
        best = max(pressure, best)

print("Part 2:", best)
