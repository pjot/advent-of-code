def get_instructions():
    instructions = []
    with open('input2') as f:
        for l in f.readlines():
            instructions.append(l.strip().split(' '))
    return {
        i: v for i, v in enumerate(instructions)
    }


def run(program, registers):
    pos = 0
    i = 0
    while True:
        i += 1
        if pos >= len(program):
            return registers['a']
        p = program[pos]

        if p[0] == 'mul':
            a = registers[p[1]]
            b = registers[p[2]]
            registers[p[3]] = a * b
            pos += 1
        if p[0] == 'nop':
            pos += 1
        elif p[0] == 'tgl':
            c = registers[p[1]]
            toggle = program.get(pos + c)
            if toggle is None:
                pos += 1
                continue
            t = toggle[0]
            if t == 'inc':
                toggle[0] = 'dec'
            if t == 'dec' or t == 'tgl':
                toggle[0] = 'inc'
            if t == 'jnz':
                toggle[0] = 'cpy'
            if t == 'cpy':
                toggle[0] = 'jnz'
            program[pos + c] = toggle
            pos += 1
            
        elif p[0] == 'cpy':
            if p[1] in 'abcd':
                v = registers[p[1]]
            else:
                v = int(p[1])
            registers[p[2]] = v
            pos += 1

        elif p[0] == 'inc':
            registers[p[1]] += 1
            pos += 1

        elif p[0] == 'dec':
            registers[p[1]] -= 1
            pos += 1

        elif p[0] == 'jnz':
            if p[1] in 'abcd':
                v = registers[p[1]]
            else:
                v = int(p[1])
            if v != 0:
                if p[2] in 'abcd':
                    pp = registers[p[2]]
                else:
                    pp = int(p[2])
                pos += pp
            else:
                pos += 1

registers = {
    'a': 7,
    'b': 0,
    'c': 0,
    'd': 0,
}
print('Part 1:', run(get_instructions(), registers))

registers = {
    'a': 12,
    'b': 0,
    'c': 0,
    'd': 0,
}
print('Part 2:', run(get_instructions(), registers))
