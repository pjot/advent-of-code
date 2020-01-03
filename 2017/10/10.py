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
        h += hex(d)[2:]

    return h


inputs = '129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108'

e, _, _ = hash(els(256), [int(i) for i in inputs.split(',')])
print('Part 1:', e[0] * e[1])

print('Part 2:', big_hash(inputs))
