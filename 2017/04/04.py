from collections import Counter

def valid(pw):
    parts = pw.split(' ')
    c = Counter(parts)
    return max(c.values()) == 1

def unique_valid(pw):
    parts = pw.split(' ')
    c = Counter(''.join(sorted(i)) for i in parts)
    return max(c.values()) == 1

def count_valid(phrases):
    return len([c for c in phrases if valid(c)])

def count_unique_valid(phrases):
    return len([c for c in phrases if unique_valid(c)])

phrases = []
with open('input') as f:
    for line in f.readlines():
        phrases.append(line.strip())

print('Part 1:', count_valid(phrases))
print('Part 2:', count_unique_valid(phrases))