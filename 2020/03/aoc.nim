import strutils
import tables

type
    Coordinate = tuple
        x, y: int

    Trees = Table[Coordinate, bool]

proc parse(filename: string): Trees =
    var file = readFile filename
    file.stripLineEnd

    let lines = file.splitLines

    for y, line in lines:
        for x, c in line:
            result[(x, y)] = c == '#'

func walk(t: Trees, right, down: int): int =
    var x, y, height, width: int
    for c in t.keys:
        height = max(height, c.y)
        width = max(width, c.x)

    inc width

    while y < height:
        x.inc right
        y.inc down

        if x >= width:
            x.dec width

        if t[(x, y)]:
            inc result

func one(t: Trees): int =
    t.walk(3, 1)

func two(t: Trees): int =
    t.walk(1, 1) *
    t.walk(3, 1) *
    t.walk(5, 1) *
    t.walk(7, 1) *
    t.walk(1, 2)

let trees = parse "input.txt"

echo "Part 1: ", one trees
echo "Part 2: ", two trees