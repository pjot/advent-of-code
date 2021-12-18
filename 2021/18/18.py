import itertools
import math

def parse_line(n):
    numbers = []
    level = 0
    current = None
    for c in n:
        if (c == ']' or c == ',') and current is not None:
            numbers.append((level, current))
            current = None

        if c == '[':
            level += 1

        if c == ']':
            level -= 1

        if c in '0123456789':
            current = int(c)

    return numbers

def parse(file):
    with open(file) as f:
        return [
            parse_line(line.strip())
            for line in f.readlines()
        ]

def add(a, b):
    aa = [(l+1, n) for l, n in a]
    bb = [(l+1, n) for l, n in b]
    return aa + bb

def explode(numbers):
    p = 0
    while p + 1 < len(numbers):
        level, left = numbers[p]
        next_level, right = numbers[p+1]
        if level == 5 and next_level == level:
            if p > 0:
                l, n = numbers[p-1]
                numbers[p-1] = (l, n+left)

            if p+2 < len(numbers):
                l, n = numbers[p+2]
                numbers[p+2] = (l, n+right)

            numbers[p] = (4, 0)
            numbers.pop(p+1)
            return numbers, False
        p += 1
    return numbers, True

def split(numbers):
    p = 0
    while p < len(numbers):
        level, n = numbers[p]
        if n > 9:
            lower = math.floor(n/2)
            higher = math.ceil(n/2)
            numbers.pop(p)
            numbers.insert(p, (level+1, higher))
            numbers.insert(p, (level+1, lower))
            return numbers, False
        p += 1
    return numbers, True

def iterate(numbers):
    numbers, done = explode(numbers)
    if not done:
        return numbers, False

    return split(numbers)

def full_reduce(numbers):
    done = False
    while not done:
        numbers, done = iterate(numbers)
    return numbers


def magnitude(numbers):
    while len(numbers) > 1:
        for i in range(len(numbers) - 1):
            a = numbers[i]
            b = numbers[i+1]
            if a[0] == b[0]:
                level = a[0]
                numbers[i] = (level-1, 3*a[1] + 2*b[1])
                numbers.pop(i+1)
                break
    return numbers[0][1]

def one(numbers):
    n = numbers[0]
    for r in numbers[1:]:
        n = add(n, r)
        n = full_reduce(n)

    return magnitude(n)

def magnitude_of_sum(a, b):
    n = add(a, b)
    n = full_reduce(n)
    return magnitude(n)

def two(numbers):
    highest = 0
    for a, b in itertools.permutations(numbers, 2):
        highest = max(highest, magnitude_of_sum(a, b))
    return highest


numbers = parse('input.txt')
print("Part 1:", one(numbers))
print("Part 2:", two(numbers))
