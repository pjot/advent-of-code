def parse(file):
    ports = {}
    with open(file) as f:
        for i, line in enumerate(f.readlines()):
            a, b = line.strip().split('/')
            ports[line.strip()] = (int(a), int(b))
    return ports


def possible(n, road, ports):
    p = []
    for i, (a, b) in ports.items():
        if (n == a or n == b) and i not in road:
            if n == a:
                p.append((i, b))
            else:
                p.append((i, a))
    return p


def new_nodes(ports, n, road):
    nodes = []
    for i, new_n in possible(n, road, ports):
        nodes.append((new_n, road + [i]))
    return nodes


def search(ports, n=0, road=None):
    road = road or []
    nodes = []
    for i, new_n in possible(n, road, ports):
        nodes.append((new_n, road + [i]))

    paths = []
    while len(nodes) > 0:
        new_nodes = []
        for n1, r in nodes:
            for i, new_n in possible(n1, r, ports):
                new_nodes.append((new_n, r + [i]))
            else:
                paths.append(r)
        nodes = new_nodes

    return paths


def strength(path, ports):
    return sum(sum(ports[p]) for p in path)

def strongest(paths, ports):
    return max(strength(p, ports) for p in paths)

def longest(paths, ports):
    length = 0
    max_strength = 0
    for p in paths:
        l = len(p)
        s = strength(p, ports)
        if l > length:
            length = len(p)
            max_strength = s
        elif s > max_strength:
            max_strength = s
    return max_strength

ports = parse('input')
paths = search(ports)

print('Part 1:', strongest(paths, ports))
print('Part 2:', longest(paths, ports))