def parse_dimensions(d):
    l, w, h = d.split("x")
    return int(l), int(w), int(h)


def paper(l, w, h):
    a1 = w * h
    a2 = w * l
    a3 = h * l
    return 2 * (a1 + a2 + a3) + min(a1, a2, a3)


def ribbon(l, w, h):
    sides = sorted([l, w, h])
    return l * w * h + 2 * sides[0] + 2 * sides[1]


with open("input.txt") as f:
    gifts = [parse_dimensions(line) for line in f.readlines()]

print("Part 1:", sum(paper(*gift) for gift in gifts))
print("Part 2:", sum(ribbon(*gift) for gift in gifts))