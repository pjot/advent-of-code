from itertools import combinations

with open('input.txt') as f:
    numbers = [int(i) for i in f.readlines()]

def is_sum(n, nums):
    for a, b in combinations(nums, 2):
        if a + b == n:
            return True
    return False

def first_fail(numbers, preamble):
    for i, n in enumerate(numbers):
        if i < preamble:
            continue

        nums = numbers[i-preamble:i]
        if not is_sum(n, nums):
            return n

def find_weakness(numbers, invalid):
    for a, _ in enumerate(numbers):
        for b in range(2, 100):
            nums = numbers[a:a+b]
            nums_sum = sum(nums)

            if nums_sum == invalid:
                return min(nums) + max(nums)
            if nums_sum > invalid:
                break

one = first_fail(numbers, 25)
print('Part 1:', one)

two = find_weakness(numbers, one)
print('Part 2:', two)
