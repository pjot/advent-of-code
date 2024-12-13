import itertools
import typing

Point = tuple[int, int]
Grid = dict[Point, str]
Edge = tuple[Point, Point, str]

def parse(file: str) -> Grid:
    grid = {}
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            line = line.strip()
            if not line:
                continue
            for x, c in enumerate(line):
                grid[x, y] = c
    return grid

def neighbours(p: Point) -> list[Point]:
    x, y = p
    return [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]

def perimeter(points: typing.Iterable[Point]) -> int:
    s = 0
    for p in points:
        for n in neighbours(p):
            if not n in points:
                s += 1
    return s

def direction(p: Point) -> str:
    x, y = p
    if x > 0:
        return "r"
    if x < 0:
        return "l"
    if y > 0:
        return "d"

    return "u"

def add(a: Point, b: Point) -> Point:
    ax, ay = a
    bx, by = b
    return ax + bx, ay + by

def diff(a: Point, b: Point) -> Point:
    ax, ay = a
    bx, by = b
    return ax - bx, ay - by

def edge(inside: Point, outside: Point) -> Edge:
    inside_x, inside_y = inside
    outside_x, outside_y = outside

    x, y = diff(outside, inside)
    rotated = y, -x

    return inside, add(inside, rotated), direction(rotated)

def reduce_once(edges: typing.Iterable[Edge]) -> tuple[set[Edge], bool]:
    out = set(edges)
    for a, b in itertools.combinations(edges, 2):
        a_start, a_end, a_direction = a
        b_start, b_end, b_direction = b

        if a_direction != b_direction:
            continue

        if a_start == b_end:
            out.add((b_start, a_end, b_direction))
            out.remove(a)
            out.remove(b)
            return out, True

        if b_start == a_end:
            out.add((a_start, b_end, b_direction))
            out.remove(a)
            out.remove(b)
            return out, True

    return out, False

def merge(edges: typing.Iterable[Edge]) -> set[Edge]:
    merged, changed = set(edges), True
    while changed:
        merged, changed = reduce_once(merged)
    return merged

def sides(points: typing.Iterable[Point]) -> int:
    edges = set()
    for p in points:
        for n in neighbours(p):
            if not n in points:
                edges.add(edge(p, n))

    return len(merge(edges))


grid = parse("input")
seen = set()
one = two = 0

for c, current in grid.items():
    if c in seen:
        continue

    matching = set()
    discarded = set()
    matching.add(c)

    horizon = {c}
    while horizon:
        new_horizon = set()
        for h in horizon:
            discarded.add(h)

            for n in neighbours(h):
                if not grid.get(n):
                    continue
                if n in discarded:
                    continue

                if grid.get(n) == current:
                    matching.add(n)
                    new_horizon.add(n)
                else:
                    discarded.add(n)
        horizon = new_horizon

    one += len(matching) * perimeter(matching)
    two += len(matching) * sides(matching)

    seen |= matching

print("Part 1:", one)
print("Part 2:", two)
