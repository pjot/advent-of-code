def reverse_and_flip(s):
    o = ''
    for i in reversed(s):
        if i == '1':
            o += '0'
        else:
            o += '1'
    return o


def dragon_curve(i):
    return i + '0' + reverse_and_flip(i)


def checksum(s):
    o = ''
    for i in range(int(len(s) / 2)):
        a = s[2 * i]
        b = s[2 * i + 1]
        if a == b:
            o += '1'
        else:
            o += '0'
    return o


def cs(s):
    while True:
        s = checksum(s)
        if len(s) % 2 != 0:
            return s


def fill(data, size):
    while len(data) < size:
        data = dragon_curve(data)

    data = data[:size]

    return cs(data)

print('Part 1:', fill('11011110011011101', 272))
print('Part 2:', fill('11011110011011101', 35651584))