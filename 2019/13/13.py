from intcode import Computer, parse_file


def run_to_output(program):
    outputs = []
    computer = Computer(program)
    done = False

    while not done:
        done = computer.iterate()
        if not done:
            outputs.append(computer.output)

    return outputs


def joystick(pad, ball):
    if pad > ball:
        return -1
    if ball > pad:
        return 1
    return 0


def run_with_screen(program):
    computer = Computer(program)
    pad = 0
    ball = 0
    done = False
    score = 0

    while not done:
        computer.next_input = lambda: joystick(pad, ball)

        computer.iterate()
        x = computer.output

        computer.iterate()
        y = computer.output

        done = computer.iterate()
        tile = computer.output

        if tile == 4:
            ball = x
        if tile == 3:
            pad = x

        if x == -1 and y == 0:
            score = tile

        if done:
            return score


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