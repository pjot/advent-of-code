import strutils
import sets

type

    Direction = enum
        Left
        Right
        Up
        Down

    Move = object
        direction: Direction
        steps: int

    Point = object
        x, y: int

    Path = HashSet[Point]

func direction(c: char): Direction =
    case c
    of 'R': Right 
    of 'L': Left
    of 'U': Up
    of 'D': Down
    else: Down

func distance(p: Point): int =
    (abs p.x) + (abs p.y)

func move(p: Point, direction: Direction): Point =
    case direction
    of Up: return Point(x: p.x, y: succ p.y)
    of Down: return Point(x: p.x, y: pred p.y)
    of Right: return Point(x: succ p.x, y: p.y)
    of Left: return Point(x: pred p.x, y: p.y)

func moves(line: string): seq[Move] =
    for p in line.split(','):
        result.add Move(
            direction: direction p[0],
            steps: parseInt p[1 ..< (len p)]
        )

proc parse(filename: string): (seq[Move], seq[Move]) =
    let lines = (readFile filename).splitLines
    return (moves(lines[0]), moves(lines[1]))

func path(moves: seq[Move]): Path =
    var p = Point(x: 0, y: 0)
    for move in moves:
        for step in 0 ..< move.steps:
            p = p.move(move.direction)
            result.incl p

func closest(points: Path): int =
    result = 10000000
    for p in points:
        result = min([result, p.distance])

func distance(point: Point, moves: seq[Move]): int =
    var p = Point(x: 0, y: 0)
    for move in moves:
        for step in 0 ..< move.steps:
            inc result
            p = p.move(move.direction)
            if p == point:
                return

func best(one, two: seq[Move], common: HashSet[Point]): int =
    result = 100000000
    for c in common:
        let total = c.distance(one) + c.distance(two)
        result = min(total, result)

let 
    (one, two) = parse("input.path")
    common = intersection(path one, path two)


echo "Part 1: ", closest common
echo "Part 2: ", best(one, two, common)