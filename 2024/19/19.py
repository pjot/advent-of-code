from functools import cache
from typing import Iterable

Towels = tuple[str, ...]

def parse(file) -> tuple[Towels, Iterable[str]]:
    towels = []
    designs = []
    with open("input") as f:
        a, b = f.read().split("\n\n")
        towels = a.strip().split(", ")
        for line in b.splitlines():
            designs.append(line.strip())

    return tuple(towels), designs

@cache
def ways_to_combine(design: str, towels: Towels) -> int:
    combinations = 0
    for t in towels:
        if design == t:
            combinations += 1

        if design.startswith(t):
            remaining = design.replace(t, "", 1)
            possible_towels = remove_impossible(remaining, towels)

            combinations += ways_to_combine(remaining, possible_towels)

    return combinations

def remove_impossible(design: str, towels: Towels) -> Towels:
    possible = []
    for t in towels:
        if t in design:
            possible.append(t)
    return tuple(possible)


towels, designs = parse("input")
one = two = 0
for design in designs:
    combinations = ways_to_combine(design, towels)
    two += combinations
    if combinations:
        one += 1

print("Part 1:", one)
print("Part 2:", two)
