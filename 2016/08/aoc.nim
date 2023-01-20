import strutils
import tables
import algorithm

type
    Coord = tuple
        x, y: int

    Light = enum
        On
        Off

    Screen = Table[Coord, Light]

func initScreen(w, h: int): Screen =
    for x in 0 ..< w:
        for y in 0 ..< h:
            result[(x, y)] = Off

iterator parse(f: string): seq[string] =
    var file = readFile f
    file.stripLineEnd

    for line in file.splitLines:
        yield line.split

proc display(screen: Screen) =
    for y in 0 ..< 6:
        var l = ""
        for x in 0 ..< 50:
            l.add (if screen[(x, y)] == On: '#' else: ' ')
        echo l

func active(screen: Screen): int =
    for v in screen.values:
        if v == On:
            inc result

func rotateColumn*(s: var Screen, x, count: int): Screen {.discardable.} =
    var c: seq[Light]
    for y in 0 ..< 6:
        c.add s[(x, y)]

    c.rotateLeft(-count)

    for y in 0 ..< 6:
        s[(x, y)] = c[y]
    return s

func rotateRow*(s: var Screen, y, count: int): Screen {.discardable.} =
    var r: seq[Light]
    for x in 0 ..< 50:
        r.add s[(x, y)]

    r.rotateLeft(-count)

    for x in 0 ..< 50:
        s[(x, y)] = r[x]
    return s

var screen = initScreen(50, 6)
for l in parse "input":
    case l[0]
    of "rect":
        let
            p = l[1].split('x')
            target: Coord = (parseInt p[0], parseInt p[1])

        for x in 0 ..< target.x:
            for y in 0 ..< target.y:
                screen[(x, y)] = On

    of "rotate":
        let
            c = parseInt l[2].split('=')[1]            
            count = parseInt l[4]

        if l[1] == "row":
            screen.rotateRow(c, count)
        else:
            screen.rotateColumn(c, count)


echo "Part 1: ", screen.active
echo "Part 2:"
display(screen)

