def handle_position(program, position):
    op_code = program[position]
    if op_code == 99:
        return program, -1

    a_pos = program[position + 1]
    a = program[a_pos]

    b_pos = program[position + 2]
    b = program[b_pos]

    c_pos = program[position + 3]

    if op_code == 1:
        program[c_pos] = a + b
    if op_code == 2:
        program[c_pos] = a * b

    return program, position + 4

def run_program(program):
    position = 0
    while position >= 0:
        program, position = handle_position(program, position)

    return program


def parse_file(filename):
    with open(filename) as f:
        code = f.readline()
        ints = code.split(',')
        program = [int(i) for i in ints]
        return program


program = parse_file('program.intcode')
program[1] = 12
program[2] = 2
result = run_program(program)

print result[0]
