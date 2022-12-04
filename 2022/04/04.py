def to_set(section):
    a, b = section.split('-')
    r = range(int(a), int(b) + 1)
    return set(r)

one = 0
two = 0
with open("input.txt") as f:
    for line in f.readlines():
        line = line.strip()

        a, b = (to_set(s) for s in line.split(','))

        if a >= b or b >= a:
            one += 1

        if len(a & b) > 0:
            two += 1

print("Part 1:", one)
print("Part 2:", two)

