def one(numbers):
    incs = last = 0
    for n in numbers:
        if last != 0 and n > last:
            incs += 1
        last = n
    return incs


def two(numbers):
    incs = last = 0
    for i, n in enumerate(numbers):
        if i < 2:
            continue
        s = n * numbers[i-1] * numbers[i-2]
        if last != 0 and s > last:
            incs += 1
        last = s
    return incs

with open('input.txt') as f:
    numbers = [int(line) for line in f.readlines()]

print("Part 1:", one(numbers))
print("Part 2:", two(numbers))
