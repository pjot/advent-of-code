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


def run(tape, position, base, next_input):
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

    output = None

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
            write(1, next_input(), mode_a)
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


def run_to_output(program):
    output = []
    t = {i: v for i, v in enumerate(program)}
    p = 0
    b = 0
    done = False

    while not done:
        t, p, o, b, done = run(
            t, p, b, lambda: 0
        )
        if not done:
            output.append(o)

    return output


def joystick(pad, ball):
    if pad > ball:
        return -1
    if ball > pad:
        return 1
    return 0


def run_with_screen(program):
    pixels = {}
    t = {i: v for i, v in enumerate(program)}
    p = 0
    b = 0
    pad = 0
    ball = 0
    done = False

    while not done:
        t, p, x, b, done = run(
            t, p, b, lambda: joystick(pad, ball)
        )
        t, p, y, b, done = run(
            t, p, b, lambda: joystick(pad, ball)
        )
        t, p, tile, b, done = run(
            t, p, b, lambda: joystick(pad, ball)
        )
        if tile == 4:
            ball = x
        if tile == 3:
            pad = x

        pixels[(x, y)] = tile
        if done:
            return pixels.get((-1, 0), 0)


program = parse_file('game.intcode')
outputs = run_to_output(program)
blocks = 0
for i, v in enumerate(outputs):
    if (i + 1) % 3 == 0:
        if v == 2:
            blocks += 1
print("Part 1:", blocks)

program[0] = 2
print("Part 2:", run_with_screen(program))