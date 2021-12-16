from collections import Counter

rules = {}
pairs = Counter()
with open('input.txt') as f:
    a, b = '', ''
    for c in f.readline().strip():
        a, b = b, c
        if len(a + b) == 2:
            pairs[a + b] += 1

    f.readline()

    for line in f.readlines():
        pair, insert = line.strip().split(' -> ')
        rules[pair] = insert


def answer(pairs):
    counts = Counter()
    for pair, count in pairs.items():
        a, b = list(pair)
        counts[a] += count
        counts[b] += count
    counts = {k: int(v / 2) for k, v in counts.items()}

    most = 0
    least = float('inf')
    for value in counts.values():
        most = max(most, value)
        least = min(least, value)

    return most - least

def iterate(pairs, rules):
    new_pairs = Counter()
    for pair, count in pairs.items():
        if insert := rules.get(pair):
            a, b = list(pair)
            new_pairs[a + insert] += count
            new_pairs[insert + b] += count
    return new_pairs

for step in range(1, 41):
    pairs = iterate(pairs, rules)
    if step == 10:
        print("Part 1:", answer(pairs))

print("Part 2:", answer(pairs))

