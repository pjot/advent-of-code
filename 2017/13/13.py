def parse(file):
    o = {}
    with open(file) as f:
        for line in f.readlines():
            p = line.strip().split(': ')
            o[int(p[0])] = int(p[1])
    return o


def position(highest, time):
    offset = time % ((highest - 1) * 2)
    if offset > highest - 1:
        return 2 * (highest - 1) - offset
    else:
        return offset

def passes_through(delay):
    for pos, highest in layers.items():
        if position(layers[pos], pos + delay) == 0:
            return False
    return True

layers = parse('input')
severity = 0
for pos, highest in layers.items():
    if position(layers[pos], pos) == 0:
        severity += pos * layers[pos]
print('Part 1:', severity)

delay = 0
while True:
    if passes_through(delay):
        print('Part 2:', delay)
        break
    delay += 1