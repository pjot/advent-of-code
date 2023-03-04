import strutils

func seat(line: string): int =
    let converted = line
        .replace("F", "0")
        .replace("L", "0")
        .replace("B", "1")
        .replace("R", "1")
    return fromBin[int](converted)

proc parse(filename: string): seq[int] =
    var file = readfile filename
    file.stripLineEnd
    for line in file.splitLines:
        result.add line.seat

func mine(seats: seq[int]): int =
    for i in seats.min .. seats.max:
        if i notin seats:
            return i

let seats = parse "input.txt"

echo "Part 1: ", seats.max
echo "Part 2: ", seats.mine