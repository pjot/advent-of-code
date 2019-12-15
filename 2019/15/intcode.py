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


class Computer:
    def __init__(self, program, next_input=None):
        self.position = 0
        self.base = 0
        self.next_input = next_input
        self.tape = {k: v for k, v in enumerate(program)}
        self.output = 0

    def run_with_input(self, input):
        self.next_input = lambda: input
        self.iterate()
        return self.output

    def run_to_output(self):
        done = False
        outputs = []
        while not done:
            done = self.iterate()
            if not done:
                outputs.append(self.output)

        return outputs

    def read(self, delta=0, mode=1):
        if mode == 2:
            return self.tape.get(
                self.base + self.tape.get(self.position + delta, 0),
                0
            )
        if mode == 1:
            return self.tape.get(self.position + delta, 0)
        if mode == 0:
            return self.tape.get(
                self.tape.get(self.position + delta, 0),
                0
            )

    def write(self, delta, value, mode):
        if mode == 2:
            key = self.base + self.tape[self.position + delta]
        if mode == 1:
            key = self.position + delta
        if mode == 0:
            key = self.tape[self.position + delta]

        self.tape[key] = value

    def iterate(self):
        while True:
            instruction = self.read()
            op_code, mode_a, mode_b, mode_c = parse_instruction(instruction)

            if op_code == 99:
                return True

            if op_code == 1:
                a = self.read(1, mode_a)
                b = self.read(2, mode_b)
                self.write(3, a + b, mode_c)
                self.position += 4

            if op_code == 2:
                a = self.read(1, mode_a)
                b = self.read(2, mode_b)
                self.write(3, a * b, mode_c)
                self.position += 4

            if op_code == 3:
                self.write(1, self.next_input(), mode_a)
                self.position += 2

            if op_code == 4:
                self.output = self.read(1, mode_a)
                self.position += 2
                return False

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
                self.write(3, value, mode_c)
                self.position += 4

            if op_code == 8:
                a = self.read(1, mode_a)
                b = self.read(2, mode_b)
                value = 1 if a == b else 0
                self.write(3, value, mode_c)
                self.position += 4

            if op_code == 9:
                a = self.read(1, mode_a)
                self.base += a
                self.position += 2

