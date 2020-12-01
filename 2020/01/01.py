import itertools

lines = []
with open("input.txt") as f:
    for l in f.readlines():
        lines.append(int(l))

def two_makes_2020(ls):
    for a, b in itertools.combinations(ls, 2):
        if a + b == 2020:
            return a, b

def three_makes_2020(ls):
    for a, b, c in itertools.combinations(ls, 3):
        if a + b + c == 2020:
            return a, b, c

a, b = two_makes_2020(lines)
print("Part 1:", a * b)

a, b, c = three_makes_2020(lines)
print("Part 2:", a * b * c)
