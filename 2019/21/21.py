from intcode import Computer, parse_file


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
    for ch in o:
        if ch < 128:
            print(chr(ch), end='')
        else:
            print(ch)
    print()
    print()


walk = '''NOT A J
NOT J J
AND B J
AND C J
NOT J J
AND D J
WALK
'''

run = '''NOT A J
NOT J J
AND B J
AND C J
NOT J J
AND D J
NOT E T
NOT T T
OR H T
AND T J
RUN
'''


print("Part 1:")
run_sprintscript(walk)

print("Part 2:")
run_sprintscript(run)
