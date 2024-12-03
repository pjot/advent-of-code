import re

def one(memory):
    muls = re.findall("mul\((\d+,\d+)\)", memory)
    s = 0
    for mul in muls:
        a, b = [int(n) for n in mul.split(",")]
        s += a * b
    return s

def two(memory):
    pattern = (
        "mul\((\d+,\d+)\)"
        "|"
        "(do)\(\)"
        "|"
        "(don't)\(\)"
    )
    instructions = re.findall(pattern, memory)

    enabled = True
    s = 0
    for m, do, dont in instructions:
        if do:
            enabled = True
        elif dont:
            enabled = False
        elif m and enabled:
            a, b = [int(n) for n in m.split(",")]
            s += a * b

    return s

with open("input") as f:
    mem = f.read()

print("Part 1:", one(mem))
print("Part 1:", two(mem))
