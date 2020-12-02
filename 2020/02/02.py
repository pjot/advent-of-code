import re

PATTERN = re.compile(r'(\d+)-(\d+) ([a-z]): ([a-z]+)')

def parse(line):
    a, b, letter, pw = re.match(PATTERN, line).groups()
    return int(a), int(b), letter, pw

with open('input.txt') as f:
    passwords = [parse(line) for line in f.readlines()]

one = 0
two = 0
for a, b, letter, pw in passwords:
    if a <= pw.count(letter) <= b:
        one += 1
    if (pw[a - 1] == letter) ^ (pw[b - 1] == letter):
        two += 1

print('Part 1:', one)
print('Part 2:', two)
