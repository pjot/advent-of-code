import strutils

type
    Group = seq[string]

proc parse(filename: string): seq[Group] =
    var file = readfile filename
    file.stripLineEnd
    for group in file.split("\n\n"):
        result.add group.splitLines

func letters(person: string): set[char] =
    for c in person:
        result.incl c

func union(group: Group): int =
    var seen: set[char]
    for person in group:
        seen = seen + letters(person)
    return seen.card

func intersection(group: Group): int =
    var seen = Letters
    for person in group:
        seen = seen * letters(person)
    return seen.card

func one(groups: seq[Group]): int =
    for group in groups:
        result.inc group.union

func two(groups: seq[Group]): int =
    for group in groups:
        result.inc group.intersection

let groups = parse "input.txt"

echo "Part 1: ", one(groups)
echo "Part 2: ", two(groups)