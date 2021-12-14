from collections import Counter

rules = {}
with open('input.txt') as f:
    polymer = f.readline().strip()
    f.readline()
    for line in f.readlines():
        pair, insert = line.strip().split(' -> ')
        rules[(pair[0], pair[1])] = insert

for step in range(1, 41):
    print(step)
    p = a = b = ''
    for c in polymer:
        a, b = b, c

        if (a, b) in rules:
            p += a + rules[(a, b)]

    polymer = p + b
    #print(step, polymer)

counts = Counter(polymer)
most_common = 0
least_common = float('inf')
for c, v in counts.items():
    most_common = max(most_common, v)
    least_common = min(least_common, v)

print(most_common - least_common)
