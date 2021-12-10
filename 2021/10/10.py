def parse(file):
    with open(file) as f:
        return [l.strip() for l in f.readlines() if len(l.strip()) > 0]

invalid_score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

stack_scores = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

pairs = {
    ')': '(',
    '>': '<',
    ']': '[',
    '}': '{',
}

def stack_score(stack):
    score = 0
    for c in stack:
        score *= 5
        score += stack_scores[c]
    return score

def interpret(line):
    stack = []
    for c in line:
        if c in pairs.values():
            stack.append(c)
            continue
        if len(stack) == 0:
            return True, c
        if pairs[c] != stack.pop():
            return True, c
    return False, reversed(stack)

def middle_value(l):
    midpoint = int((len(l) - 1) / 2)
    return sorted(l)[midpoint]

lines = parse('input.txt')

one = 0
two = []
for line in lines:
    invalid, result = interpret(line)
    if invalid:
        one += invalid_score[result]
    else:
        two.append(stack_score(result))

print('Part 1:', one)
print('Part 2:', middle_value(two))
