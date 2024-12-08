from collections import defaultdict
from itertools import combinations
import typing

class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other: typing.Hashable) -> bool:
        return hash(self) == hash(other)

    def __add__(self, p: "Point") -> "Point":
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p: "Point") -> "Point":
        return Point(self.x - p.x, self.y - p.y)

    def __le__(self, p: "Point") -> bool:
        return self.x <= p.x and self.y <= p.y

def parse(file) -> tuple[dict[str, set[Point]], Point]:
    antennas = defaultdict(set)
    max_y, max_x = 0, 0
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            if not line.strip():
                continue
            for x, c in enumerate(line.strip()):
                if c != ".":
                    antennas[c].add(Point(x, y))
                max_x = max(x, max_x)
            max_y = max(y, max_y)

    return antennas, Point(max_x, max_y)

def antipoles(
    antennas: set[Point],
    bound: Point,
    multiple: bool = False,
) -> set[Point]:
    poles = set()
    zero = Point(0, 0)
    for a, b in combinations(antennas, 2):
        delta = b - a

        if multiple:
            while zero <= a <= bound:
                poles.add(a)
                a -= delta

            while zero <= b <= bound:
                poles.add(b)
                b += delta
        else:
            for d in [a - delta, b + delta]:
                if zero <= d <= bound:
                    poles.add(d)

    return poles

antennas, bound = parse("input")
one = set()
two = set()
for points in antennas.values():
    one |= antipoles(points, bound, False)
    two |= antipoles(points, bound, True)

print("Part 1:", len(one))
print("Part 2:", len(two))
