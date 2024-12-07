import typing
import operator

Operator = typing.Callable[[int, int], int]

def parse(file: str) -> typing.Iterator[tuple[int, list[int]]]:
    with open(file) as f:
        for line in f.readlines():
            target, ns = line.strip().split(": ")
            numbers = [int(n) for n in ns.split(" ")]
            yield int(target), numbers

def validate(t: int, numbers: list[int], operators: list[Operator]) -> bool:
    sums = [0]
    for n in numbers:
        new_sums = []
        for s in sums:
            for p in [o(s, n) for o in operators]:
                if 0 < p <= t:
                    new_sums.append(p)
        sums = new_sums

    return t in sums

def concatenate(a: int, b: int) -> int:
    return int(str(a) + str(b))

one = two = 0
for t, numbers in parse("input"):
    if validate(t, numbers, [operator.add, operator.mul]):
        one += t
    if validate(t, numbers, [operator.add, operator.mul, concatenate]):
        two += t

print("Part 1:", one)
print("Part 2:", two)
