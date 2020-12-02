passwords = []
with open("input.txt") as f:
    for line in f.readlines():
        policy, letter, pw = line.strip().split(' ')
        a, b = policy.split('-')
        letter = letter[0]
        passwords.append((int(a), int(b), letter, pw))

one = 0
two = 0
for a, b, letter, pw in passwords:
    if a <= pw.count(letter) <= b:
        one += 1
    if (pw[a-1] == letter) ^ (pw[b-1] == letter):
        two += 1

print('Part 1:', one)
print('Part 2:', two)
