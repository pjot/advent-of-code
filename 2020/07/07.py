import re
from collections import defaultdict

def parse_child(child):
    count, name = child.split(maxsplit=1)
    return int(count), name

tree = defaultdict(list)
parents = defaultdict(set)
with open('input.txt') as f:
    for line in f.readlines():
        parent = re.findall(r'(\w+ \w+) bags contain', line)[0]
        children = re.findall(r'(\d+ \w+ \w+) bags?', line)

        for child in children:
            c = parse_child(child)

            parents[c[1]].add(parent)
            tree[parent].append(c)

seen = set()
def visit(child):
    for parent in parents[child]:
        seen.add(parent)
        visit(parent)

visit('shiny gold')

print('Part 1:', len(seen))

def contents(bag):
    bags = 0
    for count, child in tree[bag]:
        # plus one is the current bag
        bags += count * (contents(child) + 1)
    return bags

print('Part 2:', contents('shiny gold'))
