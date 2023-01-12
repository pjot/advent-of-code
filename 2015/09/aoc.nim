import strutils
import tables
import sets
import algorithm
import sequtils

type
    City = string
    Path = seq[City]
    DistanceFunc = proc (a, b: City): int
    Distances = Table[Path, int]
    Cities = HashSet[City]

proc parse(file: string): (Distances, Cities) =
    var
        distances = initTable[Path, int]()
        f = readFile file
        cities = initHashSet[City]()

    stripLineEnd f

    for line in splitLines f:
        let
            p = line.split
            path = sorted([p[0], p[2]])
            distance = parseInt p[4]

        distances[path] = distance

        cities.incl p[0]
        cities.incl p[2]

    return (distances, cities)

iterator permute(cities: Cities): Path =
    var all = sorted(toSeq(cities))
    while all.nextPermutation() == true:
        yield all

iterator pairwise[T](input: openArray[T]): (T, T) =
    for i in 1 .. input.len - 1:
        yield (input[i], input[i-1])

proc length(p: Path, distance: DistanceFunc): int =
    for (a, b) in p.pairwise:
        result.inc distance(a, b)

proc measure(distances: Distances): DistanceFunc =
    proc distance(a, b: string): int =
        distances[sorted([a, b])]
    
    return distance

let
    (distances, cities) = parse "input"
    distance = measure distances

var 
    shortest = 1000000
    longest = 0

for p in cities.permute:
    let d = length(p, distance)
    shortest = min(shortest, d)
    longest = max(longest, d)

echo "Part 1: ", shortest
echo "Part 2: ", longest
