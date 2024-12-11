from functools import cache

def parse(file: str) -> list[int]:
    with open(file) as f:
        line = f.readlines()[0].strip()
        return [int(n) for n in line.split()]

@cache
def iterate(stone: int) -> list[int]:
    if stone == 0:
        return [1]

    if len(str(stone)) % 2 == 0:
        s = str(stone)
        middle = len(s) // 2
        return [int(n) for n in [s[:middle], s[middle:]]]

    return [stone * 2024]

@cache
def blink(stone: int, blinks: int) -> int:
    if blinks == 1:
        return len(iterate(stone))

    return sum(blink(s, blinks - 1) for s in iterate(stone))

def solve(stones: list[int], blinks: int) -> int:
    return sum(blink(stone, blinks) for stone in stones)

stones = parse("input")
print("Part 1:", solve(stones, 25))
print("Part 2:", solve(stones, 75))
