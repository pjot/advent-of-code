import tables
import strutils

var register = initTable[string, int]()
let lines = splitLines (readFile "input")

proc largest(t: Table[auto, int]): int =
    for v in t.values:
        result = max(result, v)

proc condition(c: string, a, b: int): bool =
    case c
    of "<":
        return a < b
    of ">":
        return a > b
    of "<=":
        return a <= b
    of ">=":
        return a >= b
    of "!=":
        return a != b
    of "==":
        return a == b

var biggest = 0
for line in lines:
    let 
        p = split line
        target = p[0]
        action = p[1]
        amount = parseint p[2]
        a = register.getOrDefault p[4]
        cmp = p[5]
        b = parseint p[6]

    if condition(cmp, a, b):
        let current = register.getOrDefault target
        case action
        of "inc":
            register[target] = current + amount
        of "dec":
            register[target] = current - amount
    
    biggest = max(biggest, largest register)

echo "Part 1: ", largest register
echo "Part 2: ", biggest