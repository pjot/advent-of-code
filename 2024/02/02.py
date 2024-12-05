import itertools
import typing

Report = list[int]

def parse(file: str) -> typing.Iterator[Report]:
    with open(file) as f:
        for line in f.readlines():
            if line.strip():
                yield [int(n) for n in line.split()]

def safe(report: Report) -> bool:
    reverse = report[0] == max(report)
    if report != sorted(report, reverse=reverse):
        return False

    for a, b in itertools.pairwise(report):
        if abs(a - b) not in {1, 2, 3}:
            return False

    return True

def safe_dampened(report: Report) -> bool:
    for p, _ in enumerate(report):
        smaller = report.copy()
        smaller.pop(p)

        if safe(smaller):
            return True

    return False

one = two = 0
for report in parse("input"):
    if safe(report):
        one += 1
    if safe_dampened(report):
        two += 1

print("Part 1:", one)
print("Part 2:", two)
