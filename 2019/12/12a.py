x = [17, 1, 6, 19]
y = [-7, 4, -2, 11]
z = [-11, -1, -6, 9]
dx = [0, 0, 0, 0]
dy = [0, 0, 0, 0]
dz = [0, 0, 0, 0]


def d(a, b):
    if a == b:
        return 0
    return (a - b) / abs(a - b)


def gravity_delta(p1, p2, p3, p4):
    return [
        d(p2, p1) + d(p3, p1) + d(p4, p1),
        d(p1, p2) + d(p3, p2) + d(p4, p2),
        d(p1, p3) + d(p2, p3) + d(p4, p3),
        d(p1, p4) + d(p2, p4) + d(p3, p4),
    ]


def apply_gravity(deltas, coords):
    ds = gravity_delta(*coords)
    return [int(a + b) for a, b, in zip(deltas, ds)]


def apply_velocity(coords, deltas):
    return [int(a + b) for a, b in zip(coords, deltas)]


def iterate(x, y, z, dx, dy, dz):
    dxp = apply_gravity(dx, x)
    dyp = apply_gravity(dy, y)
    dzp = apply_gravity(dz, z)

    xp = apply_velocity(x, dxp)
    yp = apply_velocity(y, dyp)
    zp = apply_velocity(z, dzp)

    return xp, yp, zp, dxp, dyp, dzp


def calculate_energies(xs, ys, zs):
    return [abs(x) + abs(y) + abs(z) for x, y, z in zip(xs, ys, zs)]


def p(xs, ys, zs, dxs, dys, dzs):
    for x, y, z, dx, dy, dz in zip(xs, ys, zs, dxs, dys, dzs):
        print('{:>5} {:>5} {:>5} {:>5} {:>5} {:>5}'.format(
            x, y, z, dx, dy, dz
        ))


def energies(x, y, z, dx, dy, dz):
    potential = calculate_energies(x, y, z)
    print(potential)
    kinetic = calculate_energies(dx, dy, dz)
    print(kinetic)

    total = [p * k for p, k in zip(potential, kinetic)]
    print(total)
    return sum(total)


for i in range(1000):
    x, y, z, dx, dy, dz = iterate(x, y, z, dx, dy, dz)
p(x, y, z, dx, dy, dz)

print("Energy:", energies(x, y, z, dx, dy, dz))