import strutils
import tables
import sets

type
    Parents = Table[string, string]
    Neighbours = Table[string, HashSet[string]]

proc safeAdd(neighbours: var Neighbours, moon, planet: string) =
    if not neighbours.hasKey(planet):
        neighbours[planet] = initHashSet[string]()

    neighbours[planet].incl moon

proc add(neighbours: var Neighbours, moon, planet: string) =
    neighbours.safeAdd(moon, planet)
    neighbours.safeAdd(planet, moon)

proc parse(filename: string): (Parents, Neighbours) =
    var
        parents = Parents()
        neighbours = Neighbours()
        file = readFile filename
    file.stripLineEnd

    for line in splitLines file:
        let 
            parts = line.split(")")
            planet = parts[0]
            moon = parts[1]

        parents[moon] = planet
        neighbours.add(moon, planet)

    return (parents, neighbours)

func orbits(parents: Parents, planet: string): int =
    var curr = planet
    while parents.hasKey(curr):
        inc result
        curr = parents[curr]

func countOrbits(parents: Parents): int =
    for p in parents.keys:
        result.inc parents.orbits(p)

func bfs(start, target: string, neighbours: Neighbours): int =
    var
        horizon = initHashSet[string]()
        seen = initHashSet[string]()

    horizon.incl start
    seen.incl start

    while len(horizon) > 0:
        inc result
        var newHorizon = initHashSet[string]()
        for h in horizon:
            for n in neighbours[h]:
                if n in seen:
                    continue
                seen.incl n

                if n == target:
                    return

                newHorizon.incl n

        horizon = newHorizon

let 
    (parents, neighbours) = parse "starmap.txt"
    you = parents["YOU"]
    santa = parents["SAN"]

echo "Part 1: ", countOrbits(parents)
echo "Part 2: ", bfs(you, santa, neighbours)