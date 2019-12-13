import os
import sys


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


def wait_key():
    ''' Wait for a key press on the console and return it. '''
    result = None
    if os.name == 'nt':
        import msvcrt
        result = msvcrt.getch()
    else:
        import termios
        fd = sys.stdin.fileno()

        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)

        try:
            result = sys.stdin.read(1)
        except IOError:
            pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

    return result


def read_input():
    print('a, s, d')
    i = wait_key()
    if i == 'a':
        r = -1
    elif i == 'd':
        r = 1
    else:
        r = 0
    return r


def char(p):
    if p == 0:
        return ' '
    if p == 1:
        return 'W'
    if p == 2:
        return '#'
    if p == 3:
        return '='
    if p == 4:
        return 'O'


def draw_pixels(pixels):
    for y in range(0, 23):
        for x in range(0, 45):
            pixel = pixels.get((x, y), 0)

            print(char(pixel), end="")
        print()
    print('Score: ', pixels.get((-1, 0), 0))


def run_with_screen(program):
    pixels = {}
    t = {i: v for i, v in enumerate(program)}
    p = 0
    b = 0
    done = False

    while not done:
        t, p, x, b, done = run(
            t, p, b, read_input
        )
        t, p, y, b, done = run(
            t, p, b, read_input
        )
        t, p, tile, b, done = run(
            t, p, b, read_input
        )
        pixels[(x, y)] = tile
        draw_pixels(pixels)


program = parse_file('game.intcode')
program[0] = 2
run_with_screen(program)
