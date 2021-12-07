def parse(file):
    with open(file) as f:
        return [int(i) for i in f.readline().strip().split(',')]

def check(crabs, position, distance, limit=None):
    steps = 0
    for c in crabs:
        steps += distance(c, position)
        if limit and steps > limit:
            return
    return steps

def delta(current, position):
    return abs(current - position)

def sum_up_to(n):
    return int(n * (1 + n) / 2)

def sum_up_to_delta(current, position):
    return sum_up_to(delta(current, position))

crabs = parse('input.txt')

one = two = None
for position in range(len(crabs)):
    new_one = check(crabs, position, delta, one)
    new_two = check(crabs, position, sum_up_to_delta, two)
    if new_one:
        one = new_one
    if new_two:
        two = new_two

print("Part 1:", one)
print("Part 2:", two)
