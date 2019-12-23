from collections import defaultdict
from intcode import parse_file, Computer


def run_one(queues, network):
    while True:
        for i, c in network.items():
            if len(queues[i]) > 0:
                c.inputs.append(queues[i].pop(0))
            else:
                c.inputs.append(-1)

            c.iterate()
            addr = c.output
            if addr is None:
                continue
            c.iterate()
            x = c.output
            c.iterate()
            y = c.output

            if 0 <= addr < 50:
                queues[addr].append(x)
                queues[addr].append(y)

            if addr == 255:
                return y


def run_two(network, nat):
    last_nat = [None, None]
    while True:
        empty_inputs = all([len(c.inputs) == 0 for c in network.values()])
        empty_outputs = all([c.output == None for c in network.values()])
        empty_nat = nat == [None, None]
        if empty_outputs and not empty_nat:
            network[0].inputs.append(nat[0])
            network[0].inputs.append(nat[1])
            if last_nat[1] == nat[1]:
                return nat[1]
            last_nat = nat
        for i, c in network.items():
            c.output = None
            c.iterate()
            addr = c.output
            c.iterate()
            x = c.output
            c.iterate()
            y = c.output

            if addr is None:
                if len(c.inputs) == 0:
                    c.inputs.append(-1)
            elif addr == 255:
                nat = [x, y]
            elif addr < 50 and addr >= 0:
                network[addr].inputs.append(x)
                network[addr].inputs.append(y)


def part_two():
    network = {}
    for i in range(50):
        program = parse_file('input.intcode')
        c = Computer(program, [i])
        network[i] = c

    return run_two(network, [None, None])


def part_one():
    queues = {}
    network = {}
    for i in range(50):
        program = parse_file('input.intcode')
        c = Computer(program, [i])
        queues[i] = []
        network[i] = c

    return run_one(queues, network)


print("Part 1:", part_one())
print("Part 2:", part_two())