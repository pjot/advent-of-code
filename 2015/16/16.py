REAL = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def parse(file):
    aunts = []
    with open(file) as f:
        for l in f.readlines():
            p = l.split(", ")
            s = {
                "name": p[0].split(" ")[1].replace(":", "")
            }
            for t in p:
                ts = t.split(": ")
                s[ts[-2]] = int(ts[-1])
            aunts.append(s)
    return aunts


def part_one(aunt):
    for k, v in REAL.items():
        if aunt.get(k) and aunt[k] != v:
            return False
    return True


def part_two(aunt):
    greater_than = ["cats", "trees"]
    less_than = ["pomeranians", "goldfish"]

    for k, v in REAL.items():
        av = aunt.get(k)
        if av is None:
            continue

        if k in greater_than:
            if not av > v:
                return False
        elif k in less_than:
            if not av < v:
                return False
        else:
            if av != v:
                return False
    return True


aunts = parse("input")
for aunt in aunts:
    if part_one(aunt):
        print("Part 1:", aunt["name"])
    if part_two(aunt):
        print("Part 2:", aunt["name"])
