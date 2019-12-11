from functools import reduce


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

    output = next(inputs)

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
            write(1, next(inputs), mode_a)
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


def inputter(v):
    while True:
        yield v


def handle_turn(direction, turn):
    new = (direction + (turn * 2) - 1) % 4
    deltas = {
        0: (0, 1),
        1: (-1, 0),
        2: (0, -1),
        3: (1, 0),
    }
    return new, deltas[new]


def add_points(a, b):
    return a[0] + b[0], a[1] + b[1]


def one_iteration(t, p, b, i):
    t, p, color, b, done = run(t, p, b, inputter(i))
    t, p, turn, b, done = run(t, p, b, inputter(i))

    return t, p, b, turn, color, done


def paint(program, initial):
    pixels = {}
    current = (0, 0)
    pixels[current] = initial
    direction = 0

    t = {m: i for m, i in enumerate(program)}

    t, p, b, turn, color, _ = one_iteration(
        t, 0, 0, pixels.get(current, 0)
    )

    pixels[current] = color
    direction, (dx, dy) = handle_turn(direction, turn)
    current = add_points(current, (dx, dy))

    while True:
        t, p, b, turn, color, done = one_iteration(
            t, p, b, pixels.get(current, 0)
        )

        pixels[current] = color
        direction, (dx, dy) = handle_turn(direction, turn)
        current = add_points(current, (dx, dy))
        if done:
            break

    return pixels


def min_max(coords):
    return reduce(
        lambda acc, c: (
            min(c, acc[0]),
            max(c, acc[1])
        ),
        coords,
        (0, 0)
    )


def draw_image(pixels):
    im = {}
    for (x, y), color in pixels.items():
        im[(x, y)] = '#' if color == 1 else ' '

    min_x, max_x = min_max([c[0] for c in pixels.keys()])
    min_y, max_y = min_max([c[1] for c in pixels.keys()])

    for y in range(max_y, min_y - 1, -1):
        for x in range(max_x, min_x - 1, -1):
            pixel = im.get((x, y), " ")
            print(pixel, end="")
        print()


program = parse_file('input.intcode')
print("Part 1:", len(paint(program, 0)))

print("Part 2:")
draw_image(paint(program, 1))
