instructions = []
with open('input') as f:
    for l in f.readlines():
        instructions.append(l.strip())


def run(program, registers):
    pos = 0
    while True:
        if pos >= len(program):
            return registers['a']

        p = program[pos].split(' ')

        if p[0] == 'cpy':
            if p[1] in 'abcd':
                v = registers[p[1]]
            else:
                v = int(p[1])
            registers[p[2]] = v
            pos += 1

        if p[0] == 'inc':
            registers[p[1]] += 1
            pos += 1

        if p[0] == 'dec':
            registers[p[1]] -= 1
            pos += 1

        if p[0] == 'jnz':
            if p[1] in 'abcd':
                v = registers[p[1]]
            else:
                v = int(p[1])
            if v != 0:
                pos += int(p[2])
            else:
                pos += 1

registers = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
}
print('Part 1:', run(instructions, registers))

registers = {
    'a': 0,
    'b': 0,
    'c': 1,
    'd': 0,
}
print('Part 2:', run(instructions, registers))
