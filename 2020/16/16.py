import re

reading = 'rules'
rules = []
nearby = []
with open('input.txt') as f:
    for line in f.readlines():
        line = line.strip()

        if reading == 'rules':
            if line == '':
                reading = 'your'
                continue

            matches = re.findall(r'(\d+-\d+)', line)
            rule = []
            for match in matches:
                lo, hi = match.split('-')
                rule.append((int(lo), int(hi)))
            rules.append((line.split(':')[0], rule))

        if reading == 'your':
            if line.startswith('your'):
                continue
            if line == '':
                reading = 'nearby'
                continue

            your = [int(i) for i in line.split(',')]

        if reading == 'nearby':
            if line.startswith('nearby'):
                continue
            nearby.append([int(i) for i in line.split(',')])

def invalid_sum(ticket, rules):
    invalid = 0
    for n in ticket:
        valid = False
        for _, limits in rules:
            for lo, hi in limits:
                if lo <= n <= hi:
                    valid = True
                if valid:
                    break
            if valid:
                break
        if not valid:
            invalid += n
    return invalid

invalid = 0
valid_tickets = []
for ticket in nearby:
    t = invalid_sum(ticket, rules)
    if t == 0:
        valid_tickets.append(ticket)
    invalid += t

print('Part 1:', invalid)

def could_be(limits, n):
    for lo, hi in limits:
        if lo <= n <= hi:
            return True
    return False
    
def rule_for_index(index, rules, limits, tickets):
    possible = rules
    for ticket in tickets:
        n = ticket[index]
        for rule in list(possible):
            ls = limits[rule]
            if not could_be(ls, n):
                possible.remove(rule)
                continue
        if len(possible) == 1:
            return possible.pop()

limits = {r: l for r, l in rules}
rule_indices = {}

while True:
    for i, _ in enumerate(your):
        if i in rule_indices.values():
            continue
        all_rules = set([rule for rule, _ in rules if rule not in rule_indices])
        r = rule_for_index(i, all_rules, limits, valid_tickets + [your])
        rule_indices[r] = i

    val = 1
    cnt = 0
    for rule, index in rule_indices.items():
        if rule is None:
            continue
        if rule.startswith('departure'):
            cnt += 1
            val *= your[index]

    if cnt == 6:
        print('Part 2:', val)
        break
