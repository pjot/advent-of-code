from intcode import parse_file, Computer


def run():
    network = {
        i: Computer(parse_file('input.intcode'), [i])
        for i in range(50)
    }

    nat = None
    first_y = None

    while True:
        empty_outputs = all(
            c.output is None
            for c in network.values()
        )

        if empty_outputs and nat:
            network[0].inputs += nat

        for _, c in network.items():
            c.output = None

            addr = c.iterate_once()
            x = c.iterate_once()
            y = c.iterate_once()

            if addr == 255:
                if first_y is None:
                    first_y = y
                if nat and nat[1] == y:
                    return first_y, y
                nat = [x, y]
            elif addr is None:
                c.inputs.append(-1)
            else:
                network[addr].inputs += [x, y]


one, two = run()
print("Part 1:", one)
print("Part 2:", two)
