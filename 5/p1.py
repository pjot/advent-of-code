def parse_file(filename):
    with open(filename) as f:
        code = f.readline()
        ints = code.split(',')
        program = [int(i) for i in ints]
        return program

def digit(instruction, place):
    code_map = '{:05d}'.format(instruction)
    return int(code_map[place])

def read(data, position, mode):
    if mode == 1:
        return data[position]
    if mode == 0:
        return data[data[position]]

def write(data, position, value):
    data[data[position]] = value

def run_program(data, program_input):
    position = 0
    output = None

    while True:
        code = data[position]
        mode_a = digit(code, 2)
        mode_b = digit(code, 1)
        op_code = code % 100

        if op_code == 99:
            return output

        if op_code == 1:
            a = read(data, position + 1, mode_a)
            b = read(data, position + 2, mode_b)
            write(data, position + 3, a + b)
            position += 4

        if op_code == 2:
            a = read(data, position + 1, mode_a)
            b = read(data, position + 2, mode_b)
            write(data, position + 3, a * b)
            position += 4

        if op_code == 3:
            write(data, position + 1, program_input)
            position += 2

        if op_code == 4:
            output = read(data, position + 1, mode_a)
            position += 2

    return output

program = parse_file('program.testcode')
print run_program(program, 1)
