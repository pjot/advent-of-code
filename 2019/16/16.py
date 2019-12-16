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


with open('input.txt') as f:
    input_number = split(f.readline().strip())

n1 = input_number

offset = int("".join(str(i) for i in n1[:7]))
n2 = input_number * 10000

for i in range(1, 101):
    n1 = apply_phase_full(n1, i)

print("Part 1:", ''.join(str(i) for i in n1[:8]))

for i in range(1, 101):
    print(i)
    n2 = apply_phase(n2, i)

print("Part 2:", ''.join(str(i) for i in n2[offset:offset+8]))
