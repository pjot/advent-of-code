import sequtils
import strutils

proc run(offsets: seq[int], new_value: proc(o, v: int): int): int =
    var 
        p = 0
        steps = 0
        o = offsets

    while true:
        if p > (len o) - 1 or p < 0:
            return steps

        var v = o[p]
        o[p] = new_value(o[p], v)
        p += v

        inc steps

var offsets = (splitLines readFile("input")).map(parseInt)

proc one(o, v: int): int = return succ v
proc two(o, v: int): int =
    if o > 2:
        pred v
    else:
        succ v


echo "Part 1: ", run(offsets, one)
echo "Part 2: ", run(offsets, two)