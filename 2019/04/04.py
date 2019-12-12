def is_valid_first(n):
    digits = [int(j) for j in str(n)]
    if digits != sorted(digits):
        return False

    for digit in digits:
        if digits.count(digit) > 1:
            return True


def is_valid_second(n):
    digits = [int(j) for j in str(n)]
    if digits != sorted(digits):
        return False

    for digit in digits:
        if digits.count(digit) == 2:
            return True


valid_first = 0
valid_second = 0
for n in range(240920, 789957):
    if is_valid_first(n):
        valid_first += 1
    if is_valid_second(n):
        valid_second += 1

print("Part 1:", valid_first)
print("Part 2:", valid_second)
