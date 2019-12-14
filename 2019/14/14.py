from collections import defaultdict
from math import ceil


def parse_file(file):
    with open(file) as f:
        return [parse(l.strip()) for l in f.readlines()]


def split(t):
    amount, kind = t.split(' ')
    return kind, int(amount)


def parse(l):
    parts = l.split(' => ')
    raw_inputs = parts[0].split(', ')
    inputs = [split(x) for x in raw_inputs]
    return inputs, (split(parts[1]))


def ore_for(chemical, amount, stored):
    if chemical == 'ORE':
        return amount

    available = min(amount, stored[chemical]) 
    amount -= available
    stored[chemical] -= available

    output, inputs = reactions[chemical]
    quantity = ceil(amount / output)

    ore = 0
    for required_chem, required_units in inputs:
        ore += ore_for(
            required_chem,
            quantity * required_units,
            stored
        )

    stored[chemical] += quantity * output - amount

    return ore


codes = parse_file('input.txt')
reactions = {}
for code in codes:
    outputs, produced = code
    chemical, amount = produced
    reactions[chemical] = (amount, outputs)


def trillion():
    trillion = 1000000000000
    i = 1
    ores = 1
    while ores < trillion:
        i *= 2
        ores = ore_for('FUEL', i, defaultdict(int))

    lower = i / 2
    upper = i
    while True:
        middle = int(lower + (upper - lower) / 2)
        if ore_for('FUEL', middle, defaultdict(int)) > trillion:
            upper = middle
        else:
            lower = middle
        if lower + 1 == upper:
            return lower


print("Part 1:", ore_for('FUEL', 1, defaultdict(int)))
print("Part 2:", trillion())