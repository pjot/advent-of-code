import re


def is_nice(s):
    for bad in ['ab', 'cd', 'pq', 'xy']:
        if bad in s:
            return False

    vowels = sum(s.count(vowel) for vowel in 'aeiou')

    if vowels < 3:
        return False

    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            return True
        i += 1

    return False


between = re.compile(r'.*(.).\1.*')
pair = re.compile(r'.*(..).*\1.*')


def is_nicer(s):
    if not between.match(s):
        return False
    if not pair.match(s):
        return False
    return True


with open('input.txt') as f:
    lines = list(f.readlines())

nice = [s for s in lines if is_nice(s)]
nicer = [s for s in lines if is_nicer(s)]

print("Part 1:", len(nice))
print("Part 2:", len(nicer))
