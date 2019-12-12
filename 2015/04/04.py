import hashlib

answer = 'iwrupvqb'


def md5(s):
    return hashlib.md5(s.encode('ascii')).hexdigest()


def find_key(answer, zeroes):
    beginning = '0' * zeroes
    i = 1
    while True:
        phrase = '{}{}'.format(answer, i)
        if md5(phrase).startswith(beginning):
            return i
        i += 1


print("Part 1:", find_key(answer, 5))
print("Part 2:", find_key(answer, 6))
