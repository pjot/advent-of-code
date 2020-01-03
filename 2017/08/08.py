def parse(file):
    program = []
    with open(file) as f:
        for line in f.readlines():
            program.append(line.strip())
    return program


registers = {}
highest_value = 0
for line in parse('input'):
    p = line.split(' ')

    target = p[0]
    action = p[1]
    amount = int(p[2])
    a = registers.get(p[4], 0)
    comp = p[5]
    b = int(p[6])

    if comp == '>':
        cond = a > b
    elif comp == '<':
        cond = a < b
    elif comp == '>=':
        cond = a >= b
    elif comp == '==':
        cond = a == b
    elif comp == '<=':
        cond = a <= b
    elif comp == '!=':
        cond = a != b

    if cond:
        if action == 'inc':
            registers[target] = registers.get(target, 0) + amount
        elif action == 'dec':
            registers[target] = registers.get(target, 0) - amount

    highest_value = max(highest_value, max(registers.values()))


print('Part 1:', max(registers.values()))
print('Part 2:', highest_value)



