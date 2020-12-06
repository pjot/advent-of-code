from collections import Counter

with open('input.txt') as f:
    one = 0
    two = 0
    for group in f.read().split('\n\n'):
        group = group.strip()
        letters = set(group)
        letters.discard('\n')
        
        seen = Counter()
        for person in group.split():
            for c in person:
                seen[c] += 1

        one += len(letters)
        two += len([
            k for k, v in seen.items()
            if v == group.count('\n') + 1
        ])

print('Part 1:', one)
print('Part 2:', two)

