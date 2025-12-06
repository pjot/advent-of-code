import operator
import functools


def parse(file):
    with open(file) as f:
        lines = f.read().splitlines()
        symbol_line = lines.pop()

        symbols = []
        numbers = []

        current_numbers = [[] for _ in lines]
        symbol = ""

        for i, s in enumerate(symbol_line):
            if s != " ":
                symbol = s

            chars = [line[i] for line in lines]
            if "".join(chars).strip() == "":
                symbols.append(symbol)
                numbers.append(["".join(n) for n in current_numbers])

                symbol = ""
                current_numbers = [[] for _ in lines]
            else:
                for i, c in enumerate(chars):
                    current_numbers[i].append(c)

        numbers.append(["".join(n) for n in current_numbers])
        symbols.append(symbol)

    return symbols, numbers


def take(numbers):
    o = ""
    for n in numbers:
        if n:
            o += n.pop()
    return o


def transpose(numbers):
    lists = [list(str(n)) for n in numbers]
    out = []
    while n := take(lists):
        out.append(int(n))
    return out


symbols, numbers = parse("input")
one = two = 0
for i, s in enumerate(symbols):
    op = operator.add if s == "+" else operator.mul
    n = numbers[i]
    one += functools.reduce(op, [int(m) for m in n])
    two += functools.reduce(op, transpose(n))

print("Part 1:", one)
print("Part 2:", two)
