import strutils
import tables
import sets


type
    Point = object
        x, y: int

proc parse(filename: string): seq[string] =
    var file = readFile filename
    stripLineEnd file
    return splitLines file

var grid = initTable[Point, HashSet[string]]()

for line in parse "input":
    let
        p = split line.replace(":", "")
        start = p[2].split(',')
        finish = p[3].split('x')
        x1 = parseint start[0]
        y1 = parseint start[1]
        x2 = parseint finish[0]
        y2 = parseint finish[1]
        claim = p[0]

    echo "handling claim ", claim
    for x in x1 .. x1 + x2 - 1:
        for y in y1 .. y1 + y2 - 1:
            let p = Point(x: x, y: y)
            if not (grid.hasKey p):
                grid[p] = initHashSet[string]()
            grid[p].incl claim


var share = 0
for v in grid.values:
    if (len v) > 1:
        inc share

echo share