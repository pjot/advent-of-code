from collections import deque

def parse(file):
    numbers = []
    with open(file) as f:
        for i, line in enumerate(f.readlines()):
            n = int(line.strip())
            numbers.append((i, n))
    return numbers

def mix(numbers, iterations=1):
    file = deque(numbers)
    for _ in range(iterations):
        for i, n in numbers:
            position = file.index((i, n))
            file.rotate(-position)
            file.popleft()
            file.rotate(-n)
            file.appendleft((i, n))
    return file

def grove_coordinates(file):
    file = [n for _, n in file]

    l = len(file)
    i = file.index(0)

    a = file[(i + 1000) % l]
    b = file[(i + 2000) % l]
    c = file[(i + 3000) % l]

    return a + b + c

numbers = parse("input.txt")

f = mix(numbers)
print("Part 1:", grove_coordinates(f))

key = 811589153
decrypted = [(i, n * key) for i, n in numbers]
f = mix(decrypted, iterations=10)
print("Part 2:", grove_coordinates(f))

