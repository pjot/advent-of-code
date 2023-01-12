import strutils
import sets

type
    Direction = enum
        up
        down
        left
        right

    Point = object
        x, y: int

iterator parse(filename: string): Direction =
    for c in readFile filename:
        case c
        of 'v':
            yield down
        of '^':
            yield up
        of '>':
            yield right
        of '<':
            yield left
        else:
            discard

proc step(p: Point, direction: Direction): Point =
    case direction
    of up:
        return Point(x: p.x, y: succ p.y)
    of down:
        return Point(x: p.x, y: pred p.y)
    of right:
        return Point(x: succ p.x, y: p.y)
    of left:
        return Point(x: pred p.x, y: p.y)


proc walk(filename: string): int =
    var
        seen = initHashSet[Point]()
        p = Point(x: 0, y: 0)

    for d in parse filename:
        p = step(p, d)

        seen.incl p

    return len seen

proc doubleWalk(filename: string): int =
    var
        seen = initHashSet[Point]()
        santa = Point(x: 0, y: 0)
        robot = Point(x: 0, y: 0)
        i = 0

    for d in parse filename:
        if i mod 2 == 0:
            santa = step(santa, d)
        else:
            robot = step(robot, d)

        seen.incl santa
        seen.incl robot
        inc i

    return len seen

echo "Part 1: ", walk "input.txt"
echo "Part 2: ", doubleWalk "input.txt"