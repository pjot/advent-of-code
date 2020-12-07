import re
from collections import defaultdict

tree = defaultdict(list)
parents = defaultdict(set)
with open('input.txt') as f:
    for line in f.readlines():
        parent = re.findall(r'(\w+ \w+) bags contain', line)[0]
        children = re.findall(r'(\d+ \w+ \w+) bags?', line)

        for child in children:
            count, name = child.split(maxsplit=1)

            parents[name].add(parent)
            tree[parent].append((int(count), name))

def visit(child, seen):
    for parent in parents[child]:
        seen.add(parent)
        seen |= visit(parent, seen)
    return seen

seen = visit('shiny gold', set())

print('Part 1:', len(seen))

def contents(bag):
    bags = 0
    for count, child in tree[bag]:
        # plus one is the current bag
        bags += count * (contents(child) + 1)
    return bags

print('Part 2:', contents('shiny gold'))
