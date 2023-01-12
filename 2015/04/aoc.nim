import md5
import strutils

proc firstStart(start: string): int =
    let input = "iwrupvqb"
    var i = 0
    while true:
        let m = $toMD5(input & $i)
        if m.startsWith start:
            return i
        inc i

echo "Part 1: ", firstStart "00000"
echo "Part 2: ", firstStart "000000"
