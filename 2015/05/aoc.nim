import strutils

proc parse(filename: string): seq[string] =
    var file = readFile filename
    stripLineEnd file
    return splitLines file

proc vowels(s: string): int =
    for c in "aeiou":
        result.inc s.count(c)

proc duplicate(s: string): bool =
    for i in 1 .. (len s) - 1:
        if s[i] == s[i-1]:
            return true
    return false

proc magic(s: string): bool =
    for sub in ["ab", "cd", "pq", "xy"]:
        if sub in s:
            return true
    return false

proc isNice(s: string): bool =
    vowels(s) > 2 and duplicate(s) and not magic(s)

proc one(filename: string): int =
    for s in parse filename:
        if isNice s:
            inc result
        
echo "Part 1: ", one "input.txt"
