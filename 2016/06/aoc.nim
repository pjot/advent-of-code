import strutils
import tables

proc parse(f: string): Table[int, string] =
    for i in 0 ..< 8:
        result[i] = ""
    
    var file = readFile f
    file.stripLineEnd
    for line in file.splitLines:
        for i, c in line:
            result[i].add c

func one(s: string): char =
    s.toCountTable.largest[0]

func two(s: string): char =
    s.toCountTable.smallest[0]

proc solve(find: proc(s: string): char): string =
    var columns = parse "input"
    for i in 0 ..< 8:
        result.add find(columns[i])
    

echo "Part 1: ", solve one
echo "Part 2: ", solve two