import strutils
import tables

proc hasCount(c: int, s: string): bool =
    let t = newCountTable(s)
    for v in t.values:
        if v == c:
            return true
    return false

proc checksum(lines: seq[string]): int =
    var two, three = 0
    for line in lines:
        if hasCount(2, line):
            inc two

        if hasCount(3, line):
            inc three

    return two * three

proc common(a, b: string): string =
    for i, c1 in a:
        let c2 = b[i]
        if c1 == c2:
            result.add c1
    return result

iterator combinations[T](things: seq[T]): (T, T) =
    for i, a in things:
        for j in i .. (len things) - 1:
            yield (a, things[j])

proc bestPair(lines: seq[string]): string =
    let length = len lines[0]
    for (a, b) in combinations(lines):
        let c = common(a, b)
        if (len c) == length - 1:
            return c

var file = readFile "input"
stripLineEnd file
let lines = splitLines file

echo "Part 1: ", checksum lines
echo "Part 2: ", bestPair lines
