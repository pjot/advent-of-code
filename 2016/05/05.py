import hashlib


def md5(s):
    return hashlib.md5(s.encode()).hexdigest()


def pretty(two):
    return ''.join(two.get(i, '_') for i in range(8))


prefix = 'wtnhxymk'

one = ''
two = {}
i = 0
while len(two) < 8:
    i += 1
    hash = md5(prefix + str(i))

    if hash[:5] == '00000':
        a = hash[5:6]
        b = hash[6:7]

        if len(one) < 8:
            one += a

        if a in '01234567' and two.get(int(a)) is None:
            two[int(a)] = b


print('Part 1:', one)
print('Part 2:', pretty(two))
