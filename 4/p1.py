valid = 0
for n in range(240920, 789857):
    d = [int(s) for s in str(n)]
    if sorted(d) == d and len(set(d)) < 6:
        valid += 1

print 'valid', valid
