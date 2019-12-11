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
    b = 0
    t = {m: i for m, i in enumerate(program)}
    output = []
    while not done:
        t, p, o, b, done = run(t, p, b, input)
        if not done:
            output.append(o)
    return t, p, b, output


class inputter:
    def __init__(self, v):
        self.v = v

    def __getitem__(self, position):
        return self.v

    def pop(self, position):
        return self.v


def handle_turn(direction, turn):
    d = {
        'up': 0,
        'left': 1,
        'down': 2,
        'right': 3,
    }
    t = {
        1: 1,
        0: -1,
    }
    new = d[direction] + t[turn]

    d_reversed = {
        v: k for k, v in d.items()
    }
    new_direction = d_reversed[new % 4]

    deltas = {
        'up': (0, 1),
        'left': (-1, 0),
        'down': (0, -1),
        'right': (1, 0),
    }
    return new_direction, deltas[new_direction]


def add_points(a, b):
    return a[0] + b[0], a[1] + b[1]


def paint(program, initial):
    pixels = {}
    current = (0, 0)
    pixels[current] = initial
    direction = 'up'

    t = {m: i for m, i in enumerate(program)}

    t, p, color, b, done = run(
        t, 0, 0, inputter(pixels.get(current, 0))
    )
    t, p, turn, b, done = run(
        t, p, b, inputter(pixels.get(current, 0))
    )

    pixels[current] = color
    direction, (dx, dy) = handle_turn(direction, turn)
    current = add_points(current, (dx, dy))

    while True:
        t, p, color, b, done = run(
            t, p, b, inputter(pixels.get(current, 0))
        )
        t, p, turn, b, done = run(
            t, p, b, inputter(pixels.get(current, 0))
        )

        pixels[current] = color
        direction, (dx, dy) = handle_turn(direction, turn)
        current = add_points(current, (dx, dy))
        if done:
            break

    return pixels


def draw_image(pixels):
    im = {}
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0
    for (x, y), color in pixels.items():
        im[(x, y)] = '#' if color == 1 else ' '
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    for y in range(max_y+1, min_y-1, -1):
        print()
        for x in range(max_x+1, min_x-1, -1):
            pixel = im.get((x, y), " ")
            print(pixel, end="")


program = parse_file('input.intcode')
print("Part 1:", len(paint(program, 0)))

print("Part 2:")
draw_image(paint(program, 1))
