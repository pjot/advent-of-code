def read_file(filename):
    with open(filename) as f:
        for l in f.readlines():
            stars = l.strip().split(')')
            yield stars[0], stars[1]

class Node:
    def __init__(self, name):
        self.name = name
        self.inner = None
        self.outer = []
        self.distance = None

def orbit_count(node, nodes):
    orbits = 0
    while node.inner is not None:
        node = nodes[node.inner]
        orbits += 1
    return orbits

nodes = {}
for inner, outer in read_file('starmap.txt'):
    if inner not in nodes:
        nodes[inner] = Node(inner)
    if outer not in nodes:
        nodes[outer] = Node(inner)

    nodes[outer].inner = inner
    nodes[inner].outer.append(outer)

def mark_distance(node, nodes):
    if node.inner is not None:
        if nodes[node.inner].distance is None:
            nodes[node.inner].distance = node.distance + 1
            mark_distance(nodes[node.inner], nodes)
    for name in node.outer:
        if nodes[name].distance is None:
            nodes[name].distance = node.distance + 1
            mark_distance(nodes[name], nodes)

your_inner = nodes['YOU'].inner
nodes[your_inner].distance = 0
mark_distance(nodes[your_inner], nodes)

santas_inner = nodes['SAN'].inner
print nodes[santas_inner].distance
