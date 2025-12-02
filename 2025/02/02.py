import typing


def parse(file: str) -> typing.Iterator[tuple[int, int]]:
    with open(file) as f:
        pairs = f.read().split(",")
        for p in pairs:
            a, b = p.split("-")
            yield int(a), int(b)


def invalid_one(n: int) -> bool:
    s = str(n)
    l = len(s)
    if l % 2 == 1:
        return False

    half = l // 2
    return s[half:] == s[:half]


def invalid_two(n: int) -> bool:
    s = str(n)
    l = len(s)

    for part in range(1, l // 2 + 1):
        if l % part != 0:
            continue

        repeat = l // part
        section = s[:part]
        if s == section * repeat:
            return True
    return False


one = two = 0
for a, b in parse("input"):
    for n in range(a, b + 1):
        if invalid_one(n):
            one += n
        if invalid_two(n):
            two += n

print("Part 1:", one)
print("Part 2:", two)
