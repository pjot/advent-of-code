def is_valid(n):
    l = [int(j) for j in str(n)]
    if l != sorted(l):
        return False

    for digit in l:
        if l.count(digit) == 2:
            return True

valid = 0
for n in range(240920, 789957):
    if is_valid(n):
        valid += 1

print "valid", valid
