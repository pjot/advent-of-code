def parse(file):
    tree = {}
    with open(file) as f:
        for line in f.readlines():
            p = line.strip().split(' <-> ')
            tree[p[0]] = {
                'name': p[0],
                'children': p[1].split(', ')
            }
    return tree

def children_of(tree, name):
    children = []
    seen = {name}
    horizon = tree[name]['children']
    while horizon:
        new_horizon = []
        for child in horizon:
            seen.add(child)
            for c in tree[child]['children']:
                if c in seen:
                    continue
                new_horizon.append(c)
        horizon = new_horizon
    return seen

tree = parse('input')
children = children_of(tree, '0')
print('Part 1:', len(children))

unseen = set(tree.keys())
groups = 0
while len(unseen) > 0:
    top = unseen.pop()
    unseen.discard(top)
    unseen -= children_of(tree, top)
    groups += 1
print('Part 2:', groups)

