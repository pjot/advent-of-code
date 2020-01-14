def draw(r, e):
    for i, v in enumerate(r):
        if e[0] == i and e[1] == i:
            print('<{}>'.format(v), end='')
        elif e[0] == i:
            print('({})'.format(v), end='')
        elif e[1] == i:
            print('[{}]'.format(v), end='')
        else:
            print(' {} '.format(v), end='')
    print()

def after(n):
    r = [3, 7]
    e = [0, 1]

    while True:
        r0 = r[e[0]]
        r1 = r[e[1]]
        s = str(r0 + r1)
        for d in s:
            r.append(int(d))
        e[0] += r0 + 1
        e[0] %= len(r)
        e[1] += r1 + 1
        e[1] %= len(r)
        if len(r) > n + 10:
            return ''.join(map(str, r[n:n+10]))


def find(n):
    r = '37'
    e = [0, 1]

    while n not in r[-7:]:
        r0 = int(r[e[0]])
        r1 = int(r[e[1]])
        r += str(r0 + r1)
        e[0] += r0 + 1
        e[0] %= len(r)
        e[1] += r1 + 1
        e[1] %= len(r)

    return r.index(n)


print('Part 1:', after(990941))
print('Part 2:', find('990941'))