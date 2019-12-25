from itertools import combinations
from intcode import parse_file, Computer


def run(inputs):
    program = parse_file('game.intcode')
    c = Computer(program, inputs)

    o = ''
    while True:
        done = c.iterate()
        if done:
            break
        else:
            print(chr(c.output), end='')
            #o += chr(c.output)
    return o


def expand(d):
    if d == 'n':
        return 'north\n'
    if d == 's':
        return 'south\n'
    if d == 'e':
        return 'east\n'
    if d == 'w':
        return 'west\n'


def reverse_direction(d):
    if d == 'n':
        return 's'
    if d == 's':
        return 'n'
    if d == 'e':
        return 'w'
    if d == 'w':
        return 'e'


things = {
    'mouse': 'n',
    'pointer': 'nn',
    #'giant electromagnet': 'nne',
    #'escape pod': 'ne',
    #'infinite loop': 's',
    #'photons': 'ssw',
    'monolith': 'w',
    #'sand': 'ws',
    'space law space brochure': 'wnws',
    'asterisk': 'wssw',
    'mutex': 'wssws',
    'food ration': 'wnw',
}
checkpoint = 'sswse'


def test(items):
    inputs = []
    for item in items:
        for direction in things[item]:
            inputs += expand(direction)
        inputs += 'take '
        inputs += item
        inputs += '\n'
        for direction in reversed(things[item]):
            inputs += expand(reverse_direction(direction))
    for direction in checkpoint:
        inputs += expand(direction)
    return [ord(i) for i in inputs]


def too_light(o):
    lines = o.split('\n')
    for line in lines[-20:]:
        if 'Droids on this ship are heavier' in line:
            return True
    return False


def too_heavy(o):
    lines = o.split('\n')
    for line in lines[-20:]:
        if 'Droids on this ship are lighter' in line:
            return True
    return False


def test_items(items):
    inputs = test(items)
    out = run(inputs)
    if too_light(out):
        print('too light:', items)
    elif too_heavy(out):
        print('too heavy:', items)
    else:
        print('just right:', items)


inputs = test([
    'space law space brochure',
    'asterisk',
    'mutex',
    'food ration'
])
run(inputs)
