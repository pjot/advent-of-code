import std/strutils

proc maybe_add(sum: int, a, b: char): int =
  var a = parseInt($a)
  var b = parseInt($b)
  if a == b:
    return sum + a

  return sum

var
  numbers = readLines("input")[0]
  half = len(numbers) div 2
  one = 0
  two = 0

for i, n in numbers:
  var other_one = (i + 1) mod len(numbers)
  one = maybe_add(one, n, numbers[other_one])

  var other_two = (i + half) mod len(numbers)
  two = maybe_add(two, n, numbers[other_two])

echo "Part 1: ", one
echo "Part 2: ", two
