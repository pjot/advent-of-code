from collections import Counter


class Particle:
    def __init__(self, x, y, z, dx, dy, dz, d2x, d2y, d2z, index):
        self.x = x
        self.y = y
        self.z = z

        self.dx = dx
        self.dy = dy
        self.dz = dz

        self.d2x = d2x
        self.d2y = d2y
        self.d2z = d2z

        self.index = index

    def tick(self):
        self.dx += self.d2x
        self.dy += self.d2y
        self.dz += self.d2z

        self.x += self.dx
        self.y += self.dy
        self.z += self.dz

    def distance(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def __str__(self):
        return 'p=<{},{},{}>, v=<{},{},{}>, a=<{},{},{}>'.format(
            self.x, self.y, self.z,
            self.dx, self.dy, self.dz,
            self.d2x, self.d2y, self.d2z,
        )

def parse(file):
    particles = []
    with open(file) as f:
        for i, line in enumerate(f.readlines()):
            p, v, a = [
                r.replace('<', '').replace('>', '').split('=').pop()
                for r in line.strip().split(', ')
            ]
            x, y, z = map(int, p.split(','))
            dx, dy, dz = map(int, v.split(','))
            d2x, d2y, d2z = map(int, a.split(','))
            particles.append(Particle(
                x, y, z,
                dx, dy, dz,
                d2x, d2y, d2z,
                i
            ))
    return particles


def one():
    ps = parse('input')
    for i in range(400):
        for p in ps:
            p.tick()

    ps.sort(key=lambda p: p.distance())
    return ps[0].index


def prune(ps):
    c = Counter([(p.x, p.y, p.z) for p in ps])
    collisions = {k for k, v in c.items() if v > 1}
    return [
        p for p in ps if (p.x, p.y, p.z) not in collisions
    ]


def two():
    ps = parse('input')
    for i in range(400):
        for p in ps:
            p.tick()
        ps = prune(ps)

    return len(ps)


print('Part 1:', one())
print('Part 2:', two())