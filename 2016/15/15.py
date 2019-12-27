one = [
    (17, 15),
    (3, 2),
    (19, 4),
    (13, 2),
    (7, 2),
    (5, 0),
]
two = [
    (11, 0),
]

def is_match(n, discs):
    for i, disc in enumerate(discs):
        m, p = disc
        if (n + p + i) % m != 0:
            return False
    return True


def find(discs):
    n = 0
    while True:
        n += 1
        if is_match(n, discs):
            return n - 1


print('Part 1:', find(one))
print('Part 2:', find(one + two))