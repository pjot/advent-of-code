def find_unique(buffer, length):
    for pos in range(length, len(buffer)):
        candidate = buffer[pos-length:pos]
        if len(set(candidate)) == length:
            return pos

with open("input.txt") as f:
    buffer = f.read().strip()

print("Part 1:", find_unique(buffer, 4))
print("Part 2:", find_unique(buffer, 14))
