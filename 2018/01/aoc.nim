import strutils
import sets

proc next(f: int, line: string): int =
    let
        sign = line[0]
        n = parseint line[1 .. ^1]

    case sign
    of '+':
        return f.succ n
    of '-':
        return f.pred n
    else:
        discard

proc iterate(lines: seq[string]): int =
    var frequency = 0

    for line in lines:
        frequency = next(frequency, line)
    
    return frequency

proc firstSeen(lines: seq[string]): int =
    var
        frequency = 0
        seen = initHashSet[int]()

    while true:
        for line in lines:
            frequency = next(frequency, line)

            if frequency in seen:
                return frequency

            seen.incl frequency

var file = readFile "input"
stripLineEnd file
let lines = splitLines file

echo "Part 1: ", iterate lines
echo "Part 2: ", firstSeen lines