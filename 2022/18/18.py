import itertools

def parse(file):
    points = set()
    with open(file) as f:
        for line in f.readlines():
            coordinates = line.strip().split(',')
            points.add(tuple(int(c) for c in coordinates))
    return points

def shares_side(a, b):
    ax, ay, az = a
    bx, by, bz = b
    if ax == bx and ay == by and abs(az - bz) == 1:
        return True
    if ax == bx and abs(ay - by) == 1 and az == bz:
        return True
    if abs(ax - bx) == 1 and ay == by and az == bz:
        return True
    return False

def sides(points):
    total = 0
    seen = []
    for p in points:
        shared = 0
        for s in seen:
            if shares_side(p, s):
                shared += 2
        seen.append(p)
        total += 6 - shared
    return total

def has_point_in_direction(p, d, points):
    px, py, pz = p
    dx, dy, dz = d
    while 0 < px < 20 and 0 < py < 20 and 0 < pz < 20:
        px += dx
        py += dy
        pz += dz
        if (px, py, pz) in points:
            return True
    return False

def is_middle(p, points):
    directions = [
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1),
        (-1, 0, 0),
        (0, -1, 0),
        (0, 0, -1),
    ]
    for d in directions:
        if not has_point_in_direction(p, d, points):
            return False
    return True

def inner_points(points):
    inner = []
    for x in range(0, 20):
        for y in range(0, 20):
            for z in range(0, 20):
                l = x, y, z
                if l in points:
                    continue
                if is_middle(l, points):
                    inner.append(l)
    return inner

points = parse("input.txt")
all_sides = sides(points)
print("Part 1:", all_sides)

inner_sides = sides(inner_points(points))
print("Part 2:", all_sides - inner_sides)
