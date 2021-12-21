def parse(file):
    with open(file) as f:
        ip = int(f.readline().strip().split().pop())
        program = {}
        for i, line in enumerate(f.readlines()):
            op, a, b, c = line.split()
            program[i] = (op, int(a), int(b), int(c))
    return ip, program


def run(code, ip_bind, r):
    ip = 0
    while True:
        row = code.get(ip)
        if row is None:
            return r
        op, a, b, c = row

        r[ip_bind] = ip

        if op == 'seti':
            r[c] = a
        elif op == 'setr':
            r[c] = r[a]
        elif op == 'addi':
            r[c] = r[a] + b
        elif op == 'addr':
            r[c] = r[a] + r[b]
        elif op == 'mulr':
            r[c] = r[a] * r[b]
        elif op == 'muli':
            r[c] = r[a] * b
        elif op == 'eqrr':
            r[c] = 1 if r[a] == r[b] else 0
        elif op == 'gtrr':
            r[c] = 1 if r[a] > r[b] else 0
        else:
            raise Exception('unrecognized op', op)

        ip = r[ip_bind]
        ip += 1

ip_bind, code = parse('input.txt')
r = [0] * 6

r = run(code, ip_bind, r)
print('Part 1:', r[0])
