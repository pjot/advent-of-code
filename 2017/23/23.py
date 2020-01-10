
def parse(file):
    p = {}
    with open(file) as f:
        for i, line in enumerate(f.readlines()):
            p[i] = line.strip()
    return p

class Computer:
    def __init__(self, program):
        self.program = program
        self.pos = 0
        self.registers = {
            k: 0 for k in 'abcdefghijklmnopqrstuvxyz'
        }
        self.muls = 0
        self.debug = False

    def get(self, v):
        if v in self.registers:
            return self.registers.get(v, 0)
        return int(v)

    def run(self):
        while True:
            if self.pos not in self.program:
                return
            k, *rest = self.program[self.pos].split()

            if k == 'set':
                a, b = rest
                self.registers[a] = self.get(b)
                self.pos += 1
            elif k == 'sub':
                a, b = rest
                self.registers[a] -= self.get(b)
                self.pos += 1
            elif k == 'mul':
                a, b = rest
                self.registers[a] *= self.get(b)
                self.pos += 1
                self.muls += 1
            elif k == 'jnz':
                a, b = rest
                if self.get(a) == 0:
                    self.pos += 1
                else:
                    self.pos += self.get(b)

            if self.debug:
                print(self.pos + 1)



def one():
    c = Computer(parse('input'))
    c.run()
    return c.muls


def two():
    c = Computer(parse('input2'))
    c.debug = True
    c.registers['a'] = 1
    c.run()
    return c.registers['h']

print('Part 1:', one())
print('Part 2:', two())