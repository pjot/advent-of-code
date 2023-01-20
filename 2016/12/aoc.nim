import strutils
import tables

type
    Register = Table[string, int]
    Program = seq[string]

func isNumber(x: string): bool =
  try:
    discard parseInt(x)
    result = true
  except ValueError:
    result = false

proc parse(f: string): Program =
    var file = readFile f
    file.stripLineEnd
    return file.splitLines

func solve(code: Program, r: var Register): int =
    var curr = 0
    while curr < code.len:
        let p = code[curr].split
        case p[0]
            of "jnz":
                let
                    a = p[1]
                    n = parseInt p[2]
                    c = if isNumber(a): parseInt a else: r[a]

                if c == 0:
                    inc curr
                else:
                    curr.inc n
            of "inc":
                let a = p[1]
                inc r[a]
                inc curr
            of "dec":
                let a = p[1]
                dec r[a]
                inc curr
            of "cpy":
                if isNumber(p[1]):
                    let
                        a = p[2]
                        n = parseInt p[1]
                    r[a] = n
                else:
                    let
                        a = p[1]
                        b = p[2]
                    r[b] = r[a]
                inc curr
    return r["a"]

var one = [("a", 0), ("b", 0), ("c", 0), ("d", 0)].toTable
var two = [("a", 0), ("b", 0), ("c", 1), ("d", 0)].toTable

let code = parse "input"
echo "Part 1: ", solve(code, one)
echo "Part 2: ", solve(code, two)
