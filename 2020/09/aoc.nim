import strutils

proc parse(filename: string): seq[int] =
    var file = readfile filename
    file.stripLineEnd

    for line in file.splitLines:
        result.add parseint line

iterator combinations(numbers: seq[int]): (int, int) =
    for (i, a) in numbers.pairs:
        for j in i + 1 .. numbers.len - 1:
            yield (a, numbers[j])

func valid(numbers: seq[int], pos: int): bool =
    let target = numbers[pos]
    var previous: seq[int]
    for n in pos - 25 .. pos - 1:
        if n > 0:
            previous.add numbers[n]

    for (a, b) in previous.combinations:
        if a + b == target:
            return true
    return false

func first_invalid(numbers: seq[int]): int =
    for n in 25 .. numbers.len:
        if not numbers.valid(n):
            return numbers[n]

func matching_sum(numbers: seq[int], position, target: int): (bool, int) =
    var
        s = 0
        p = position
        ns: seq[int]

    while s < target:
        s.inc numbers[p]
        ns.add numbers[p]
        p.inc

    if s == target:
        return (true, ns.min + ns.max)
    return (false, 0)

func weakness(numbers: seq[int], invalid: int): int =
    for p in 0 .. numbers.len - 1:
        let (matches, res) = numbers.matching_sum(p, invalid)
        if matches:
            return res

let
    numbers = parse "input.txt"
    one = numbers.first_invalid

echo "Part 1: ", one
echo "Part 2: ", numbers.weakness(one)