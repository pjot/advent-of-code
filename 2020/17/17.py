grid_3d = {}
grid_4d = {}

with open('input.txt') as f:
    for y, line in enumerate(f.readlines()):
        for x, c in enumerate(line.strip()):
            grid_3d[x, y, 0] = c
            grid_4d[x, y, 0, 0] = c

def bounds_4d(g):
    minx = miny = minz = minw = 100
    maxx = maxy = maxz = maxw = -100
    for p, c in g.items():
        if c == '.':
            continue
        x, y, z, w = p
        minx = min(minx, x)
        miny = min(miny, y)
        minz = min(minz, z)
        minw = min(minw, w)

        maxx = max(maxx, x)
        maxy = max(maxy, y)
        maxz = max(maxz, z)
        maxw = max(maxw, w)

    return minx, maxx, miny, maxy, minz, maxz, minw, maxw

def bounds_3d(g):
    minx = miny = minz = 100
    maxx = maxy = maxz = -100
    for p, c in g.items():
        if c == '.':
            continue
        x, y, z = p
        minx = min(minx, x)
        miny = min(miny, y)
        minz = min(minz, z)

        maxx = max(maxx, x)
        maxy = max(maxy, y)
        maxz = max(maxz, z)

    return minx, maxx, miny, maxy, minz, maxz

def neighbours_4d(x, y, z, w):
    ns = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                for dw in [-1, 0, 1]:
                    if (dx, dy, dz, dw) != (0, 0, 0, 0):
                        ns.append((x+dx, y+dy, z+dz, w+dw))
    return ns

def neighbours_3d(x, y, z):
    ns = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                if (dx, dy, dz) != (0, 0, 0):
                    ns.append((x+dx, y+dy, z+dz))
    return ns

def iterate_4d(g):
    new = {}
    minx, maxx, miny, maxy, minz, maxz, minw, maxw = bounds_4d(g)

    for x in range(minx - 1, maxx + 2):
        for y in range(miny - 1, maxy + 2):
            for z in range(minz - 1, maxz + 2):
                for w in range(minw - 1, maxw + 2):
                    p = (x, y, z, w)
                    new[p] = next_value(p, g, neighbours_4d)
    return new

def iterate_3d(g):
    new = {}
    minx, maxx, miny, maxy, minz, maxz = bounds_3d(g)

    for x in range(minx - 1, maxx + 2):
        for y in range(miny - 1, maxy + 2):
            for z in range(minz - 1, maxz + 2):
                p = (x, y, z)
                new[p] = next_value(p, g, neighbours_3d)
    return new

def next_value(p, g, ns):
    active = 0
    for n in ns(*p):
        nc = g.get(n, '.')
        if nc == '#':
            active += 1

    if active == 3 or (active == 2 and g.get(p, '.') == '#'):
        return '#'
    else:
        return '.'

for i in range(6):
    grid_4d = iterate_4d(grid_4d)
    grid_3d = iterate_3d(grid_3d)

print('Part 1:', list(grid_3d.values()).count('#'))
print('Part 2:', list(grid_4d.values()).count('#'))
