from itertools import permutations

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
    def __init__(self, memory, inputs):
        self.memory = memory
        self.position = 0
        self.inputs = inputs
        self.output = None

    def read(self, delta=0, mode=1):
        if mode == 1:
            return self.memory[self.position + delta]
        if mode == 0:
            return self.memory[self.memory[self.position + delta]]

    def write(self, delta, value):
        pos = self.read(delta)
        self.memory[pos] = value

def run_program(memory):
    while True:
        instruction = memory.read()
        op_code, mode_a, mode_b = parse_instruction(instruction)

        if op_code == 99:
            return memory.output, True

        if op_code == 1:
            a = memory.read(1, mode_a)
            b = memory.read(2, mode_b)
            memory.write(3, a + b)
            memory.position += 4

        if op_code == 2:
            a = memory.read(1, mode_a)
            b = memory.read(2, mode_b)
            memory.write(3, a * b)
            memory.position += 4

        if op_code == 3:
            memory.write(1, memory.inputs.pop(0))
            memory.position += 2

        if op_code == 4:
            memory.output = memory.read(1, mode_a)
            memory.position += 2
            return memory.output, False

        if op_code == 5:
            a = memory.read(1, mode_a)
            b = memory.read(2, mode_b)
            if a != 0:
                memory.position = b
            else:
                memory.position += 3

        if op_code == 6:
            a = memory.read(1, mode_a)
            b = memory.read(2, mode_b)
            if a == 0:
                memory.position = b
            else:
                memory.position += 3

        if op_code == 7:
            a = memory.read(1, mode_a)
            b = memory.read(2, mode_b)
            value = 1 if a < b else 0
            memory.write(3, value)
            memory.position += 4

        if op_code == 8:
            a = memory.read(1, mode_a)
            b = memory.read(2, mode_b)
            value = 1 if a == b else 0
            memory.write(3, value)
            memory.position += 4

def run_amps(program, phases):
    value = 0
    done = False
    amps = [Memory(program[:], [phase]) for phase in phases]
    while not done:
        for amp in amps:
            amp.inputs.append(value)
            value, done = run_program(amp)
    return value

def find_max(program, phases):
    max_value = 0
    max_phase = []
    for phases in permutations(phases):
        output = run_amps(program, phases)
        if output > max_value:
            max_value = output
            max_phase = phases

    return max_value

program = parse_file('input.amp')
print 'Part 1:', find_max(program, [0, 1, 2, 3, 4])

print 'Part 2:', find_max(program, [5, 6, 7, 8, 9])