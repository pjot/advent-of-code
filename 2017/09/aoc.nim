import strutils

proc remove_garbage(s: string): (string, int) =
    var
        in_garbage = false
        cancel_next = false
        garbage = 0
        s = s.replace("!!", "")
        o = ""

    for c in s:
        if not cancel_next:
            if in_garbage and c != '!' and c != '>':
                inc garbage

            if c == '<':
                in_garbage = true
                cancel_next = false

            elif c == '>':
                if in_garbage:
                    in_garbage = false
                else:
                    o.add c

            elif not in_garbage:
                o.add c

        cancel_next = c == '!'

    return (o, garbage)

proc score(s: string): int =
    var level = 0
    for c in s:
        if c == '{':
            inc level
        if c == '}':
            result.inc level
            dec level


var (without_garbage, removed) = remove_garbage(readFile "input")
echo "Part 1: ", score without_garbage
echo "Part 2: ", removed

