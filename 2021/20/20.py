def parse(file):
    with open(file) as f:
        enhancement = {
            k: v for k, v in enumerate(f.readline().strip())
        }
        f.readline()
        grid = {}
        for y, row in enumerate(f.readlines()):
            for x, c in enumerate(row.strip()):
                grid[x, y] = c
        return enhancement, grid

def bounds(grid):
    xs = set()
    ys = set()
    for x, y in grid.keys():
        xs.add(x)
        ys.add(y)
    return min(xs), max(xs), min(ys), max(ys)

def pixel_value(grid, p, outside_value):
    deltas = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0), (0, 0), (1, 0),
        (-1, 1), (0, 1), (1, 1),
    ]
    neighbours = [
        (d[0]+p[0], d[1]+p[1]) for d in deltas
    ]
    characters = ''.join(
        grid.get(n, outside_value) for n in neighbours
    )
    binary = characters.replace('#', '1').replace('.', '0')
    return int(binary, 2)

def iterate(g, e, outside_value):
    n = {}
    x0, x1, y0, y1 = bounds(g)
    for x in range(x0-1, x1+2):
        for y in range(y0-1, y1+2):
            v = pixel_value(g, (x, y), outside_value)
            n[x, y] = e.get(v)
    return n

def lit_pixels(g):
    return len([p for p in g.values() if p == '#'])

e, g = parse('input.txt')
first = e[0]

for i in range(25):
    g = iterate(g, e, '.')
    g = iterate(g, e, '#' if first == '#' else '.')

    if i == 0:
        print("Part 1:", lit_pixels(g))

print("Part 2:", lit_pixels(g))
