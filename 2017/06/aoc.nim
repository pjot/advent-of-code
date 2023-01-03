import sets
import strutils
import sequtils

type Banks = seq[int]

proc rounds(banks: Banks): (int, Banks) =
    var banks = banks
    var seen = initHashSet[Banks]()
    var rounds = 0
    while banks notin seen:
        seen.incl banks
        inc rounds

        var biggest = 0
        var pos = 0
        for i, n in banks:
            if n > biggest:
                pos = i
                biggest = n

        banks[pos] = 0
        for s in 1 .. biggest:
            var p = (pos + s) mod (len banks)
            banks[p] = banks[p] + 1

    return (rounds, banks)

var file = readFile "input"
stripLineEnd file
var banks = toSeq(split file).map(parseint)

var (one, new_banks) = rounds banks
var (two, _) = rounds new_banks

echo "Part 1: ", one
echo "Part 2: ", two