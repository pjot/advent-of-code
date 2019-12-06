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
    )

class Memory:
    def __init__(self, memory):
        self.memory = memory

    def read(self, position, mode=1):
        if mode == 1:
            return self.memory[position]
        if mode == 0:
            return self.memory[self.memory[position]]

    def write(self, position, value):
        pos = self.read(position)
        self.memory[pos] = value

def run_program(memory, program_input):
    position = 0
    output = None

    while True:
        instruction = memory.read(position)
        op_code, mode_a, mode_b = parse_instruction(instruction)

        if op_code == 99:
            return output

        if op_code == 1:
            a = memory.read(position + 1, mode_a)
            b = memory.read(position + 2, mode_b)
            memory.write(position + 3, a + b)
            position += 4

        if op_code == 2:
            a = memory.read(position + 1, mode_a)
            b = memory.read(position + 2, mode_b)
            memory.write(position + 3, a * b)
            position += 4

        if op_code == 3:
            memory.write(position + 1, program_input)
            position += 2

        if op_code == 4:
            output = memory.read(position + 1, mode_a)
            position += 2

        if op_code == 5:
            a = memory.read(position + 1, mode_a)
            b = memory.read(position + 2, mode_b)
            if a != 0:
                position = b
            else:
                position += 3

        if op_code == 6:
            a = memory.read(position + 1, mode_a)
            b = memory.read(position + 2, mode_b)
            if a == 0:
                position = b
            else:
                position += 3

        if op_code == 7:
            a = memory.read(position + 1, mode_a)
            b = memory.read(position + 2, mode_b)
            value = 1 if a < b else 0
            memory.write(position + 3, value)
            position += 4

        if op_code == 8:
            a = memory.read(position + 1, mode_a)
            b = memory.read(position + 2, mode_b)
            value = 1 if a == b else 0
            memory.write(position + 3, value)
            position += 4

    return output

program = parse_file('program.testcode')
print "Part 1:", run_program(Memory(program), 1)

program = parse_file('program.testcode')
print "Part 2:", run_program(Memory(program), 5)
