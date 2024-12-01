left, right = [], []
with open("input") as f:
    for line in f.readlines():
        a, b = [int(n) for n in line.split()]
        left.append(a)
        right.append(b)

distance = 0
for a, b in zip(sorted(left), sorted(right)):
    distance += max(a, b) - min(a, b)
print("Part 1:", distance)

similarity = 0
for a in left:
    similarity += a * right.count(a)
print("Part 2:", similarity)
