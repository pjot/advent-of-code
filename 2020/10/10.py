from collections import defaultdict
from functools import lru_cache

with open('input.txt') as f:
    adapters = [int(i) for i in f.readlines()]

adapters = [0] + sorted(adapters) + [max(adapters) + 3]

diffs = []
for i, a in enumerate(adapters[1:]):
    b = adapters[i]
    diffs.append(a - b)

print('Part 1:', diffs.count(1) * diffs.count(3))

diffs = ''.join(str(d) for d in diffs)
ways = 1
while '1111' in diffs:
    ways *= 7
    diffs = diffs.replace('1111', '', 1)
while '111' in diffs:
    ways *= 4
    diffs = diffs.replace('111', '', 1)
while '11' in diffs:
    ways *= 2
    diffs = diffs.replace('11', '', 1)

print('Part 2:', ways)
