import strutils
import tables
import sets

type
    Bags = Table[string, Bag]

    Counts = Table[string, int]

    Content = object
        name: string
        count: int

    Bag = object
        name: string
        contains: seq[Content]

proc parse(filename: string): Bags =
    var file = readfile filename
    file.stripLineEnd

    for line in file.splitLines:
        var
            parts = line.split(" bags contain ")
            bag = Bag(
                name: parts[0],
                contains: @[],
            )
            contains = parts[1]

        if contains != "no other bags.":
            let parsed = contains
                .replace(".", "")
                .replace(" bags", "")
                .replace(" bag", "")
                .split(", ")
            for part in parsed:
                var bags = part.split(" ", 1)
                bag.contains.add Content(
                    count: parseint bags[0],
                    name: bags[1]
                )
        result[bag.name] = bag 

iterator canBeIn(bags: Bags, bag: string): string =
    for candidate in bags.values:
        for c in candidate.contains:
            if c.name == bag:
                yield candidate.name

proc ways(bags: Bags, bag: string): int =
    var 
        seen = initHashSet[string]()
        horizon = initHashSet[string]()

    horizon.incl bag

    while horizon.len > 0:
        var newHorizon = initHashSet[string]()

        for h in horizon:
            if h in seen:
                continue
            seen.incl h

            for n in bags.canBeIn(h):
                newHorizon.incl n

        horizon = newHorizon

    return seen.len - 1

func maybeCount(counts: Counts, bag: Bag): (bool, int) =
    var count = 0
    for content in bag.contains:
        if content.name in counts:
            count.inc content.count * (counts[content.name] + 1)
        else:
            return (false, 0)
    return (true, count)

func counts(bags: Bags, target: string): int =
    var counts = Counts()
    for bag in bags.values:
        if bag.contains.len == 0:
            counts[bag.name] = 0

    while bags.len > counts.len:
        for bag in bags.values:
            if bag.name in counts:
                continue
            
            let (worked, count) = counts.maybeCount(bag)
            if worked:
                counts[bag.name] = count

    return counts[target]

let bags = parse "input.txt"
echo "Part 1: ", bags.ways("shiny gold")
echo "Part 2: ", bags.counts("shiny gold")