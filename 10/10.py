import math
from collections import defaultdict


def parse_file(file):
    with open(file) as f:
        return [
            [d for d in l.strip()]
            for l in f.readlines()
        ]


def group_by_angle(x, y, m):
    asteroids = defaultdict(list)
    for x2 in range(len(m)):
        for y2 in range(len(m)):
            if x == x2 and y == y2:
                continue
            dx = x2 - x
            dy = y - y2
            if m[y2][x2] == '#':
                angle = int(360 * math.atan2(dy, dx) * 10000 / (2 * math.pi))
                length = dx*dx + dy*dy
                asteroids[angle].append((length, (x2, y2)))

    return asteroids


def count_asteroids(x, y, m):
    return len(group_by_angle(x, y, m))


m = parse_file('input.map')
high = 0
best = (None, None)
for x in range(len(m)):
    for y in range(len(m)):
        if m[y][x] != '#':
            continue
        cnt = count_asteroids(x, y, m)
        if cnt > high:
            high = cnt
            best = (x, y)
print("Part 1:", high)

grouped_for_best = group_by_angle(best[0], best[1], m)
import pprint
pprint.pprint(grouped_for_best)


