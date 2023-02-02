import strutils
import tables

type
    Program = Table[int, int]

proc parse(filename: string): Program =
    let
        file = readFile filename
        code = file.splitLines()[0]
        numbers = code.split(',')

    for i, n in numbers:
        result[i] = parseInt(n)

proc run(code: Program, one, two: int): int =
    var
        mem = code
        pos = 0

    mem[1] = one
    mem[2] = two

    while code.hasKey(pos):
        let op = mem[pos]

        if op == 99:
            return mem[0]

        let
            a = mem[pos + 1]
            b = mem[pos + 2]
            target = mem[pos + 3]

        case op
        of 1:
            # add
            mem[target] = mem[a] + mem[b]
            pos.inc 4
        of 2:
            # multiply
            mem[target] = mem[a] * mem[b]
            pos.inc 4
        else:
            # shouldn't happen
            discard

    return mem[0]

func find(code: Program, value: int): int =
    for noun in 0 ..< 99:
        for verb in 0 ..< 99:
            if run(code, noun, verb) == value:
                return 100 * noun + verb


let code = parse "program.intcode"
echo "Part 1: ", run(code, 12, 2)
echo "Part 2: ", find(code, 19690720)
