from itertools import combinations
from z3 import Int, Solver

def parse(file):
    hails = []
    with open(file) as f:
        for line in f.readlines():
            clean = line.replace(",", "").replace("@", "")
            x, y, z, dx, dy, dz = [int(n) for n in clean.split()]
            p = x, y, z
            v = dx, dy, dz
            hails.append((p, v))
    return hails

def km(p, v):
    x, y, _ = p
    dx, dy, _ = v
    k = float(dy)/dx
    m = y - k * x
    return k, m

def intersection(p1, v1, p2, v2):
    k1, m1 = km(p1, v1)
    k2, m2 = km(p2, v2)

    if k1 == k2:
        return 0, 0

    x1, y1, _ = p1
    x = (m2 - m1) / (k1 - k2)
    y = k1 * x + m1
    return x, y

def one(hails):
    a, b = 200000000000000, 400000000000000

    inside = 0
    for (ap, av), (bp, bv) in combinations(hails, 2):
        x, y = intersection(ap, av, bp, bv)
        if a <= x <= b and a <= y <= b:
            x1, y1, _ = ap
            x2, y2, _ = bp
            dx1, dy1, _ = av
            dx2, dy2, _ = bv
            in_future = (
                (x >= x1 if dx1 > 0 else x <= x1) and
                (y >= y1 if dy1 > 0 else y <= y1) and
                (x >= x2 if dx2 > 0 else x <= x2) and
                (y >= y2 if dy2 > 0 else y <= y2)
            )
            if in_future:
                inside += 1

    return inside

def two(hails):
    x = Int("x")
    y = Int("y")
    z = Int("z")
    dx = Int("dx")
    dy = Int("dy")
    dz = Int("dz")
    s = Solver()

    for i, h in enumerate(hails):
        t = Int(f"t{i}")
        s.add(t > 0)

        (xx, yy, zz), (dxx, dyy, dzz) = h
        s.add(x + dx * t == xx + dxx * t)
        s.add(y + dy * t == yy + dyy * t)
        s.add(z + dz * t == zz + dzz * t)

    s.check()
    m = s.model()
    return m[x].as_long() + m[y].as_long() + m[z].as_long()

hails = parse("input")
print("Part 1:", one(hails))
print("Part 2:", two(hails))
