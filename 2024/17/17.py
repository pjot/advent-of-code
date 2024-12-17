Code = list[int]
Registers = tuple[int, int, int]

def parse(file: str) -> tuple[Code, Registers]:
    a = b = c = 0
    code = []
    with open("input") as f:
        lines = f.readlines()
        a = int(lines[0].split()[2])
        b = int(lines[1].split()[2])
        c = int(lines[2].split()[2])
        code = [
            int(n) for n in
            lines[4].split()[1].split(",")
        ]
    return code, (a, b, c)

def run(code: Code, registers: Registers) -> list[int]:
    a, b, c = registers
    pointer = 0
    out = []

    def combo(o):
        if o in {0, 1, 2, 3}:
            return o
        if o == 4:
            return a
        if o == 5:
            return b
        if o == 6:
            return c

    while True:
        if pointer + 1 > len(code):
            break
        op = code[pointer]
        operand = code[pointer + 1]

        if op == 0:
            # adv
            numerator = a
            denominator = 2 ** combo(operand)
            a = int(numerator / denominator)
        if op == 1:
            # bxl
            b = b ^ operand
        if op == 2:
            # bst
            b = combo(operand) % 8
        if op == 3:
            # jnz
            if a != 0 and pointer != operand:
                pointer = operand
                continue
        if op == 4:
            # bxc
            b = b ^ c
        if op == 5:
            # out
            out.append(combo(operand) % 8)
        if op == 6:
            # bdv
            numerator = a
            denominator = 2 ** b
            b = int(numerator / denominator)
        if op == 7:
            # cdv
            numerator = a
            denominator = 2 ** b
            c = int(numerator / denominator)

        pointer += 2

    return out

def decompiled(a: int) -> list[int]:
    out = []
    b = c = 0
    while a != 0:

        b = a % 8
        b = b ^ 6
        c = int(a / (2 ** b))
        b = b ^ c
        b = b ^ 7
        a = int(a / (2 ** 3))

        out.append(b % 8)

    return out

def find_quine(code: Code) -> int:
    """
        Comment for future me.

        The decompiled program for my input is above. The interesting
        thing is that it's a loop that shrinks `a` every iteration and
        runs until a is 0. It does this by updating `a` based on `a % 8`
        which means each iteration starts by ignoring the last digit
        (base 8). Thus each number in the output only depends on the
        number to the left of their place in `a` which means we can find
        `a` by iterating left-to-right until we find a match for the
        next position. Sometimes there are multiple options, so I added
        some backtracking if it ends up not being able to solve a digit.
    """
    solution = 0
    current = len(code)
    start_position = 0

    while current > 0:
        target = code[current - 1]

        found_match = False
        for n in range(start_position, 8):
            # Add the digit `n` to the end of solution
            attempt = solution * 8 + n

            output = run(code, (attempt, 0, 0))

            if output and output[0] == target:
                # Match! Update solution
                solution = solution * 8 + n
                # Go to next position
                current -= 1
                start_position = 0

                found_match = True
                break

        if not found_match:
            # Need to backtrack, start with last digit + 1
            start_position = (solution % 8) + 1
            current += 1
            # Remove last digit
            solution = solution // 8

    return solution

def pretty(output: list[int]) -> str:
    return ",".join(str(n) for n in output)

code, registers = parse("input")

print("Part 1:", pretty(run(code, registers)))
print("Part 2:", find_quine(code))
