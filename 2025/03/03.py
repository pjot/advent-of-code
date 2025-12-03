import math

def digits(n: int) -> int:
    if n == 0:
        return 0
    return math.ceil(math.log10(n))

def biggest(batteries: str, n: int) -> int:
    l = len(batteries)
    p = joltage = 0
    while digits(joltage) < n:
        left = len(batteries) + digits(joltage) - n
        next_digit = max(batteries[p:left + 1])
        p = batteries.index(next_digit, p) + 1

        joltage *= 10
        joltage += int(next_digit)

    return joltage

one = two = 0
with open("input") as f:
    for batteries in f.read().splitlines():
        one += biggest(batteries, 2)
        two += biggest(batteries, 12)

print("Part 1:", one)
print("Part 2:", two)
