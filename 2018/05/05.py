def parse(file):
    with open(file) as f:
        return f.readline().strip()


REPLACEMENTS = [
    a + a.upper() for a in 'qwertyuiopasdfghjklzxcvbnm'
] + [
    a.upper() + a for a in 'qwertyuiopasdfghjklzxcvbnm'
]


def iterate(s):
    for a in REPLACEMENTS:
        s = s.replace(a, '')
    return s

def multi_iterate(s):
    while True:
        s2 = iterate(s)
        if s2 == s:
            return len(s2)
        s = s2


def removed_multi(s):
    polymers = set([ss.lower() for ss in s])
    min_len = float('inf')
    for p in polymers:
        s2 = s.replace(p, '').replace(p.upper(), '')
        min_len = min(min_len, multi_iterate(s2))
    return min_len
    

s = parse('input')
print('Part 1:', multi_iterate(s))

print('Part 2:', removed_multi(s))