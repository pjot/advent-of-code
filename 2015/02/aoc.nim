import strutils

proc parse(filename: string): seq[string] =
    var file = readFile filename
    stripLineEnd file
    return splitLines file

proc paper(line: string): int =
    let
        p = line.split "x"
        x = parseInt p[0]
        y = parseInt p[1]
        z = parseInt p[2]
    return 2 * (x*y + x*z + y*z) + min([x*y, x*z, y*z])

proc ribbon(line: string): int =
    let
        p = line.split "x"
        x = parseInt p[0]
        y = parseInt p[1]
        z = parseInt p[2]
        volume = x * y * z
        sum = x + y + z

    return volume + 2 * (sum - max([x, y, z]))

proc one(filename: string): int =
    for line in parse filename:
        result.inc (paper line)

proc two(filename: string): int =
    for line in parse filename:
        result.inc (ribbon line)

echo "Part 1: ", one "input.txt"
echo "Part 2: ", two "input.txt"