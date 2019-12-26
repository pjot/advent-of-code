import re


def has_abba(s):
    for i in range(len(s) - 3):
        a = s[i]
        b = s[i+1]
        c = s[i+2]
        d = s[i+3]
        if (a, b) == (d, c) and a != b:
            return True
    return False


def hypernets(s):
    return re.findall(r'\[([a-z]+)\]', s)


def supports_tls(s):
    hns = hypernets(s)
    for hn in hns:
        if has_abba(hn):
            return False
        s = s.replace('[' + hn + ']', '[]')
    return has_abba(s)


def find_babs(s):
    for i in range(len(s) - 2):
        a = s[i]
        b = s[i+1]
        c = s[i+2]
        if a == c and a != b:
            yield b + a + b


def supports_ssl(s):
    hns = hypernets(s)
    babs = set()
    for hn in hns:
        for bab in find_babs(hn):
            babs.add(bab)
        s = s.replace('[' + hn + ']', '[]')

    for bab in babs:
        if bab in s:
            return True

    return False


lines = []
with open('input') as f:
    for line in f.readlines():
        lines.append(line.strip())

tls = 0
ssl = 0
for s in lines:
    if supports_tls(s):
        tls += 1
    if supports_ssl(s):
        ssl += 1

print('Part 1:', tls)
print('Part 2:', ssl)