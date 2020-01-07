from collections import defaultdict


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
        self.inputs = []
        self.sent = 0
        self.waiting = False
        self.last_recv = None

    def get(self, v):
        if v in self.registers:
            return self.registers.get(v, 0)
        return int(v)

    def run(self):
        while True:
            k, *rest = self.program[self.pos].split()

            if k == 'snd':
                self.pos += 1
                self.sent += 1
                return self.get(rest[0])
            elif k == 'set':
                a, b = rest
                self.registers[a] = self.get(b)
                self.pos += 1
            elif k == 'add':
                a, b = rest
                self.registers[a] += self.get(b)
                self.pos += 1
            elif k == 'mul':
                a, b = rest
                self.registers[a] *= self.get(b)
                self.pos += 1
            elif k == 'mod':
                a, b = rest
                self.registers[a] %= self.get(b)
                self.pos += 1
            elif k == 'rcv':
                if len(self.inputs) > 0:
                    self.waiting = False
                    self.last_recv = self.inputs.pop(0)
                    self.registers[rest[0]] = self.last_recv
                    self.pos += 1
                else:
                    self.waiting = True
                    return
            elif k == 'jgz':
                a, b = rest
                if self.get(a) > 0:
                    self.pos += self.get(b)
                else:
                    self.pos += 1


def one():
    c = Computer(parse('input'))
    while c.last_recv is None:
        o = c.run()
        c.inputs = [o]
    return c.last_recv


def two():
    a = Computer(parse('input'))
    b = Computer(parse('input'))
    a.registers['p'] = 0 
    b.registers['p'] = 1 

    while True:
        o1 = a.run()
        if o1 is not None:
            b.inputs.append(o1)

        o2 = b.run() 
        if o2 is not None:
            a.inputs.append(o2)

        if a.waiting and b.waiting and len(a.inputs) == 0 and len(b.inputs) == 0:
            return a, b

print('Part 1:', one())

a, b = two()
print('Part 2:', b.sent)
