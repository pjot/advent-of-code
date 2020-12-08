def parse(file):
    program = {}
    with open(file) as f:
        for i, line in enumerate(f.readlines()):
            op, arg = line.strip().split()
            arg = int(arg)
            program[i] = (op, arg)
    return program

def run(code):
    acc = 0
    pos = 0
    seen = set()
    while True:
        if pos in seen:
            return 'SEEN', acc
        if pos not in code:
            return 'TERM', acc

        seen.add(pos)
        op, arg = code[pos]

        if op == 'nop':
            pos += 1

        elif op == 'jmp':
            pos += arg

        elif op == 'acc':
            acc += arg
            pos += 1

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
