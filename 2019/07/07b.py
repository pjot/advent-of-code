from itertools import permutations


def parse_file(filename):
    with open(filename) as f:
        code = f.readline()
        ints = code.split(',')
        program = [int(i) for i in ints]
        return program


def parse_instruction(instruction):
    full_instruction = '{:05d}'.format(instruction)
    return (
        instruction % 100,
        int(full_instruction[2]),
        int(full_instruction[1]),
    )


def run(tape, position, inputs):
    def read(delta=0, mode=1):
        if mode == 1:
            return tape[position + delta]
        if mode == 0:
            return tape[tape[position + delta]]

    output = inputs[0]

    def write(pos, value):
        tape[read(pos)] = value

    while True:
        instruction = read()
        op_code, mode_a, mode_b = parse_instruction(instruction)

        if op_code == 99:
            return tape, position, output, True

        if op_code == 1:
            a = read(1, mode_a)
            b = read(2, mode_b)
            write(3, a + b)
            position += 4

        if op_code == 2:
            a = read(1, mode_a)
            b = read(2, mode_b)
            write(3, a * b)
            position += 4

        if op_code == 3:
            write(1, inputs.pop(0))
            position += 2

        if op_code == 4:
            output = read(1, mode_a)
            position += 2
            return tape, position, output, False

        if op_code == 5:
            a = read(1, mode_a)
            b = read(2, mode_b)
            if a != 0:
                position = b
            else:
                position += 3

        if op_code == 6:
            a = read(1, mode_a)
            b = read(2, mode_b)
            if a == 0:
                position = b
            else:
                position += 3

        if op_code == 7:
            a = read(1, mode_a)
            b = read(2, mode_b)
            value = 1 if a < b else 0
            write(3, value)
            position += 4

        if op_code == 8:
            a = read(1, mode_a)
            b = read(2, mode_b)
            value = 1 if a == b else 0
            write(3, value)
            position += 4


def run_amps(program, phases):
    a0, p0, o0, _ = run(program, 0, [phases[0], 0])
    a1, p1, o1, _ = run(program, 0, [phases[1], o0])
    a2, p2, o2, _ = run(program, 0, [phases[2], o1])
    a3, p3, o3, _ = run(program, 0, [phases[3], o2])
    a4, p4, o4, done = run(program, 0, [phases[4], o3])
    while not done:
        a0, p0, o0, _ = run(program, p0, [o4])
        a1, p1, o1, _ = run(program, p1, [o0])
        a2, p2, o2, _ = run(program, p2, [o1])
        a3, p3, o3, _ = run(program, p3, [o2])
        a4, p4, o4, done = run(program, p4, [o3])
    return o4


def find_max(program, phases):
    max_value = 0
    for phases in permutations(phases):
        output = run_amps(program, phases)
        if output > max_value:
            max_value = output

    return max_value


program = parse_file('input.amp')

print('Part 1:', find_max(program, [0, 1, 2, 3, 4]))
print('Part 2:', find_max(program, [5, 6, 7, 8, 9]))