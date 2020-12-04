import re

with open('input.txt') as f:
    things = []
    thing = {}
    for line in f.readlines():
        if len(line.strip()) == 0:
            things.append(thing)
            thing = {}
        else:
            items = line.strip().split()
            for item in items:
                key, val = item.split(':')
                thing[key] = val

def has_required_fields(thing):
    required_fields = [
        'byr', 'iyr', 'eyr', 'hgt',
        'hcl', 'ecl', 'pid'
    ]
    for field in required_fields:
        if field not in thing:
            return False
    return True

def is_between(value, low, high):
    v = int(value)
    return low <= v <= high

def has_valid_fields(thing):
    if not has_required_fields(thing):
        return False

    if not is_between(thing['byr'], 1920, 2002):
        return False

    if not is_between(thing['iyr'], 2010, 2020):
        return False

    if not is_between(thing['eyr'], 2020, 2030):
        return False

    match = re.search(r'(\d+)(in|cm)', thing['hgt'])
    if not match:
        return False

    height, unit = match.groups()
    if unit == 'cm' and not is_between(height, 150, 193):
        return False
    if unit == 'in' and not is_between(height, 59, 76):
        return False

    if not re.match(r'^#[a-f0-9]{6}$', thing['hcl']):
        return False

    valid_ecl = [
        'amb', 'blu', 'brn', 'gry',
        'grn', 'hzl', 'oth',
    ]
    if thing['ecl'] not in valid_ecl:
        return False

    if not re.match(r'^\d{9}$', thing['pid']):
        return False

    return True

has_fields = 0
valid = 0
for thing in things:
    if has_required_fields(thing):
        has_fields += 1
    if has_valid_fields(thing):
        valid += 1

print('Part 1: ', has_fields)
print('Part 2: ', valid)
