current = 0
elfs = []

with open("input.txt") as f:
    for line in f.readlines():
        l = line.strip()
        if l == "":
            elfs.append(current)
            current = 0
        else:
            current += int(l)

elfs.sort(reverse=True)

print("Part 1:", elfs[0])
print("Part 2:", sum(elfs[:3]))

