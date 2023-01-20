import strutils
import algorithm

type
    Numbers = (int, int, int)
    Parser = proc(lines: seq[string]): seq[Numbers]

func one(lines: seq[string]): seq[Numbers] =
    for line in lines:
        let p = line.splitWhitespace
        result.add (
            parseInt p[0],
            parseInt p[1],
            parseInt p[2],
        )

func two(lines: seq[string]): seq[Numbers] =
    for i, line in lines:
        if i mod 3 != 0: continue
        
        let
            a = lines[i].splitWhitespace
            b = lines[i+1].splitWhitespace
            c = lines[i+2].splitWhitespace

        result.add (parseInt a[0], parseInt b[0], parseInt c[0])
        result.add (parseInt a[1], parseInt b[1], parseInt c[1])
        result.add (parseInt a[2], parseInt b[2], parseInt c[2])


func isTriangle(a, b, c: int): bool =
    var ns = [a, b, c]
    ns.sort
    return ns[2] < ns[1] + ns[0]

proc triangles(parse: Parser): int =
    var file = readFile "input"
    file.stripLineEnd
    for (a, b, c) in parse(file.splitLines):
        if isTriangle(a, b, c):
            inc result

echo "Part 1: ", triangles one
echo "Part 2: ", triangles two