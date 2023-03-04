import strutils
import algorithm
import tables

proc parse(filename: string): seq[int] =
    var file = readfile filename
    file.stripLineEnd

    for line in file.splitLines:
        result.add parseint line

    return result.sorted

func path(adapters: seq[int]): int =
    var 
        ones = 0
        threes = 1

    case adapters[0]
    of 1: inc ones
    of 3: inc threes
    else: discard

    for i in 1 .. adapters.len - 1:
        let
            a = adapters[i-1]
            b = adapters[i]
        case b - a
        of 1: inc ones
        of 3: inc threes
        else: discard
    
    return ones * threes

proc paths(adapters: seq[int]): int =
    var cache = initTable[int, int]()
    cache[0] = 1
    for a in adapters:
        cache[a] = 0
        for n in [1, 2, 3]:
            if cache.hasKey(a-n):
                cache[a].inc cache[a-n]

    return cache[adapters.max]

let adapters = parse "input.txt"

echo "Part 1: ", adapters.path
echo "Part 2: ", adapters.paths