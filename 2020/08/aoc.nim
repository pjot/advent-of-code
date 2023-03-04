import strutils
import sets
import tables

type
    Kind = enum
        ACC
        NOP
        JMP

    Operation = object
        kind: Kind
        value: int

    Code = Table[int, Operation]

func kind(v: string): Kind =
    case v
    of "acc": return ACC
    of "nop": return NOP
    of "jmp": return JMP

proc parse(filename: string): Code =
    var file = readfile filename
    file.stripLineEnd

    var number = 0
    for line in file.splitLines:
        let p = line.split

        result[number] = Operation(
            kind: p[0].kind,
            value: parseint p[1],
        )
        inc number

func run(code: Code): (bool, int) =
    var
        acc = 0
        p = 0
        seen = initHashSet[int]()

    while p notin seen:
        seen.incl p

        if p notin code:
            return (true, acc)

        let op = code[p]
        case op.kind
        of ACC:
            acc.inc op.value
            p.inc
        of NOP:
            p.inc
        of JMP:
            p.inc op.value

    return (false, acc)

func swap(op: Operation): Operation =
    case op.kind
    of JMP: return Operation(kind: NOP, value: op.value)
    of NOP: return Operation(kind: JMP, value: op.value)
    else: return op

func swap(code: Code, place: int): Code =
    for p, c in code.pairs:
        if p == place:
            result[p] = c.swap
        else:
            result[p] = c

func two(code: Code): int =
    for p in code.keys:
        if code[p].kind == ACC:
            continue
        
        let (terminated, acc) = run code.swap(p)
        if terminated:
            return acc
        
let code = parse "input.txt"
let (_, one) = run code
echo "Part 1: ", one
echo "Part 2: ", two code