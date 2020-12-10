from collections import defaultdict
from functools import lru_cache

with open('input.txt') as f:
    adapters = [int(i) for i in f.readlines()]

s = [0] + sorted(adapters)

diffs = []
for i in range(1, len(s)):
    diffs.append(s[i] - s[i-1])
diffs.append(3)

print('Part 1:', diffs.count(1) * diffs.count(3))

tree = defaultdict(list)
for i, x in enumerate(s):
    for ii in range(i+1, i+4):
        if ii >= len(s):
            continue
        a = s[ii]
        if 0 < a - x <= 3:
            tree[x].append(a)

tree[max(s)] = [max(s) + 3]

@lru_cache(None)
def search(p):
    if p not in tree.keys():
        return 1

    cnt = 0
    for c in tree[p]:
        cnt += search(c)
    return cnt

print('Part 2:', search(0))
