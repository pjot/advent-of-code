import functools
from copy import copy

def parse(file):
    pairs = []
    with open(file) as f:
        for lines in f.read().split("\n\n"):
            a, b = lines.strip().split("\n")
            pairs.append((
                eval(a),
                eval(b),
            ))
    return pairs

def is_list(l):
    return isinstance(l, list)

def is_int(n):
    return isinstance(n, int)

def compare(one, two):
    match one, two:
        case list(), int():
            return compare(one, [two])

        case int(), list():
            return compare([one], two)

        case int(), int():
            if one < two:
                return 1
            elif one > two:
                return -1

        case list(), list():
            for a, b in zip(one, two):
                if (c := compare(a, b)) != 0:
                    return c

            if len(one) < len(two):
                return 1
            if len(two) < len(one):
                return -1

    return 0

pairs = parse("input.txt")

right_order = 0
for i, (a, b) in enumerate(pairs):
    if compare(a, b) == 1:
        right_order += i + 1

print("Part 1:", right_order)

divider_packets = [
    [[2]], [[6]],
]

all_packets = copy(divider_packets)
for a, b in pairs:
    all_packets.append(a)
    all_packets.append(b)

sorted_packets = sorted(
    all_packets,
    key=functools.cmp_to_key(compare),
    reverse=True
)

decoder_key = 1
for i, p in enumerate(sorted_packets):
    if p in divider_packets:
        decoder_key *= i + 1

print("Part 2:", decoder_key)
