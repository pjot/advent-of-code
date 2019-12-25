def parse_file(file):
    with open(file) as f:
        return [
            s.strip() for s in f.readlines()
        ]


def find_code(instructions, keypad):
    x, y = 1, 1
    code = ""
    for instruction in instructions:
        for d in instruction:
            if d == 'U':
                y -= 1
                if keypad.get((x, y)) is None:
                    y += 1
            if d == 'D':
                y += 1
                if keypad.get((x, y)) is None:
                    y -= 1
            if d == 'L':
                x -= 1
                if keypad.get((x, y)) is None:
                    x += 1
            if d == 'R':
                x += 1
                if keypad.get((x, y)) is None:
                    x -= 1
        code += keypad[x, y]
    return code


one = {
    (0, 0): '1', (1, 0): '2', (2, 0): '3',
    (0, 1): '4', (1, 1): '5', (2, 1): '6',
    (0, 2): '7', (1, 2): '8', (2, 2): '9',
}
two = {
                              (2, 0): '1',
                 (1, 1): '2', (2, 1): '3', (3, 1): '4',
    (0, 2): '5', (1, 2): '6', (2, 2): '7', (3, 2): '8', (4, 2): '9',
                 (1, 3): 'A', (2, 3): 'B', (3, 3): 'C',
                              (2, 4): 'D',
}

instructions = parse_file("input.txt")
print("Part 1:", find_code(instructions, one))
print("Part 2:", find_code(instructions, two))