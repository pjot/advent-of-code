import strutils
import algorithm

const MIN = 240920
const MAX = 789857

func hasDouble(s: string): bool =
    for i in 0 .. 4:
        let
            a = s[i]
            b = s[i+1]
        if a == b:
            return true
    return false

func hasUniqueDouble(s: string): bool =
    for i in 0 .. 2:
        let
            a = s[i]
            b = s[i+1]
            c = s[i+2]
            d = s[i+3]
        if a != b and b == c and c != d:
            return true

    if s[0] == s[1] and s[0] != s[2]: return true
    if s[4] == s[5] and s[4] != s[3]: return true

    return false

func increases(s: string): bool =
    sorted(s) == s
    
func one(s: string): bool =
    s.increases and s.hasDouble

func two(s: string): bool =
    s.increases and s.hasUniqueDouble

func valid(f: proc(s: string): bool): int =
    for i in MIN .. MAX:
        if f($i): inc result

echo "Part 1: ", valid one
echo "Part 2: ", valid two