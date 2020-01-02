import re


def hash(banks):
    return '-'.join(str(s) for s in banks)


def shuffle(banks):
    i = banks.index(max(banks))
    l = len(banks)
    to_distribute = banks[i]
    banks[i] = 0
    for j in range(to_distribute):
        banks[(1 + i + j) % l] += 1
    return banks


def repeat(banks):
    seen = {hash(banks)}
    shuffles = 0
    while True:
        shuffles += 1
        banks = shuffle(banks)
        h = hash(banks)
        if h in seen:
            return shuffles, banks
        seen.add(h)


with open('input') as f:
    parts = re.split(r'\s+', f.readline().strip())
    banks = [int(i) for i in parts]


one, banks = repeat(banks)
two, _ = repeat(banks)

print('Part 1:', one)
print('Part 2:', two)