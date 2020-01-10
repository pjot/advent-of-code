def parse(file):
    g = {}
    m_y = 0
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            m_y = max(y, m_y)
            for x, c in enumerate(line.strip()):
                g[x, y] = c
    return g, m_y

def draw(g):
    for y in range(-5, 8):
        for x in range(-5, 8):
            print(g.get((x, y), ' '), end='')
        print()

def walk(c, d):
    x, y = c
    if d == 'N':
        return x, y - 1
    if d == 'E':
        return x + 1, y
    if d == 'S':
        return x, y + 1
    if d == 'W':
        return x - 1, y

def iterate(g, c, d):
    directions = ['N', 'E', 'S', 'W']
    infected = False
    n = g.get(c, '.')
    if n == '#':
        new_dir = (directions.index(d) + 1) % 4
        d = directions[new_dir]
        g[c] = 'F'
        c = walk(c, d)
    elif n == '.':
        g[c] = 'W'
        new_dir = (directions.index(d) - 1) % 4
        d = directions[new_dir]
        c = walk(c, d)
    elif n == 'F':
        new_dir = (directions.index(d) + 2) % 4
        d = directions[new_dir]
        g[c] = '.'
        c = walk(c, d)
    elif n == 'W':
        g[c] = '#'
        infected = True
        c = walk(c, d)

    return g, c, d, infected


g, side = parse('input')
c = side // 2, side // 2
d = 'N'

def infected(g, c, d, n):
    cnt = 0
    for i in range(n):
        g, c, d, infected = iterate(g, c, d)
        if infected:
            cnt += 1
    return cnt

print(infected(g, c, d, 10000000))
