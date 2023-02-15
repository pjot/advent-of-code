import strutils

proc parse(filename: string): seq[int] =
    var file = readFile filename
    file.stripLineEnd
    for line in file.splitLines:
        result.add (parseInt line)

func one(numbers: seq[int]): int =
    for i, a in numbers:
        for j in i .. (len numbers) - 1:
            let b = numbers[j]
            if a + b == 2020:
                return a * b

func two(numbers: seq[int]): int =
    for i, a in numbers:
        for j in i .. (len numbers) - 1:
            for k in j .. (len numbers) - 1:
                let
                    b = numbers[j]
                    c = numbers[k]
                if a + b + c == 2020:
                    return a * b * c

let numbers = parse "input.txt"

echo "Part 1: ", one numbers
echo "Part 2: ", two numbers