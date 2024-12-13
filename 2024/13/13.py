import typing

Equation = tuple[int, int, int, int, int, int]

def button(line: str) -> tuple[int, int]:
    l = line.replace(",", "").split()
    a = l[2].split("+")[1]
    b = l[3].split("+")[1]
    return int(a), int(b)

def target(line: str) -> tuple[int, int]:
    l = line.replace(",", "").split()
    a = l[1].split("=")[1]
    b = l[2].split("=")[1]
    return int(a), int(b)

def parse(file: str) -> typing.Iterator[Equation]:
    with open("input") as io:
        for p in io.read().split("\n\n"):
            lines = p.strip().splitlines()
            a, b = button(lines[0])
            c, d = button(lines[1])
            e, f = target(lines[2])
            yield a, b, c, d, e, f

def moves(equation: Equation) -> tuple[float, float]:
    a, b, c, d, e, f = equation
    top = f * a - e * b
    bottom = d * a - b * c

    second = top / bottom
    first = (e - c * second) / a
    return first, second

def token(a: int, b: int) -> int:
    return 3 * a + b

def contribution(equation: Equation) -> int:
    a, b = moves(equation)
    if a.is_integer() and b.is_integer():
        return token(int(a), int(b))
    return 0

def add_for_two(equation: Equation) -> Equation:
    a, b, c, d, e, f = equation
    e += 10000000000000
    f += 10000000000000
    return a, b, c, d, e, f


one = two = 0
for equation in parse("input"):
    one += contribution(equation)

    changed_equation = add_for_two(equation)
    two += contribution(changed_equation)

print("Part 1:", one)
print("Part 2:", two)
