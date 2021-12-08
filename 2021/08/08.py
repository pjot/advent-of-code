import itertools

def parse(file):
    inputs = []
    outputs = []
    with open(file) as f:
        for line in f.readlines():
            if not '|' in line:
                continue
            input, output = line.split(' | ')
            inputs.append(input.split())
            outputs.append(output.split())
    return inputs, outputs

inputs, outputs = parse('input.txt')

numbers = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9,
}
values = 'abcdefg'

def all_but(s):
    rest = set(values)
    for c in s:
        rest.remove(c)
    return rest

def handle_signal(possible, signal):
    remaining = all_but(signal)
    if len(signal) == 2:
        possible['c'] -= remaining
        possible['f'] -= remaining

    if len(signal) == 3:
        possible['a'] -= remaining
        possible['c'] -= remaining
        possible['f'] -= remaining

    if len(signal) == 4:
        possible['b'] -= remaining
        possible['c'] -= remaining
        possible['d'] -= remaining
        possible['f'] -= remaining

    return possible

def flip(n):
    return 1 if n == 0 else 0

def permutations(possible):
    possible = {
        k: list(v) for k, v in possible.items()
    }
    cases = itertools.product(range(2), repeat=3)
    for case in cases:
        b, c, e = case
        yield {
            'a': possible['a'][0],
            'b': possible['b'][b],
            'c': possible['c'][c],
            'd': possible['d'][flip(b)],
            'e': possible['e'][e],
            'f': possible['f'][flip(c)],
            'g': possible['g'][flip(e)],
        }

def parse_signal(mapping, signal):
    signal = signal.upper()
    for output, input in mapping.items():
        signal = signal.replace(input.upper(), output)
    return ''.join(sorted(signal))

def try_mapping(mapping, inputs, outputs):
    for i in inputs:
        s = parse_signal(mapping, i)
        if not numbers.get(s) is not None:
            return

    n = ''
    for i in outputs:
        s = parse_signal(mapping, i)
        if numbers.get(s) is not None:
            n += str(numbers.get(s))
        else:
            return

    return int(n)

def reduce(possible):
    # Reduce because of c and f:
    if len(possible['c']) == 2:
        possible['a'] -= possible['c']
        possible['b'] -= possible['c']
        possible['d'] -= possible['c']
        possible['e'] -= possible['c']
        possible['g'] -= possible['c']

    # Reduce because we know some mappings
    done = {}
    for k, v in possible.items():
        if len(v) == 1:
            done[k] = v

    for k, v in done.items():
        for c in all_but(k):
            possible[c] -= v

    # Reduce because we know some pairs of mappings
    for k, v in possible.items():
        for k2, v2 in possible.items():
            if k != k2 and v == v2:
                for l in all_but(k + k2):
                    possible[l] -= v
    return possible

one = 0
for o in outputs:
    for signal in o:
        if len(signal) in [2, 3, 4, 7]:
            one +=1

two = 0
for i, o in zip(inputs, outputs):
    possible = {k: set(values) for k in values}
    for signal in i:
        possible = handle_signal(possible, signal)

    for signal in o:
        possible = handle_signal(possible, signal)

    possible = reduce(possible)

    for permutation in permutations(possible):
        output = try_mapping(permutation, i, o)
        if output is not None:
            two += output
            break

print('Part 1:', one)
print('Part 2:', two)
