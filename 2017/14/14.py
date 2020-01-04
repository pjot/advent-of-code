def els(n):
    return list(range(n))


def circular_reverse(l, start, length):
    o = []
    mod = len(l)
    for i in range(length):
        ind = (i + start) % mod
        o.append(l[ind])
    o = list(reversed(o))

    for i, v in enumerate(o):
        ind = (i + start) % mod
        l[ind] = v

    return l


def hash(elements, inputs, pos=0, skip=0):
    for i in inputs:
        elements = circular_reverse(elements, pos, i)
        pos += i + skip
        skip += 1
        pos %= len(elements)
    return elements, pos, skip


def xor(l):
    x = 0
    for i in l:
        x ^= i
    return x


def big_hash(inp):
    ip = [ord(c) for c in inp]
    ip += [17, 31, 73, 47, 23]
    pos = 0
    skip = 0
    elements = els(256)
    for _ in range(64):
        elements, pos, skip = hash(elements, ip, pos, skip)

    dense = []
    for a in range(16):
        dense.append(xor(elements[a * 16:a * 16 + 16]))
    h = ''
    for d in dense:
        n = hex(d)[2:]
        if len(n) == 1:
            n = '0' + n
        h += n

    return h


def binify(g):
    b = ''
    for c in g:
        i = int(c, 16)
        b += '{:04b}'.format(i)
    return b


base = 'uugsqrei'
cnt = 0
grid = {}
ones = set()
for i in range(128):
    b = '{}-{}'.format(base, i)
    h = big_hash(b)
    h = binify(h)
    for j, c in enumerate(h):
        grid[j, i] = c
        if c == '1':
            ones.add((j, i))
            cnt += 1

def neighbours(p):
    x, y = p
    return [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]


regions = 0
while ones:
    horizon = {ones.pop()}
    seen = set()
    while horizon:
        new_horizon = set()
        for h in horizon:
            seen.add(h)
            for n in neighbours(h):
                if n in seen:
                    continue
                if grid.get(n, '0') == '0':
                    continue
                new_horizon.add(n)
                ones.discard(n)
        horizon = new_horizon
    regions += 1


print('Part 1:', cnt)
print('Part 2:', regions)