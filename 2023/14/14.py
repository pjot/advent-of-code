def parse(file):
    with open(file) as f:
        return [l.strip() for l in f.readlines()]

def transpose(lines):
    new_lines = []
    for x, _ in enumerate(lines[0]):
        line = ""
        for l in lines:
            line += l[x]
        new_lines.append(line)
    return new_lines

def flip(lines):
    return [line[::-1] for line in lines]

def tilt(line):
    a, b = "", line
    while a != b:
        a, b = b, b.replace(".O", "O.")
    return b

def tilt_left(lines):
    return [tilt(line) for line in lines]

def tilt_right(lines):
    return flip(tilt_left(flip(lines)))

def tilt_up(lines):
    return transpose(tilt_left(transpose(lines)))

def tilt_down(lines):
    return transpose(tilt_right(transpose(lines)))

def load(lines):
    height = len(lines)
    return sum(
        (height - y) * line.count("O")
        for y, line in enumerate(lines)
    )

def cycle(lines):
    lines = tilt_up(lines)
    lines = tilt_left(lines)
    lines = tilt_down(lines)
    lines = tilt_right(lines)
    return lines

def two(lines):
    seen = {}
    seen[tuple(lines)] = 0

    big = 1000000000 - 1

    for i in range(big):
        lines = cycle(lines)

        h = tuple(lines)
        if h in seen:
            cycle_length = i - seen[h]
            remaining = big - i
            if remaining % cycle_length == 0:
                return load(lines)
        else:
            seen[h] = i

lines = parse("input")

print("Part 1:", load(tilt_up(lines)))
print("Part 2:", two(lines))
