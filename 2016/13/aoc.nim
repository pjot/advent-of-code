import sets
import tables
import strutils

type
    Coord = tuple
        x, y: int

    Point = enum
        Wall
        Open

    Grid = Table[Coord, Point]

const favourite = 1358

func get*(g: var Grid, c: Coord): Point =
    if not g.hasKey(c):
        let
            (x, y) = c
            v = x*x + 3*x + 2*x*y + y + y*y + favourite
            b = toCountTable(toBin(v, 32))

        if b['1'] mod 2 == 0:
            g[c] = Open
        else:
            g[c] = Wall
        
    return g[c]

iterator neighbours(c: Coord): Coord =
    let
        (x, y) = c
        possible: seq[Coord] = @[
            (x+1, y), (x-1, y),
            (x, y+1), (x, y-1)
        ]
    
    for p in possible:
        if p.x < 0 or p.y < 0:
            continue
        yield p

func reachable(g: var Grid, start: Coord, maxSteps: int): int =
    var
        horizon = initHashSet[Coord]()
        seen = initHashSet[Coord]()
        steps = 0

    horizon.incl(start)

    while len(horizon) > 0:
        var newHorizon = initHashSet[Coord]()
        if steps == maxSteps:
            return len(seen)
        for h in horizon:
            for n in h.neighbours:
                if n in seen:
                    continue
                if g.get(n) == Wall:
                    continue

                seen.incl n
                newHorizon.incl n

        horizon = newHorizon
        inc steps

func distance(g: var Grid, start, target: Coord): int =
    var
        horizon = initHashSet[Coord]()
        seen = initHashSet[Coord]()
        steps = 0

    horizon.incl(start)

    while len(horizon) > 0:
        var newHorizon = initHashSet[Coord]()
        for h in horizon:
            for n in h.neighbours:
                if n in seen:
                    continue
                if g.get(n) == Wall:
                    continue
                if n == target:
                    return steps + 1

                seen.incl n
                newHorizon.incl n

        inc steps
        horizon = newHorizon

var g = Grid()
let
    start = (1, 1)
    target = (31, 39)

echo "Part 1: ", g.distance(start, target)
echo "Part 2: ", g.reachable(start, 50)