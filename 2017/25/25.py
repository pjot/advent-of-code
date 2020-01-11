from collections import defaultdict


def checksum(t):
    cnt = 0
    for v in t.values():
        if v == 1:
            cnt += 1
    return cnt


def iterate(t, p, s):
    c = t[p]
    if s == 'A':
        if c == 0:
            t[p] = 1
            return t, p + 1, 'B'
        else:
            t[p] = 0
            return t, p - 1, 'F'
    if s == 'B':
        if c == 0:
            t[p] = 0
            return t, p + 1, 'C'
        else:
            t[p] = 0
            return t, p + 1, 'D'
    if s == 'C':
        if c == 0:
            t[p] = 1
            return t, p - 1, 'D'
        else:
            t[p] = 1
            return t, p + 1, 'E'
    if s == 'D':
        if c == 0:
            t[p] = 0
            return t, p - 1, 'E'
        else:
            t[p] = 0
            return t, p - 1, 'D'
    if s == 'E':
        if c == 0:
            t[p] = 0
            return t, p + 1, 'A'
        else:
            t[p] = 1
            return t, p + 1, 'C'
    if s == 'F':
        if c == 0:
            t[p] = 1
            return t, p - 1, 'A'
        else:
            t[p] = 1
            return t, p + 1, 'A'

tape = defaultdict(int)
pos = 0
state = 'A'

for i in range(12994925):
    tape, pos, state = iterate(tape, pos, state)

print('Part 1:', checksum(tape))