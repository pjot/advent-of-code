def read_file(filename):
    with open(filename) as f:
        for l in f.readlines():
            stars = l.strip().split(')')
            yield stars[0], stars[1]

class Node:
    def __init__(self, name):
        self.name = name
        self.inner = None

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

orbits = 0
for node in nodes.values():
    orbits += orbit_count(node, nodes)

print orbits
    
    
