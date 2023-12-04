from collections import defaultdict

def numbers(ns):
    return set(int(n.strip()) for n in ns.split())

def parse(line):
    p = line.strip().split()
    card = int(p[1].strip(":"))

    l = " ".join(p[2:])
    winning, mine = [numbers(c) for c in l.split("|")]

    return card, winning, mine

points = 0
copies = defaultdict(lambda: 1)

with open("input") as f:
    for line in f.readlines():
        card, winning, mine = parse(line)
        matches = len(winning & mine)

        if copies.get(card) is None:
            copies[card] = 1

        if matches:
            points += 2 ** (matches - 1)

            for i in range(matches):
                copies[card + i + 1] += copies[card]

print("Part 1:", points)
print("Part 2:", sum(copies.values()))
