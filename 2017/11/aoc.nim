import strutils
import sets

type
    Point = object
        x, y: int

proc move(p: Point, step: string): Point =
    case step
    of "ne":
        return Point(x: succ p.x, y: p.y)
    of "sw":
        return Point(x: pred p.x, y: p.y)

    of "n":
        return Point(x: p.x, y: succ p.y)
    of "s":
        return Point(x: p.x, y: pred p.y)

    of "nw":
        return Point(x: pred p.x, y: succ p.y)
    of "se":
        return Point(x: succ p.x, y: pred p.y)

iterator neighbours(p: Point): Point =
    for d in ["ne", "sw", "n", "s", "nw", "se"]:
        yield p.move(d)

proc distance(p: Point): int =
    var
        seen = initHashSet[Point]()
        horizon = @[p]
        steps = 0
        goal = Point(x: 0, y: 0)

    while len(horizon) > 0:
        var new_horizon: seq[Point]
        for h in horizon:
            for n in h.neighbours:
                if n in seen:
                    continue

                if n == goal:
                    return steps + 1

                new_horizon.add n
                seen.incl n

        inc steps
        horizon = new_horizon

proc reverse(points: HashSet[Point]): int =
    var
        seen = initHashSet[Point]()
        horizon = @[Point(x: 0, y: 0)]
        steps = 0
        points = points

    while len(horizon) > 0:
        var new_horizon: seq[Point]
        for h in horizon:
            for n in h.neighbours:
                if n in seen:
                    continue

                points.excl n

                if len(points) == 1:
                    return steps + 1

                new_horizon.add n
                seen.incl n

        inc steps
        horizon = new_horizon

let line = splitLines(readFile "input")[0].split(",")

var
    p = Point(x: 0, y: 0)
    seen = initHashSet[Point]()

for i, step in line:
    p = p.move step
    seen.incl p

echo "Part 1: ", distance p
echo "Part 2: ", reverse seen