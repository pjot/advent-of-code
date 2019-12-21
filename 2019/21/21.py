from intcode import Computer, parse_file


walk = '''OR A J
AND B J
AND C J
NOT J J
AND D J
WALK
'''

run = '''OR A J
AND B J
AND C J
NOT J J
AND D J
OR E T
OR H T
AND T J
RUN
'''


class inputter:
    def __init__(self, inputs):
        self.inputs = inputs

    def next(self):
        n = self.inputs.pop(0)
        return n


def run_sprintscript(spring):
    program = parse_file('game.intcode')
    c = Computer(program)
    i = inputter([ord(c) for c in spring])
    c.next_input = i.next
    o = c.run_to_output()
    return o.pop()


print("Part 1:", run_sprintscript(walk))
print("Part 2:", run_sprintscript(run))
