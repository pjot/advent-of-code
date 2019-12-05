def parse_file(filename):
    with open(filename) as f:
        code = f.readline()
        ints = code.split(',')
        program = [int(i) for i in ints]
        return program

def digit(instruction, place):
    code_map = '{:05d}'.format(instruction)
    return int(code_map[place])

def read(memory, position, mode):
    if mode == 1:
        return memory[position]
    if mode == 0:
        return memory[memory[position]]

def write(memory, position, value):
    memory[memory[position]] = value

def run_program(memory, program_input):
    position = 0
    output = None

    while True:
        code = memory[position]
        mode_a = digit(code, 2)
        mode_b = digit(code, 1)
        op_code = code % 100

        if op_code == 99:
            return output

        if op_code == 1:
            a = read(memory, position + 1, mode_a)
            b = read(memory, position + 2, mode_b)
            write(memory, position + 3, a + b)
            position += 4

        if op_code == 2:
            a = read(memory, position + 1, mode_a)
            b = read(memory, position + 2, mode_b)
            write(memory, position + 3, a * b)
            position += 4

        if op_code == 3:
            write(memory, position + 1, program_input)
            position += 2

        if op_code == 4:
            output = read(memory, position + 1, mode_a)
            position += 2

        if op_code == 5:
            a = read(memory, position + 1, mode_a)
            b = read(memory, position + 2, mode_b)
            if a != 0:
                position = b
            else:
                position += 3

        if op_code == 6:
            a = read(memory, position + 1, mode_a)
            b = read(memory, position + 2, mode_b)
            if a == 0:
                position = b
            else:
                position += 3

        if op_code == 7:
            a = read(memory, position + 1, mode_a)
            b = read(memory, position + 2, mode_b)
            if a < b:
                write(memory, position + 3, 1)
            else:
                write(memory, position + 3, 0)
            position += 4

        if op_code == 8:
            a = read(memory, position + 1, mode_a)
            b = read(memory, position + 2, mode_b)
            if a == b:
                write(memory, position + 3, 1)
            else:
                write(memory, position + 3, 0)
            position += 4


    return output

program = parse_file('program.testcode')
print run_program(program, 5)
