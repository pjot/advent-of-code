from collections import defaultdict

points = {}
splitters = set()
max_y = 0
with open("input") as f:
    for y, line in enumerate(f.read().splitlines()):
        for x, c in enumerate(line):
            if c == "S":
                points[x, y] = 1
                start = x, y
            if c == "^":
                splitters.add((x, y))
        max_y = max(y, max_y)

encountered_splitters = set()
total_beams = 0
while points:
    new_points = defaultdict(int)
    for p, beams in points.items():
        x, y = p
        if y > max_y:
            total_beams += beams
            continue
        if p in splitters:
            new_points[(x + 1, y)] += beams
            new_points[(x - 1, y)] += beams
            encountered_splitters.add(p)
        else:
            new_points[(x, y + 1)] += beams

    points = new_points

print("Part 1:", len(encountered_splitters))
print("Part 2:", total_beams)

