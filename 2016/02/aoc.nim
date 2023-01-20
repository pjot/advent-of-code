import strutils
import tables

type
    Point = object
        x, y: int

    Keypad = Table[Point, char]

    Move = enum
        Right
        Left
        Up
        Down

func P(x, y: int): Point =
    Point(x: x, y: y)

const one: Keypad = [
    (P(-1, -1), '1'),
    (P(0, -1), '2'),
    (P(1, -1), '3'),

    (P(-1, 0), '4'),
    (P(0, 0), '5'),
    (P(1, 0), '6'),

    (P(-1, 1), '7'),
    (P(0, 1), '8'),
    (P(1, 1), '9'),
].toTable

const two: Keypad = [
    (P(0, -2), '1'),

    (P(-1, -1), '2'),
    (P(0, -1), '3'),
    (P(1, -1), '4'),

    (P(-2, 0), '5'),
    (P(-1, 0), '6'),
    (P(0, 0), '7'),
    (P(1, 0), '8'),
    (P(2, 0), '9'),

    (P(-1, 1), 'A'),
    (P(0, 1), 'B'),
    (P(1, 1), 'C'),

    (P(0, 2), 'D'),
].toTable

func move(p: Point, m: Move): Point =
    result.x = p.x
    result.y = p.y
    case m
        of Right: inc result.x
        of Left: dec result.x
        of Up: dec result.y
        of Down: inc result.y

iterator parse(f: string): seq[Move] =
    var file = readFile f
    file.stripLineEnd
    for line in file.splitLines:
        var s: seq[Move]
        for c in line:
            case c
                of 'U': s.add Up
                of 'D': s.add Down
                of 'R': s.add Right
                of 'L': s.add Left
                else: discard
        yield s

func trace(pad: Keypad, start: Point, moves: openArray[Move]): Point =
    var p = start
    for m in moves:
        let candidate = p.move(m)
        if pad.hasKey(candidate):
            p = candidate
    return p

proc solve(pad: Keypad): string =
    var p = Point()
    for moves in parse("input.txt"):
        p = pad.trace(p, moves)
        result.add pad[p]

echo "Part 1: ", solve one
echo "Part 2: ", solve two