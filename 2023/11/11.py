from itertools import combinations

def parse(file):
    galaxies = set()
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            for x, c in enumerate(line):
                if c == "#":
                    galaxies.add((x, y))
    return galaxies

def expand(galaxies, delta):
    xs, ys = set(), set()
    for x, y in galaxies:
        xs.add(x)
        ys.add(y)

    missing_xs = set(range(min(xs), max(xs))) - xs
    missing_ys = set(range(min(ys), max(ys))) - ys

    expanded = set()
    for x, y in galaxies:
        dx = sum(delta for mx in missing_xs if mx < x)
        dy = sum(delta for my in missing_ys if my < y)
        expanded.add((x + dx, y + dy))

    return expanded

def manhattan_distance(one, two):
    return sum(abs(a - b) for a, b in zip(one, two))

def solve(galaxies, expansion):
    expanded = expand(galaxies, expansion)

    return sum(
        manhattan_distance(a, b)
        for a, b in combinations(expanded, 2)
    )

galaxies = parse("input")

print("Part 1:", solve(galaxies, 1))
print("Part 2:", solve(galaxies, 999999))
