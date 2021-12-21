from functools import cache

def indexer(t, d):
    @cache
    def geologic_index(p):
        if p == (0, 0) or p == t:
            return 0

        x, y = p
        if y == 0:
            return x * 16807
        if x == 0:
            return y * 48271

        xm = (x-1, y)
        ym = (x, y-1)

        xgi = erosion_level(geologic_index(xm), d)
        ygi = erosion_level(geologic_index(ym), d)

        return xgi * ygi

    return geologic_index

def erosion_level(index, d):
    return (index + d) % 20183

depth = 4080
target = (14, 785)
tx, ty = target
geologic_index = indexer(target, depth)

es = {
    0: '.',
    1: '=',
    2: '|',
}

risk_level = 0
for y in range(0, ty+1):
    for x in range(0, tx+1):
        gi = geologic_index((x, y))
        el = erosion_level(gi, depth)
        kind = el % 3
        risk_level += kind

print("Part 1:", risk_level)
