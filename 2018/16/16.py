from collections import Counter, defaultdict


def addr(r, a, b, c):
    r[c] = r[a] + r[b]
    return r

def addi(r, a, b, c):
    r[c] = r[a] + b
    return r

def mulr(r, a, b, c):
    r[c] = r[a] * r[b]
    return r

def muli(r, a, b, c):
    r[c] = r[a] * b
    return r

def banr(r, a, b, c):
    r[c] = r[a] & r[b]
    return r

def bani(r, a, b, c):
    r[c] = r[a] & b
    return r

def borr(r, a, b, c):
    r[c] = r[a] | r[b]
    return r

def bori(r, a, b, c):
    r[c] = r[a] | b
    return r

def setr(r, a, b, c):
    r[c] = r[a]
    return r

def seti(r, a, b, c):
    r[c] = a
    return r

def gtir(r, a, b, c):
    r[c] = 1 if a > r[b] else 0
    return r

def gtri(r, a, b, c):
    r[c] = 1 if r[a] > b else 0
    return r

def gtrr(r, a, b, c):
    r[c] = 1 if r[a] > r[b] else 0
    return r

def eqir(r, a, b, c):
    r[c] = 1 if a == r[b] else 0
    return r

def eqri(r, a, b, c):
    r[c] = 1 if r[a] == b else 0
    return r

def eqrr(r, a, b, c):
    r[c] = 1 if r[a] == r[b] else 0
    return r

operations = [
    addi, addr,
    bani, banr,
    bori, borr,
    eqir, eqri, eqrr,
    gtir, gtri, gtrr,
    muli, mulr,
    seti, setr,
]

def extract_array(l):
    return list(map(
        int,
        l.split('[')[1].rstrip(']').split(',')
    ))

def extract_stack(l):
    return list(map(
        int,
        l.split(' ')
    ))

def parse(file):
    tests = []
    with open(file) as f:
        while True:
            try:
                before = extract_array(f.readline().strip())
                stack = extract_stack(f.readline().strip())
                after = extract_array(f.readline().strip())

                tests.append((before, stack, after))

                f.readline()
            except:
                break

    return tests

def fn_name(fn):
    return str(fn).split(' ')[1]

def test_sample(before, after, stack):
    op_code, a, b, c = stack
    possible = [
        fn for fn in operations if fn(before[:], a, b, c) == after
    ]
    return op_code, possible

def test_file(file):
    tests = parse(file)
    matches = Counter()
    op_codes = defaultdict(set)
    for before, stack, after in tests:
        op_code, possible = test_sample(before, after, stack)
        matches[len(possible)] += 1
    
        for p in possible:
            op_codes[op_code].add(p)
    return matches, op_codes

def count_three_or_above(matches):
    return sum(
        v for k, v in matches.items() if k > 2
    )

def deduce(op_codes):
    codes = {}
    while len(op_codes) > 0:
        for c, v in codes.items():
            if c in op_codes:
                del op_codes[c]
            for k in op_codes.keys():
                op_codes[k].discard(v)
        for k, v in op_codes.items():
            if len(v) == 1:
                code = v.pop()
                codes[k] = code
    return codes

def parse_program(file):
    program = []
    with open(file) as f:
        for line in f.readlines():
            p = list(map(
                int,
                line.strip().split(' ')
            ))
            program.append(p)
    return program

def run_program(op_codes, program):
    registers = [0, 0, 0, 0]
    for p in program:
        op_code, a, b, c = p
        fn = op_codes[op_code]
        registers = fn(registers, a, b, c)
    return registers

matches, op_codes = test_file('input')
print('Part 1:', count_three_or_above(matches))

deduced = deduce(op_codes)
program = parse_program('program')
registers = run_program(deduced, program)
print('Part 2:', registers[0])
