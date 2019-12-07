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

class Machine:
    def __init__(self, program, phase):
        self.tape = program[:]
        self.position = 0
        self.inputs = [phase]
        self.output = None

    def read(self, delta=0, mode=1):
        if mode == 1:
            return self.tape[self.position + delta]
        if mode == 0:
            return self.tape[self.tape[self.position + delta]]

    def write(self, delta, value):
        pos = self.read(delta)
        self.tape[pos] = value

    def input(self):
        return self.inputs.pop(0)

    def run(self):
        while True:
            instruction = self.read()
            op_code, mode_a, mode_b = parse_instruction(instruction)

            if op_code == 99:
                return self.output, True

            if op_code == 1:
                a = self.read(1, mode_a)
                b = self.read(2, mode_b)
                self.write(3, a + b)
                self.position += 4

            if op_code == 2:
                a = self.read(1, mode_a)
                b = self.read(2, mode_b)
                self.write(3, a * b)
                self.position += 4

            if op_code == 3:
                self.write(1, self.input())
                self.position += 2

            if op_code == 4:
                self.output = self.read(1, mode_a)
                self.position += 2
                return self.output, False

            if op_code == 5:
                a = self.read(1, mode_a)
                b = self.read(2, mode_b)
                if a != 0:
                    self.position = b
                else:
                    self.position += 3

            if op_code == 6:
                a = self.read(1, mode_a)
                b = self.read(2, mode_b)
                if a == 0:
                    self.position = b
                else:
                    self.position += 3

            if op_code == 7:
                a = self.read(1, mode_a)
                b = self.read(2, mode_b)
                value = 1 if a < b else 0
                self.write(3, value)
                self.position += 4

            if op_code == 8:
                a = self.read(1, mode_a)
                b = self.read(2, mode_b)
                value = 1 if a == b else 0
                self.write(3, value)
                self.position += 4

def run_amps(program, phases):
    amps = [Machine(program, phase) for phase in phases]
    value = 0
    done = False
    while not done:
        for amp in amps:
            amp.inputs.append(value)
            value, done = amp.run()
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