import re


nodes = {}
with open('input') as f:
    f.readline()
    f.readline()
    for line in f.readlines():
        parts = re.split(r'\s+', line.strip())
        coords = parts[0].split('-')

        x = int(coords[1][1:])
        y = int(coords[2][1:])
        used = int(parts[2][:-1])
        avail = int(parts[3][:-1])
        nodes[x, y] = (used, avail)

pairs = 0
for (x1, y1), (used1, avail1) in nodes.items():
    for (x2, y2), (used2, avail2) in nodes.items():
        if (x1, y1) != (x2, y2) and used1 < avail2 and used1 > 0:
            pairs += 1

print('Part 1:', pairs)

def neighbours(x, y):
    return [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]

print('Part 2:', 30 * 5 + 44 + 1)

for y in range(35):
    for x in range(35):
        if nodes.get((x, y)) is None:
            c = '@'
        else:
            used, avail = nodes[x, y]
            c = '.'
            if used > 300:
                c = '#'
            elif used == 0:
                c = '%'
        print('{}'.format(c), end='')
        #print('{:3d}/{:2d} '.format(used, avail), end='')
    print()