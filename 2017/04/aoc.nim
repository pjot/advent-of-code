import sets
import strutils

proc count_one(parts: seq[string]): int =
    return len(toHashSet(parts))

proc count_two(parts: seq[string]): int =
    var unique = initHashSet[HashSet[char]]()
    for p in parts:
        unique.incl toHashSet(p)
    return len unique

var
    one = 0
    two = 0

for line in readFile("input.txt").splitLines:
    var parts = line.split
    if (count_one parts) == (len parts):
        one += 1
    if (count_two parts) == (len parts):
        two += 1

echo "Part 1: ", one
echo "Part 2: ", two