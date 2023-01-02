import strutils
import sequtils

proc divides(a, b: int): bool =
    return max(a, b) mod min(a, b) == 0

proc divisors(numbers: seq[int]): int =
    for i, a in numbers:
        for bi in i + 1 .. len(numbers) - 1:
            var b = numbers[bi]
            if divides(a, b):
                return max(a, b) div min(a, b)

var
    file = readFile "input"
    one = 0
    two = 0

stripLineEnd file

for line in splitLines file:
    var numbers = toSeq(split line).map(parseint)
    one = one + (max numbers) - (min numbers)
    two = two + divisors(numbers)

echo "Part 1: ", one
echo "Part 2: ", two