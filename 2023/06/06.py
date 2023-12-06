import math

with open("input") as f:
    lines = f.readlines()

    times = [int(i) for i in lines[0].split()[1:]]
    distances = [int(i) for i in lines[1].split()[1:]]

    time = int("".join(c for c in lines[0] if c.isdigit()))
    distance = int("".join(c for c in lines[1] if c.isdigit()))


def beating(t, d):
    r1 = math.floor((1/2) * (t - math.sqrt(t * t - 4 * d)))
    r2 = math.floor((1/2) * (t + math.sqrt(t * t - 4 * d)))
    return r2 - r1

one = 1
for t, d in zip(times, distances):
    one *= beating(t, d)

two = beating(time, distance)

print("Part 1:", one)
print("Part 2:", two)

