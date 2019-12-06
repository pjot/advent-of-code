from collections import defaultdict

def read_file(filename):
    with open(filename) as f:
        for l in f.readlines():
            stars = l.strip().split(')')
            yield stars[0], stars[1]

class Node:
    def __init__(self):
        self.inner = None
        self.outer = []
        self.distance = None

def orbit_count(node, nodes):
    orbits = 0
    while node.inner is not None:
        node = nodes[node.inner]
        orbits += 1
    return orbits

def visit(node, nodes):
    n = nodes[node]
    related = n.outer + [n.inner]
    for name in related:
        if nodes[name].distance is None:
            nodes[name].distance = n.distance + 1
            visit(name, nodes)

nodes = defaultdict(Node)
for inner, outer in read_file('starmap.txt'):
    nodes[outer].inner = inner
    nodes[inner].outer.append(outer)

orbits = 0
for node in nodes.values():
    orbits += orbit_count(node, nodes)

print 'part 1:', orbits

inner = nodes['YOU'].inner

nodes[inner].distance = 0
visit(inner, nodes)

santa_inner = nodes['SAN'].inner
print 'part 2:', nodes[santa_inner].distance
