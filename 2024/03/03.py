import re

def one(memory: str) -> int:
    muls = re.findall("mul\((\d+,\d+)\)", memory)
    s = 0
    for mul in muls:
        a, b = [int(n) for n in mul.split(",")]
        s += a * b
    return s

def two(memory: str) -> int:
    pattern = (
        "mul\((\d+,\d+)\)"
        "|"
        "(do)\(\)"
        "|"
        "(don't)\(\)"
    )

    s = 0
    enabled = True
    for match in re.finditer(pattern, memory):
        if not match.lastindex:
            continue
        m = match[match.lastindex]

        match m, enabled:
            case "do", _:
                enabled = True
            case "don't", _:
                enabled = False

            case _, True:
                a, b = [int(n) for n in m.split(",")]
                s += a * b
    return s

with open("input") as f:
    mem = f.read()

print("Part 1:", one(mem))
print("Part 2:", two(mem))
