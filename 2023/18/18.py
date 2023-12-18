from itertools import pairwise

def delta(v):
    if v in "R0":
        return (1, 0)
    if v in "D1":
        return (0, 1)
    if v in "L2":
        return (-1, 0)
    if v in "U3":
        return (0, -1)

def parse(file):
    steps = []
    colors = []
    with open(file) as f:
        for line in f.readlines():
            direction, length, color = line.strip().split()

            steps.append((delta(direction), int(length)))

            length = int(color[2:-2], 16)
            direction = color[-2:-1]
            colors.append((delta(direction), length))

    return steps, colors

def area(steps):
    x, y = 0, 0
    vertices = []
    sides = 0
    for deltas, length in steps:
        sides += length

        dx, dy = deltas
        x += dx * length
        y += dy * length

        vertices.append((x, y))

    # Shoelace formula: 2A = sum(det a, b)
    area = 0
    for a, b in pairwise(vertices):
        x1, y1 = a
        x2, y2 = b

        area += x1 * y2 - x2 * y1

    inside = area // 2

    # Pick's theorem: A = i + b / 2 - 1
    # => i = A - b / 2 + 1
    #
    # But we want i + sides:
    # i + b = A + b / 2 + 1
    return inside + sides // 2 + 1

steps, colors = parse("input")

print("Part 1:", area(steps))
print("Part 2:", area(colors))
