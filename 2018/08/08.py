def parse(file):
    with open(file) as f:
        return list(map(int, f.readline().split(' ')))


def metadata(f, p=0):
    nodes = f[p]
    md = f[p+1]
    p += 2
    if nodes == 0:
        return f[p:p+md], p+md
    else:
        mdatas = []
        for _ in range(nodes):
            mda, p = metadata(f, p)
            mdatas += mda
        return mdatas + f[p:p+md], p+md

def metadata_two(f, p=0):
    nodes = f[p]
    md = f[p+1]
    p += 2
    if nodes == 0:
        return sum(a for a in f[p:p+md]), p + md
    else:
        mdatas = {}
        for i in range(nodes):
            mda, p = metadata_two(f, p)
            mdatas[i] = mda
        return sum(mdatas.get(c-1, 0) for c in f[p:p+md]), p+md

f = parse('input')
md, _ = metadata(f)
print('Part 1:', sum(md))
md2, _ = metadata_two(f)
print('Part 2:', md2)