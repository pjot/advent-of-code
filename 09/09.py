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
        int(full_instruction[0]),
    )


def run(tape, position, base, inputs):
    def read(delta=0, mode=1):
        try:
            if mode == 2:
                return tape[base + tape[position + delta]]
            if mode == 1:
                return tape[position + delta]
            if mode == 0:
                return tape[tape[position + delta]]
        except KeyError:
            return 0

    output = inputs[0]

    def write(delta, value, mode):
        if mode == 2:
            tape[base + tape[position + delta]] = value
        if mode == 1:
            tape[position + delta] = value
        if mode == 0:
            tape[tape[position + delta]] = value

    while True:
        instruction = read()
        op_code, mode_a, mode_b, mode_c = parse_instruction(instruction)

        if op_code == 99:
            return tape, position, output, base, True

        if op_code == 1:
            a = read(1, mode_a)
            b = read(2, mode_b)
            write(3, a + b, mode_c)
            position += 4

        if op_code == 2:
            a = read(1, mode_a)
            b = read(2, mode_b)
            write(3, a * b, mode_c)
            position += 4

        if op_code == 3:
            write(1, inputs.pop(0), mode_a)
            position += 2

        if op_code == 4:
            output = read(1, mode_a)
            position += 2
            return tape, position, output, base, False

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
            write(3, value, mode_c)
            position += 4

        if op_code == 8:
            a = read(1, mode_a)
            b = read(2, mode_b)
            value = 1 if a == b else 0
            write(3, value, mode_c)
            position += 4

        if op_code == 9:
            a = read(1, mode_a)
            base += a
            position += 2


def run_program(program, input):
    done = False
    p = 0
    base = 0
    t = {m: i for m, i in enumerate(program)}
    output = []
    while not done:
        t, p, o, base, done = run(t, p, base, input)
        if not done:
            output.append(o)
    return output


program = parse_file('input.intcode')
print("Part 1:", run_program(program, [1, 1]))
print("Part 2:", run_program(program, [2, 2]))