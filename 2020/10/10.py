with open('input.txt') as f:
    adapters = [int(i) for i in f.readlines()]

adapters = [0] + sorted(adapters) + [max(adapters) + 3]

diffs = []
for i, a in enumerate(adapters[1:]):
    b = adapters[i]
    diffs.append(a - b)

print('Part 1:', diffs.count(1) * diffs.count(3))

diffs = ''.join(str(d) for d in diffs)

sevens = 7 ** diffs.count('1111')
diffs = diffs.replace('1111', '')

fours = 4 ** diffs.count('111')
diffs = diffs.replace('111', '')

twos = 2 ** diffs.count('11')

print('Part 2:', sevens * fours * twos)
