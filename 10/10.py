import math
from collections import defaultdict


def parse_file(file):
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            for x, thing in enumerate(line.strip()):
                if thing == '#':
                    yield x, y


def group_by_angle(coords, asteroids):
    x, y = coords
    by_angle = defaultdict(list)
    for x2, y2 in asteroids:
        if x == x2 and y == y2:
            continue
        dx = x2 - x
        dy = y - y2

        angle = round(180 * math.atan2(dy, dx) / math.pi, 2) - 90
        if angle < 0:
            angle += 360
        distance = dx*dx + dy*dy
        by_angle[angle].append((distance, (x2, y2)))
        by_angle[angle].sort(key=lambda k: k[0])

    return [(angle, points) for angle, points in by_angle.items()]


def count_asteroids(coords, asteroids):
    return len(group_by_angle(coords, asteroids))


def find_best(asteroids):
    high = 0
    best = (None, None)
    for x, y in asteroids:
        cnt = count_asteroids((x, y), asteroids)
        if cnt > high:
            high = cnt
            best = (x, y)
    return high, best

def shoot(asteroids, station, limit):
    grouped_for_station = group_by_angle(station, asteroids)

    s = sorted(grouped_for_station, key=lambda k: k[0], reverse=True)
    s.insert(0, s.pop())

    dropped = 0
    while True:
        for angle, p in s:
            if len(p) > 0:
                dropped += 1
                _, (x, y) = p.pop(0)
                if dropped == limit:
                    return x, y

asteroids = list(parse_file('input.map'))
high, best = find_best(asteroids)
print("Part 1:", high, best)

x, y = shoot(asteroids, best, 200)
print("Part 2:", 100 * x + y)


