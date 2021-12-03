with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

def one(lines):
    gamma = epsilon = ''
    for position, _ in enumerate(lines[0]):
        s = ''.join(line[position] for line in lines)
        gamma += '1' if s.count('1') > s.count('0') else '0'
        epsilon += '0' if s.count('1') > s.count('0') else '1'

    return int(gamma, 2) * int(epsilon, 2)

def substance(lines, keep_fn):
    for position, _ in enumerate(lines[0]):
        s = ''.join(line[position] for line in lines)

        keep = keep_fn(s.count('1'), s.count('0'))
        lines = [l for l in lines if l[position] == keep]

        if len(lines) == 1:
            return int(lines[0], 2)

def two(lines):
    o2 = substance(lines, lambda z, o: '0' if z > o else '1')
    co2 = substance(lines, lambda z, o: '1' if z > o else '0')
    return o2 * co2

print("Part 1:", one(lines))
print("Part 2:", two(lines))
