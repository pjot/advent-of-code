from functools import cache

with open("input") as f:
    line = f.readlines()[0].strip()
    stones = tuple(int(n) for n in line.split())

@cache
def iterate(stone):
    if stone == 0:
        return [1]

    if len(str(stone)) % 2 == 0:
        s = str(stone)
        middle = len(s) // 2
        return [int(n) for n in [s[:middle], s[middle:]]]

    return [stone * 2024]

@cache
def blink(stone, blinks):
    if blinks == 1:
        return len(iterate(stone))
    ss = 0
    for s in iterate(stone):
        ss += blink(s, blinks - 1)
    return ss

def solve(stones, blinks):
    s = 0
    for stone in stones:
        s += blink(stone, blinks)
    return s

print("Part 1:", solve(stones, 25))
print("Part 2:", solve(stones, 75))
