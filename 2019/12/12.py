import math


x = [17, 1, 6, 19]
y = [-7, 4, -2, 11]
z = [-11, -1, -6, 9]

dx = [0, 0, 0, 0]
dy = [0, 0, 0, 0]
dz = [0, 0, 0, 0]

x0 = x
y0 = y
z0 = z
dx0 = dx
dy0 = dy
dz0 = dz


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


def iterate(x, dx):
    dxp = apply_gravity(dx, x)
    xp = apply_velocity(x, dxp)

    return xp, dxp 


def calculate_energies(xs, ys, zs):
    return [abs(x) + abs(y) + abs(z) for x, y, z in zip(xs, ys, zs)]


def p(xs, ys, zs, dxs, dys, dzs):
    for x, y, z, dx, dy, dz in zip(xs, ys, zs, dxs, dys, dzs):
        print('{:>5} {:>5} {:>5} {:>5} {:>5} {:>5}'.format(
            x, y, z, dx, dy, dz
        ))


def energies(x, y, z, dx, dy, dz):
    potential = calculate_energies(x, y, z)
    kinetic = calculate_energies(dx, dy, dz)

    total = [p * k for p, k in zip(potential, kinetic)]
    return sum(total)


def period_for(x, dx):
    x0 = x
    dx0 = dx

    i = 0
    while True:
        x, dx = iterate(x, dx)
        i += 1
        if x == x0 and dx == dx0:
            return i

        
def least_common_multiple(a, b, c):
    lcm_ab = int(a * b / math.gcd(a, b))
    return int(lcm_ab * c / math.gcd(lcm_ab, c))


p_x = period_for(x, dx)
p_y = period_for(y, dy)
p_z = period_for(z, dz)
print(p_x, p_y, p_z, least_common_multiple(p_x, p_y, p_z))