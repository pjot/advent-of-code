import strutils
import tables
import sequtils
import sets

proc parse(file: string): Table[int, seq[int]] =
    let lines = splitLines (readFile "input")
    var neighbours = initTable[int, seq[int]]()

    for line in lines:
        let
            parts = line.split(" <-> ")
            connections = parts[1].split(", ").map(parseint)
        neighbours[parseint parts[0]] = connections
    
    return neighbours

proc reachable(start: int, neighbours: Table[int, seq[int]]): HashSet[int] =
    var
        horizon = neighbours[start]
        seen = initHashSet[int]()

    while (len horizon) > 0:
        var new_horizon: seq[int]
        for h in horizon:
            for n in neighbours[h]:
                if n in seen:
                    continue

                new_horizon.add n
                seen.incl n

        horizon = new_horizon

    return seen

let neighbours = parse "input"

var
    remaining = toHashSet[int](toSeq neighbours.keys)
    groups = 0
    one = 0

while (len remaining) > 0:
    var
        program = pop remaining
        group = reachable(program, neighbours)

    if 0 in group:
        one = len group

    remaining = remaining - group
    inc groups

echo "Part 1: ", one
echo "Part 2: ", groups
