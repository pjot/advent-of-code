import re
from itertools import product

with open('input.txt') as f:
    m1 = {} 
    m2 = {}
    for line in f.readlines():
        if line.startswith('mask'):
            m = line.strip().split()[2]

            # Part 1
            or_mask = int(m.replace('X', '0'), 2)
            and_mask = int(m.replace('X', '1'), 2)

            # Part 2
            or_masks = []
            and_masks = []
            for xs in product('10', repeat=line.count('X')):
                and_line = m.replace('0', '1')
                or_line = m
                for x in xs:
                    and_line = and_line.replace('X', x, 1)
                    or_line = or_line.replace('X', x, 1)
                or_masks.append(int(or_line, 2))
                and_masks.append(int(and_line, 2))
        else:
            addr, val = re.match(r'mem\[(\d+)\] = (\d+)', line).groups()
            addr = int(addr)
            val = int(val)

            # Part 1
            m1[addr] = (val & and_mask) | or_mask

            # Part 2
            for a, o in zip(and_masks, or_masks):
                m2[(addr & a) | o] = val

print('Part 1:', sum(m1.values()))
print('Part 2:', sum(m2.values()))
