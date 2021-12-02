instructions = []
with open('input.txt') as f:
    for line in f.readlines():
        instruction, delta = line.split(' ')
        instructions.append((instruction, int(delta)))

def one(instructions):
    horizontal = depth = 0
    for instruction, delta in instructions:
        if instruction == 'forward':
            horizontal += delta
        if instruction == 'up':
            depth -= delta
        if instruction == 'down':
            depth += delta

    return horizontal * depth

def two(instructions):
    horizontal = depth = aim = 0
    for instruction, delta in instructions:
        if instruction == 'forward':
            horizontal += delta
            depth += delta * aim
        if instruction == 'up':
            aim -= delta
        if instruction == 'down':
            aim += delta
    return horizontal * depth

print("Part 1:", one(instructions))
print("Part 2:", two(instructions))
