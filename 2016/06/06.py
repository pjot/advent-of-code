from collections import Counter


def parse_file(file):
    counters = [Counter() for i in range(8)]
    with open(file) as f:
        for line in f.readlines():
            for i, c in enumerate(line.strip()):
                counters[i][c] += 1

    return counters


def most_common(counter):
    count = 0
    char = ''
    for c, cnt in counter.items():
        if cnt > count:
            count = cnt
            char = c
    return char


def least_common(counter):
    count = float('inf')
    char = ''
    for c, cnt in counter.items():
        if cnt < count:
            count = cnt
            char = c
    return char


counters = parse_file('input')
one = ''.join(most_common(c) for c in counters)
print('Part 1:', one)

one = ''.join(least_common(c) for c in counters)
print('Part 2:', one)