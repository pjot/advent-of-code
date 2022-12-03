one = 0
two = 0

def priority(c):
    if c.islower():
        return ord(c) - 96
    return ord(c) - 38

with open("input.txt") as f:
    lines = [l.strip() for l in f.readlines()]

    for l in lines:
        half = int(len(l) / 2)
        a, b = set(l[:half]), set(l[-half:])

        c = (a & b).pop()
        one += priority(c)

    lines = [set(l) for l in lines]
    while lines:
        a, b, c = lines.pop(), lines.pop(), lines.pop()
        s = ((a & b) & c).pop()
        two += priority(s)

print("Part 1:", one)
print("Part 2:", two)
