import strutils

var input = (splitLines (readFile "input.txt"))[0]

proc one(chars: string): int =
    for c in chars:
        if c == '(':
            inc result
        if c == ')':
            dec result

proc two(chars: string): int =
    for pos, c in chars:
        if c == '(':
            inc result
        if c == ')':
            dec result

        if result == -1:
            return pos

echo one input
echo two input
