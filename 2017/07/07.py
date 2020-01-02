def build_tree(filename):
    nodes = {}
    with open(filename) as f:
        for l in f.readlines():
            l = l.strip()
            if '->' in l:
                parts = l.split(' -> ')
                sub = parts[0].split(' ')
                name = sub[0]
                weight = sub[1].split('(')[1].split(')')[0]
                children = parts[1].split(', ')
            else:
                sub = l.split(' ')
                name = sub[0]
                weight = sub[1].split('(')[1].split(')')[0]
                children = []
            nodes[name] = {
                'name': name,
                'children': children,
                'weight': int(weight),
                'parent': None,
            }

    for name in nodes.keys():
        for child in nodes[name]['children']:
            nodes[child]['parent'] = name
    return nodes


def weight(node, nodes):
    return nodes[node]['weight'] + sum(
        weight(n, nodes)
        for n in nodes[node]['children']
    )

tree = build_tree('input')
bottom = None
for node in tree.values():
    if node['parent'] is None:
        bottom = node['name']
        break

'''
for c in tree['arqoys']['children']:
    print(c, weight(c, tree))
'''

print('Part 1:', bottom)
print('Part 2:', tree['arqoys']['weight'] - 6)