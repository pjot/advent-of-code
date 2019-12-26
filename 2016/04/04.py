from collections import Counter
import re


def parse_file(file):
    with open(file) as f:
        for line in f.readlines():
            yield parse_line(line.strip())


def parse_line(l):
    n, check = l.split('[')
    parts = n.split('-')
    name = ''.join(parts[:-1])
    sector_id = int(parts[-1:].pop())
    check = check[:-1]
    return name, sector_id, check


def checksum(name):
    c = Counter(name)
    d = sorted(
        [
            (count, -ord(letter), letter)
            for letter, count in c.items()
        ],
        reverse=True
    )
    s = ''.join(letter for _, __, letter in d)
    return s[:5]


s = 0
for name, sector_id, check in parse_file('input'):
    if checksum(name) == check:
        s += sector_id

print('Part 1:', s)

rooms = [
    (name, sector_id)
    for name, sector_id, check in parse_file('input')
    if checksum(name) == check
]

def decrypt(c, n):
    e = ord(c) + (n % 26)
    if e > 122:
        e -= 26
    return chr(e)

for name, sector_id in rooms:
    dec = ''.join([decrypt(c, sector_id) for c in name])
    if 'north' in dec:
        print('Part 2:', sector_id)
