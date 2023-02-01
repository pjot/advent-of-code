import strutils
import math

proc parse(filename: string): seq[int] =
    var file = readFile filename
    file.stripLineEnd
    for line in file.splitLines:
        result.add parseInt(line)

func one(m: int): int =
    return floorDiv(m, 3) - 2

func two(m: int): int =
    var mass = m
    while one(mass) > 0:
        mass = one(mass)
        result.inc mass

func solve(masses: seq[int], fuel: proc(m: int): int): int =
    for m in masses:
        result.inc fuel(m)

let masses = parse "masses.txt"

echo "Part 1: ", solve(masses, one)
echo "Part 2: ", solve(masses, two)