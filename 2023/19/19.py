from functools import cache

def parse(file):
    workflows = {}
    parts = []
    with open(file) as f:
        a, b = f.read().split("\n\n")
        for line in a.splitlines():
            name, rules = line.strip().replace("}", "").replace("{", " ").split()
            workflows[name] = []
            for r in rules.split(","):
                if len(r) > 1 and r[1] in "<>":
                    pp = r.split(":")
                    rule = (r[1], int(pp[0][2:]), r[0], pp[1])
                else:
                    rule = ("=", r)
                workflows[name].append(rule)

        for line in b.splitlines():
            l = line.strip().replace("{", "").replace("}", "").split(",")
            part = {}
            for p in l:
                k, v = p.split("=")
                part[k] = int(v)
            parts.append(part)
    return workflows, parts

def score(part):
    return sum(part.values())

def evaluate(p, wf):
    for rule in wf:
        match rule:
            case "=", t:
                return t
            case ">", n, v, t:
                if p[v] > n:
                    return t
            case "<", n, v, t:
                if p[v] < n:
                    return t

def accepted(p, workflows):
    wf = "in"
    while True:
        wf = evaluate(p, workflows[wf])
        if wf == "A":
            return True
        if wf == "R":
            return False

workflows, parts = parse("input")

a = 0
for part in parts:
    if accepted(part, workflows):
        a += score(part)

print("Part 1:", a)

def count_valid(wf, valid):
    if wf == "R":
        return 0

    if wf == "A":
        return (
            (valid["x"][1] - valid["x"][0]) *
            (valid["m"][1] - valid["m"][0]) *
            (valid["a"][1] - valid["a"][0]) *
            (valid["s"][1] - valid["s"][0])
        )

    s = 0
    for rule in workflows[wf]:
        target = {}
        match rule:
            case "=", t:
                s += count_valid(t, valid)
                continue

            case ">", n, v, t:
                a, b = valid[v]
                target[v] = [n+1, b]
                valid[v] = [a, n+1]

            case "<", n, v, t:
                a, b = valid[v]
                target[v] = [a, n]
                valid[v] = [n, b]

        s += count_valid(t, dict(valid, **target))

    return s

valid = {
    "x": [1, 4001],
    "m": [1, 4001],
    "a": [1, 4001],
    "s": [1, 4001],
}
print("Part 2:", count_valid("in", valid))

