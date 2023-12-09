from itertools import pairwise

def extrapolate(numbers):
    line = numbers
    f = [line[0]]
    l = [line[-1]]

    while True:
        new_line = [b - a for a, b in pairwise(line)]
        f.append(new_line[0])
        l.append(new_line[-1])

        if not all(n == 0 for n in new_line):
            line = new_line

        else:
            forward = sum(l)

            backward = 0
            for first in reversed(f):
                backward = first - backward

            return backward, forward

with open("input") as f:
    one = two = 0
    for line in f.readlines():
        numbers = [int(n) for n in line.split()]
        backward, forward = extrapolate(numbers)
        one += forward
        two += backward

print("Part 1:", one)
print("Part 2:", two)
