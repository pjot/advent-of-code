import strutils

type
    Policy = object
        a, b: int
        c: char

    Combination = object
        policy: Policy
        password: string

proc parse(filename: string): seq[Combination] =
    var file = readFile filename
    file.stripLineEnd
    for line in file.splitLines:
        let 
            p = line.split
            password = p[2]
            c = p[1][0]
            ab = p[0].split('-')
            a = parseInt ab[0]
            b = parseInt ab[1]
        
        result.add Combination(
            policy: Policy(a: a, b: b, c: c),
            password: password
        )

func one(c: Combination): bool =
    let count = c.password.count(c.policy.c)

    c.policy.a <= count and count <= c.policy.b

func two(c: Combination): bool =
    let 
        a = c.password[c.policy.a - 1] == c.policy.c
        b = c.password[c.policy.b - 1] == c.policy.c

    a xor b

func solve(
    combinations: seq[Combination],
    valid: proc(c: Combination): bool
): int =
    for combination in combinations:
        if valid(combination):
            inc result

let combinations = parse "input.txt"

echo "Part 1: ", combinations.solve(one)
echo "Part 2: ", combinations.solve(two)