from collections import defaultdict

def parse(file):
    scanners = defaultdict(list)
    scanner = ''
    with open(file) as f:
        for line in f.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            if line.startswith('---'):
                _, _, scanner, _ = line.split()
                scanner = int(scanner)
            else:
                x, y, z = [int(n) for n in line.split(',')]
                scanners[scanner].append((x, y, z))
    return scanners

ROTATIONS = [
    'x', 'y',
    'xx', 'xy', 'yx', 'yy',
    'xxx', 'xxy', 'xyx', 'xyy', 'yxx', 'yyx', 'yyy',
    'xxxy', 'xxyx', 'xxyy', 'xyxx', 'xyyy', 'yxxx', 'yyyx',
    'xxxyx', 'xyxxx', 'xyyyx',
]

def add(a, b):
    return a[0]+b[0], a[1]+b[1], a[2]+b[2]

def difference(a, b):
    return a[0]-b[0], a[1]-b[1], a[2]-b[2]

def inverse(d):
    return -d[0], -d[1], -d[2]

def rotate_once(p, axis):
    x, y, z = p
    if axis == 'x':
        return (x, z, -y)
    if axis == 'y':
        return (-y, x, z)
    return (x, y, z)

def rotate(p, rotation):
    for c in rotation:
        p = rotate_once(p, c)
    return p

def rotate_scanner(points, r):
    rotated = []
    for p in points:
        rotated.append(rotate(p, r))
    return rotated

def shift_scanner(points, delta):
    shifted = []
    for p in points:
        shifted.append(add(p, delta))
    return shifted

def all_rotations(points):
    for r in ROTATIONS:
        yield r, rotate_scanner(points, r)

def most_likely_rotation(one, two):
    most_likely = ''
    delta_count = float('inf')
    for rotation, rotated in all_rotations(two):
        deltas = defaultdict(int)
        for p in one:
            for q in rotated:
                deltas[difference(p, q)] += 1

        if len(deltas) < delta_count:
            delta_count = len(deltas)
            most_likely = rotation

            common_delta = None
            count = 0
            for delta, c in deltas.items():
                if c > count:
                    count = c
                    common_delta = delta

    rotated = rotate_scanner(two, most_likely)
    shifted = shift_scanner(rotated, common_delta)

    in_common = set(one) & set(shifted)

    return most_likely, common_delta, len(in_common)

def map_one(unmapped, mapped):
    for u in unmapped:
        for m in mapped.keys():
            mapped_rotation, mapped_delta = mapped[m]
            rotation, delta, in_common = most_likely_rotation(
                rotate_scanner(scanners[m], mapped_rotation),
                scanners[u],
            )
            if in_common == 12:
                print('Mapped', u, 'using', m)
                mapped[u] = (rotation, difference(mapped_delta, delta))
                unmapped.remove(u)
                return unmapped, mapped

def count_beacons(mapped, scanners):
    beacons = set()
    for m, (r, d) in mapped.items():
        scanner = scanners[m]
        rotated = rotate_scanner(scanner, r)
        shifted = shift_scanner(rotated, inverse(d))

        for b in shifted:
            beacons.add(b)
    return len(beacons)

def manhattan_distance(one, two):
    return sum(abs(a - b) for a, b in zip(one, two))

def largest_distance(mapped):
    highest = 0
    for _, d1 in mapped.values():
        for _, d2 in mapped.values():
            highest = max(highest, manhattan_distance(d1, d2))
    return highest

scanners = parse('input.txt')
mapped = {0: ('', (0, 0, 0))}

unmapped = set(scanners.keys()) - {0}
while unmapped:
    unmapped, mapped = map_one(unmapped, mapped)

print("Part 1:", count_beacons(mapped, scanners))
print("Part 2:", largest_distance(mapped))
