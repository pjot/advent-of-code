def parse(file):
    monkeys = []
    done = {}
    with open(file) as f:
        for line in f.readlines():
            line = line.strip().replace(":", "")
            p = line.split()
            if len(p) == 2:
                done[p[0]] = int(p[1])
            else:
                monkeys.append((p[0], p[2], p[1], p[3]))
    return monkeys, done

def solve(monkeys, done, special_root=False):
    while len(monkeys) > 0:
        monkeys, done = reduce(monkeys, done, special_root)
    return done["root"]

def reduce(monkeys, done, special_root=False):
    remove = []
    for m, action, a, b in monkeys:
        if a in done and b in done:
            a = done[a]
            b = done[b]

            if m == "root" and special_root:
                value = f"{b} - {a}"

            else:
                match action:
                    case "+": value = f"({a} + {b})"
                    case "-": value = f"({a} - {b})"
                    case "*": value = f"({a} * {b})"
                    case "/": value = f"({a} // {b})"

            done[m] = value
            remove.append(m)

    monkeys = [m for m in monkeys if m[0] not in remove]
    return monkeys, done

def binary_search(expr):
    h = 1
    while True:
        h *= 10
        r = eval(expr)
        if r > 0:
            break

    d = h // 2
    while True:
        r = eval(expr)

        if r == 0:
            return h

        h = h - d if r > 0 else h + d
        d = d // 2

        if d == 0:
            d = 1

monkeys, done = parse("input.txt")
root = solve(monkeys, done)

print("Part 1:", eval(root))

monkeys, done = parse("input.txt")
done["humn"] = "h"
root = solve(monkeys, done, True)

print("Part 2:", binary_search(root))
