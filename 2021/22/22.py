def parse(file):
    steps = []
    with open(file) as f:
        for line in f.readlines():
            turn, coords = line.strip().split()
            x, y, z = coords.split(',')

            x0, x1 = x.split('..')
            x0 = x0.split('=').pop()
            x = int(x0), int(x1)

            y0, y1 = y.split('..')
            y0 = y0.split('=').pop()
            y = int(y0), int(y1)

            z0, z1 = z.split('..')
            z0 = z0.split('=').pop()
            z = int(z0), int(z1)

            steps.append((turn, (x, y, z)))
    return steps

def coord_overlap(one, two):
    c0, c1 = one
    d0, d1 = two
    if c1 < d0 or d1 < c0:
        return False
    return True

def overlaps(one, two):
    return all(coord_overlap(o, t) for o, t in zip(one, two))

def without_overlap(one, two):
    (ox0, ox1), (oy0, oy1), (oz0, oz1) = one

    (tx0, tx1), ty, tz = two
    ty0, ty1 = ty
    tz0, tz1 = tz

    cubes = set()

    if ox1 < tx1:
        x = ox1+1, tx1
        cubes.add((x, ty, tz))

    if ox0 > tx0:
        x = tx0, ox0-1
        cubes.add((x, ty, tz))

    x = max(tx0, ox0), min(tx1, ox1)
    if oy1 < ty1:
        y = oy1+1, ty1
        cubes.add((x, y, tz))

    if oy0 > ty0:
        y = ty0, oy0-1
        cubes.add((x, y, tz))

    y = max(ty0, oy0), min(ty1, oy1)
    if oz1 < tz1:
        z = oz1 + 1, tz1
        cubes.add((x, y, z))

    if oz0 > tz0:
        z = tz0, oz0 - 1
        cubes.add((x, y, z))

    return cubes

def naive_count_on(steps, limit):
    cubes = {}
    min_value = -limit
    max_value = limit + 1
    for turn, cube in steps:
        x, y, z = cube
        for xx in range(max(x[0], min_value), min(x[1]+1, max_value)):
            for yy in range(max(y[0], min_value), min(y[1]+1, max_value)):
                for zz in range(max(z[0], min_value), min(z[1]+1, max_value)):
                    if turn == 'on':
                        cubes[xx, yy, zz] = 1
                    else:
                        cubes[xx, yy, zz] = 0

    return sum(cubes.values())

def follow_steps(steps):
    on = set()
    for turn, cube in steps:
        while True:
            for previous in list(on):
                if overlaps(cube, previous):
                    on.remove(previous)
                    on |= without_overlap(cube, previous)
                    continue
            else:
                break

        if turn == 'on':
            on.add(cube)

    return on

def size(c):
    return 1 + c[1] - c[0]

def count_on(steps):
    on = follow_steps(steps)
    return sum(
        size(x) * size(y) * size(z)
        for x, y, z in on
    )

steps = parse('input.txt')
print("Part 1:", naive_count_on(steps, limit=50))
print("Part 2:", count_on(steps))
