from math import ceil


def split(n):
    return [int(d) for d in str(n)]


def apply_phase_full(numbers, phase):
    multipliers = (
        [0] * phase +
        [1] * phase +
        [0] * phase +
        [-1] * phase
    )
    r = []
    for p, _ in enumerate(numbers):
        phase = p + 1
        multipliers = (
            [0] * phase +
            [1] * phase +
            [0] * phase +
            [-1] * phase
        )
        s = 0
        for i, d in enumerate(numbers):
            m_index = (i + 1) % len(multipliers)
            m = multipliers[m_index]
            new = d * m
            s += new
        r.append(abs(s) % 10)
    return r


def apply_phase(numbers, phase):
    r = []
    s = 0
    l = len(numbers)
    for i, n in enumerate(reversed(numbers)):
        if i > l / 2:
            r.append(0)
        else:
            s += n
            r.append(s % 10)

    r = list(reversed(r))
    return r


def part_one(n):
    for i in range(1, 101):
        n = apply_phase_full(n, i)

    return ''.join(str(i) for i in n[:8])


def part_two(n):
    offset = int("".join(str(i) for i in n[:7]))

    n = n * 10000

    for i in range(1, 101):
        n = apply_phase(n, i)

    return ''.join(str(i) for i in n[offset:offset+8])


with open('input.txt') as f:
    input_number = split(f.readline().strip())

print("Part 1:", part_one(input_number))
print("Part 2:", part_two(input_number))
