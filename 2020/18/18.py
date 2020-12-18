def reduce(line, evaluate):
    last = 0
    i = 0
    while i < len(line):
        c = line[i]
        if c == '(':
            last = i
        if c == ')':
            part = line[last:i+1]
            value = str(evaluate(part[1:-1]))
            line = line.replace(part, value)
            i = 0
            continue
        i += 1
    return evaluate(line)

def calculator(expr):
    expr = expr.split()
    value = int(expr[0])
    i = 1
    while i < len(expr):
        op = expr[i]
        n = int(expr[i+1])
        if op == '+':
            value += n
        if op == '*':
            value *= n
        i += 2
    return value

def plus_before_mult(expr):
    expr = expr.split()
    acc = int(expr[0])
    value = 1
    i = 1
    while i < len(expr):
        op = expr[i]
        n = int(expr[i+1])
        if op == '*':
            value *= acc
            acc = n
        if op == '+':
            acc += n
        i += 2

    return value * acc

with open('input.txt') as f:
    one = two = 0
    for line in f.readlines():
        line = line.strip()
        one += reduce(line, calculator)
        two += reduce(line, plus_before_mult)

print('Part 1:', one)
print('Part 2:', two)
