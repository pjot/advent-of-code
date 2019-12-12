with open('input.txt') as f:
    s = f.readline()

print("Part 1:", s.count("(") - s.count(")"))

floor = 0
for i, c in enumerate(s):
    if c == "(":
        floor += 1
    if c == ")":
        floor -= 1
    if floor == -1:
        print("Part 2:", i + 1)
        break