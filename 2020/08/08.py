def parse(file):
    program = {}
    with open(file) as f:
        for i, line in enumerate(f.readlines()):
            op, arg = line.strip().split()
            arg = int(arg)
            program[i] = (op, arg)
    return program

def iterate(code, pos, acc):
    op, arg = code[pos]

    if op == 'nop':
        return pos + 1, acc
    elif op == 'jmp':
        return pos + arg, acc
    elif op == 'acc':
        return pos + 1, acc + arg

def run(code):
    acc = pos = 0
    seen = set()
    while True:
        if pos in seen:
            return 'SEEN', acc
        if pos not in code:
            return 'TERM', acc

        seen.add(pos)
        pos, acc = iterate(code, pos, acc)

def potential_fix(code):
    for i, instruction in code.items():
        fixed = {k: v for k, v in code.items()}

        op, arg = instruction
        if op == 'acc':
            continue
        elif op == 'jmp':
            fixed[i] = ('nop', arg)
        elif op == 'nop':
            fixed[i] = ('jmp', arg)

        yield fixed


p = parse('input.txt')
_, acc = run(p)

print('Part 1:', acc)

for code in potential_fix(p):
    ret, acc = run(code)
    if ret == 'TERM':
        print('Part 2:', acc)
        break
