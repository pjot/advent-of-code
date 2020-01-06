def program(n):
    alphabet = 'abcdefghijklmnop'
    return list(alphabet[:n])


def run(p, file):
    with open(file) as f:
        for line in f.readlines():
            line = line.strip()
            for instruction in line.split(','):
                if instruction[0] == 's':
                    i = int(instruction[1:])
                    p = p[-i:] + p[:-i]
                elif instruction[0] == 'x':
                    parts = instruction[1:].split('/')
                    a = int(parts[0])
                    b = int(parts[1])
                    p[a], p[b] = p[b], p[a]
                elif instruction[0] == 'p':
                    parts = instruction[1:].split('/')
                    a = p.index(parts[0])
                    b = p.index(parts[1])
                    p[a], p[b] = p[b], p[a]
    return p
    

def run_many(p, n):
    seen = []
    for i in range(n):
        s = ''.join(p)
        if s in seen:
            return seen[n % i]
        seen.append(s)
        p = run(p, 'input')
    return ''.join(p)


print('Part 1:', run_many(program(16), 1))
print('Part 2:', run_many(program(16), 1000000000))
