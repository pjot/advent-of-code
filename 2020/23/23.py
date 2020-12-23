class Cup:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def iterate(current, cups):
    current = current.next

    picked_up = [
        current.next,
        current.next.next,
        current.next.next.next,
    ]
    current.next = picked_up[2].next

    dest = current.value - 1
    if dest < 1:
        dest = len(cups)
    while cups[dest] in picked_up:
        dest -= 1
        if dest < 1:
            dest = len(cups)
    destination = cups[dest]

    picked_up[2].next = destination.next
    destination.next = picked_up[0]

    return current

def order(cups):
    f = cups[1]
    o = ''
    for i in range(8):
        f = f.next
        o += str(f.value)
    return o

def first_two(cups):
    f = cups[1]
    return f.next.value, f.next.next.value

def parse(inputs, pad_to=None):
    inputs = [int(i) for i in inputs]
    cups = {}
    last_cup = None
    if pad_to:
        inputs += list(
            range(len(inputs) + 1, pad_to + 1)
        )
    for i in inputs:
        cup = Cup(i)
        cups[i] = cup
        if last_cup:
            last_cup.next = cup
        last_cup = cup

    last_cup.next = cups[inputs[0]]

    return cups, last_cup

inputs = '135468729'

cups, current = parse(inputs)
for i in range(100):
    current = iterate(current, cups)

print('Part 1:', order(cups))

cups, current = parse(inputs, pad_to=1000000)
for i in range(10000000):
    current = iterate(current, cups)

one = cups[1]
a = one.next.value
b = one.next.next.value

print('Part 2:', a * b)
