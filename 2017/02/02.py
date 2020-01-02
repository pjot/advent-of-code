
lines = []
with open('input') as f:
    for l in f.readlines():
        lines.append(
            [int(i) for i in l.strip().split('\t')]
        )


def checksum_one(lines):
    s = 0
    for l in lines:
        s += max(l) - min(l)
    return s


def contribution(line):
    for i, n in enumerate(line):
        for j in range(i + 1, len(line)):
            m = line[j]
            if n % m == 0:
                return n // m
            if m % n == 0:
                return m // n
    return 0

def checksum_two(lines):
    s = 0
    for l in lines:
        s += contribution(l)
    return s



print('Part 1:', checksum_one(lines))
print('Part 2:', checksum_two(lines))