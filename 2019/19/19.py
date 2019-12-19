import functools
from intcode import parse_file, Computer


class inputter:
    def __init__(self, inputs):
        self.inputs = inputs

    def next(self):
        return self.inputs.pop(0)


@functools.lru_cache(2**40)
def check(x, y):
    inputs = inputter([x, y])
    computer = Computer(parse_file('input.intcode'))
    computer.next_input = inputs.next
    computer.iterate()
    return computer.output == 1


affected = 0
for y in range(30):
    for x in range(50):
        if check(x, y):
            affected += 1

print('Part 1:', affected)

current = (0, 0)


def find_edge(x, y):
    found = False
    while not found:
        if check(x, y):
            return x
        x += 1


def fits(x, y, size):
    for xx in range(x, x + size):
        for yy in range(y - size + 1, y + 1):
            if not check(xx, yy):
                return False

    return True


def find_fit(size):
    x, y = (size, size)
    while True:
        x = find_edge(x, y)
        if check(x + size - 1, y - size + 1):
            return x, y - size + 1
        y += 1


x, y = find_fit(100)
print('Part 2:', x * 10000 + y)