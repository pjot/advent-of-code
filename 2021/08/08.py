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
possible = {k: set(values) for k in values}

def all_but(s):
    rest = set(values)
    for c in s:
        rest.remove(c)
    return rest

def handle_digit(possible, d):
    remaining = all_but(d)
    if len(d) == 2:
        for c in remaining:
            possible['c'].discard(c)
            possible['f'].discard(c)

    if len(d) == 3:
        for c in remaining:
            possible['a'].discard(c)
            possible['c'].discard(c)
            possible['f'].discard(c)

    if len(d) == 4:
        for c in remaining:
            possible['b'].discard(c)
            possible['c'].discard(c)
            possible['d'].discard(c)
            possible['f'].discard(c)

    return possible

def perms(possible):
    possible = {
        k: list(v)
        for k, v in possible.items()
    }
    ps = [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
        [0, 1, 1],
        [1, 0, 0],
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 1],
    ]
    for p in ps:
        b, c, e = p
        yield {
            'a': possible['a'][0],
            'b': possible['b'][b],
            'c': possible['c'][c],
            'd': possible['d'][0 if b == 1 else 1],
            'e': possible['e'][e],
            'f': possible['f'][0 if c == 1 else 1],
            'g': possible['g'][0 if e == 1 else 1],
        }

def is_valid(mapping, inputs, outputs):
    for i in inputs:
        m = i.upper()
        for k, v in mapping.items():
            m = m.replace(v.upper(), k)
        m = ''.join(sorted(m))
        if not numbers.get(m) is not None:
            return

    n = ''
    for i in outputs:
        m = i.upper()
        for k, v in mapping.items():
            m = m.replace(v.upper(), k)
        m = ''.join(sorted(m))
        if numbers.get(m) is not None:
            n += str(numbers.get(m))
        else:
            return

    return int(n)


o_sum = 0
for i, o in zip(inputs, outputs):
    possible = {k: set(values) for k in values}
    for d in i:
        possible = handle_digit(possible, d)

    for d in o:
        possible = handle_digit(possible, d)

    if len(possible['c']) == 2:
        for c in possible['c']:
            possible['a'].discard(c)
            possible['b'].discard(c)
            possible['d'].discard(c)
            possible['e'].discard(c)
            possible['g'].discard(c)

    if len(possible['f']) == 2:
        for c in possible['f']:
            possible['a'].discard(c)
            possible['b'].discard(c)
            possible['d'].discard(c)
            possible['e'].discard(c)
            possible['g'].discard(c)

    done = {}
    for k, v in possible.items():
        if len(v) == 1:
            done[k] = v


    for k, v in done.items():
        for c in values:
            if c != k:
                possible[c] -= v

    for k, v in possible.items():
        for k2, v2 in possible.items():
            if k != k2 and v == v2:
                for l in values:
                    if l not in [k, k2]:
                        for c in v:
                            possible[l].discard(c)

    for per in perms(possible):
        r = is_valid(per, i, o)
        if r is not None:
            o_sum += r
            break

print('Part 2:', o_sum)
