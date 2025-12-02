import typing


def parse(file: str) -> typing.Iterator[tuple[str, int]]:
    with open(file) as f:
        lines = f.read().splitlines()
        for l in lines:
            direction = l[0]
            steps = int(l[1:])
            yield direction, steps


p = 50
zeroes = 0
rotations = 0

for direction, steps in parse("input"):
    old = p

    if direction == "R":
        p += steps
        rotations += p // 100
    else:
        p -= steps
        if p < 0:
            rotations += abs(p // 100)
            if old == 0:
                rotations -= 1

        if p % 100 == 0:
            rotations += 1

    p = p % 100
    zeroes += int(p == 0)

print("Part 1:", zeroes)
print("Part 2:", rotations)
