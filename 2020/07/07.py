import re
from collections import defaultdict

def parse_child(child):
    count, name = child.split(maxsplit=1)
    return int(count), name

tree = {}
with open('input.txt') as f:
    for line in f.readlines():
        parent = re.findall(r'(\w+ \w+) bags contain', line)[0]
        children = re.findall(r'(\w+ \w+ \w+) bags?', line)

        tree[parent] = [
            parse_child(child) for child in children
            if child != 'contain no other'
        ]

ways = {'shiny gold'}
prev = 0
while prev != len(ways):
    prev = len(ways)
    for parent, children in tree.items():
        for way in list(ways):
            for _, child in children:
                if child == way:
                    ways.add(parent)

print('Part 1:', len(ways) - 1)

hand = {'shiny gold': 1}
found = 0
prev = -1
while prev != found:
    prev = found
    next_hand = defaultdict(int)
    for parent, parent_count in hand.items():
        if not tree[parent]:
            next_hand[parent] = parent_count

        for child_count, child in tree[parent]:
            total_count = child_count * parent_count
            found += total_count

            next_hand[child] += total_count

    hand = next_hand

print('Part 2:', found)
