from collections import defaultdict


def parse(file):
    monkeys = []
    with open(file) as f:
        lines = [l.strip() for l in f.readlines()]

    while lines:
        monkey = {'inspected': 0}
        lines.pop(0)

        _, starting_items = lines.pop(0).split(': ')
        monkey['items'] = [
            int(i) for i in starting_items.split(', ')
        ]

        op = lines.pop(0).split(' ')
        if op[4] == '*' and op[5] == 'old':
            operation = {'kind': 'square'}
        elif op[4] == '*' :
            operation = {'kind': 'multiply', 'n': int(op[5])}
        elif op[4] == '+':
            operation = {'kind': 'add', 'n': int(op[5])}
        monkey['operation'] = operation

        test = lines.pop(0).split(' ')
        monkey['test'] = int(test[3])

        true = lines.pop(0).split(' ')
        monkey['true'] = int(true[5])

        false = lines.pop(0).split(' ')
        monkey['false'] = int(false[5])

        monkeys.append(monkey)
        if lines:
            lines.pop(0)

    return monkeys

def turn(monkey, modulo, divide_by_three):
    items = defaultdict(list)

    for worry in monkey['items']:
        operation = monkey['operation']
        if operation['kind'] == 'multiply':
            worry *= operation['n']
        elif operation['kind'] == 'add':
            worry += operation['n']
        elif operation['kind'] == 'square':
            worry *= worry

        if divide_by_three:
            worry = worry // 3

        worry = worry % modulo

        if worry % monkey['test'] == 0:
            items[monkey['true']].append(worry)
        else:
            items[monkey['false']].append(worry)

    return items, len(monkey['items'])

def round(monkeys, modulo, divide_by_three):
    for monkey in monkeys:
        items, inspected = turn(
            monkey, modulo, divide_by_three
        )
        monkey['items'] = []
        monkey['inspected'] += inspected
        for k, v in items.items():
            monkeys[k]['items'].extend(v)
    return monkeys

def monkey_business(monkeys):
    inspected = sorted([m['inspected'] for m in monkeys], reverse=True)
    return inspected[0] * inspected[1]

def divisor_product(monkeys):
    p = 1
    for monkey in monkeys:
        p *= monkey['test']
    return p

monkeys = parse('input.txt')
modulo = divisor_product(monkeys)
for i in range(20):
    monkeys = round(monkeys, modulo, True)
print("Part 1:", monkey_business(monkeys))

monkeys = parse('input.txt')
for i in range(10000):
    monkeys = round(monkeys, modulo, False)
print("Part 2:", monkey_business(monkeys))
