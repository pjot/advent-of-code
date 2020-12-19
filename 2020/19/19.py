import re

def parse(lines):
    rules = {}
    horizon = set()
    inputs = []
    parsing_rules = True
    for line in lines:
        if line.strip() == '':
            parsing_rules = False
            continue

        if not parsing_rules:
            inputs.append(line.strip())
            continue

        i, rule = line.strip().split(': ')
        if '"' in rule:
            rule = rule[1]
            horizon.add(i)

        rules[i] = rule
    return rules, inputs, horizon

def is_done(rs):
    for v in rs:
        if re.match(r'[0-9]', v):
            return False
    return True

def compile_to_regex(rules, horizon):
    while len(horizon) > 0:
        new_horizon = set()
        for h in horizon:
            val = rules[h]
            new_rules = {}

            for i, rule in rules.items():
                if i == h:
                    continue
                if h in rule.split():
                    new_rule = ' '.join([
                        val if r == h else r
                        for r in rule.split()
                    ])
                    if is_done(new_rule):
                        new_rule = f'({new_rule})'
                        new_horizon.add(i)
                    new_rules[i] = new_rule
                else:
                    new_rules[i] = rule
            rules = new_rules
        horizon = new_horizon
        if len(rules) == 1:
            break
    return rules['0'].replace(' ', '')

def matches(regex, inputs):
    regex = re.compile('^' + regex + '$')

    valid = 0
    for i in inputs:
        if regex.match(i):
            valid += 1

    return valid

def solve(lines):
    rules, inputs, horizon = parse(lines)
    regex = compile_to_regex(rules, horizon)
    return matches(regex, inputs)

with open('input.txt') as f:
    s = f.read()

lines1 = s.split('\n')

s2 = s.replace('8: 42\n', '').replace('11: 42 31\n', '')
lines2 = ['8: 42 | 42 1000'] + ['1005: "c"']
lines2 += ['11: 42 31 | 42 2000 31'] + ['2005: "d"']
lines2 += [f'{r}: 42 | 42 {r+1}' for r in range(1000, 1005)]
lines2 += [f'{r}: 42 31 | 42 {r+1} 31' for r in range(2000, 2005)]
lines2 += s2.split('\n')

print('Part 1:', solve(lines1))
print('Part 2:', solve(lines2))
