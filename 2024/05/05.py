from collections import defaultdict
from functools import cmp_to_key

def parse(file):
    ordering_rules = defaultdict(set)
    updates = []
    with open(file) as f:
        for line in f.readlines():
            if "|" in line:
                a, b = line.strip().split("|")
                ordering_rules[a].add(b)
            if "," in line:
                updates.append(line.strip().split(","))
    return ordering_rules, updates

def middle(update):
    m = len(update) // 2
    return int(update[m])

def valid_update(rules, update):
    for i, c in enumerate(update):
        before = set(update[:i])
        after = set(update[i+1:])

        if before & rules[c]:
            return 0

    return middle(update)

def key_function(rules):
    def compare(a, b):
        if b in rules[a]:
            return 1
        if a in rules[b]:
            return -1
        return 0

    return cmp_to_key(compare)

rules, updates = parse("input")

one = 0
invalid_updates = []
for update in updates:
    m = valid_update(rules, update)
    one += m
    if m == 0:
        invalid_updates.append(update)

two = 0
for update in invalid_updates:
    update.sort(key=key_function(rules))
    two += middle(update)

print("Part 1:", one)
print("Part 2:", two)

