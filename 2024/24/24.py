import itertools
from collections import defaultdict

wires = {}
gates = {}

with open("input") as f:
    w, g = f.read().split("\n\n")

    for line in g.splitlines():
        a, operation, b, _, wire = line.strip().split()

        gates[wire] = (a, operation, b)
        wires[a] = None
        wires[b] = None
        wires[wire] = None

    for line in w.splitlines():
        wire, value = line.strip().split(": ")
        wires[wire] = value == "1"

def operate(a, b, operation):
    if operation == "OR":
        return a or b
    if operation == "XOR":
        return a ^ b
    if operation == "AND":
        return a and b

def solve(wires, gates):
    def evaluate(wire):
        a, op, b = gates[wire]

        if wires.get(a) is None:
            wires[a] = evaluate(a)
        if wires.get(b) is None:
            wires[b] = evaluate(b)

        wires[wire] = operate(wires[a], wires[b], op)

    def number(v):
        my_wires = [w for w in wires.keys() if w.startswith(v)]
        word = ""
        for wire in sorted(my_wires):
            c = "1" if wires[wire] else "0"
            word = c + word
        return int(word, 2)

    none_wires = {wire for wire, val in wires.items() if val is None}

    while none_wires:
        done = set()
        for wire in none_wires:
            a, op, b = gates[wire]
            if wires[a] is not None and wires[b] is not None:
                wires[wire] = operate(wires[a], wires[b], op)
                done.add(wire)

        none_wires -= done
        if len(done) == 0:
            return 1, 1, 2

    return number("x"), number("y"), number("z")

def two():
    bad = [
        w for w, g in gates.items()
        if w.startswith("z") and g[1] != "XOR" and w != "z45"
    ]

    xor_not_xyz = [
        w for w, g in gates.items()
        if g[1] == "XOR" and w[0] not in "xyz"
    ]



    gat = sorted(gates.items())
    for g, v in gat:
        if g.startswith("z") and g not in bad and g != "z00":
            def f(va, ga):
                a, b, c = ga
                return f"({a} {b} {c} - {va})"

            a, b = v[0], v[2]
            ga = gates.get(a)
            gb = gates.get(b)
            gg = [f(a, gates.get(a)), f(b, gates.get(b))]
            gg = list(sorted(gg))
            subgr = ""
            if ga[1] == "XOR" and ga[0][0] not in "xy":
                bad.append(a)
            if gb[1] == "XOR" and gb[0][0] not in "xy":
                bad.append(b)

            for i in [0, 2]:
                wir = v[i]
                gatt = gates[wir]
                if gatt[1] == "AND" and gatt[0][0] in "xy" and gatt[0] not in {"x00", "y00"}:
                    if gatt[0] in {"x44", "y44"}:
                        continue
                    #print(gatt)
                    bad.append(wir)
                    #print("bad", wir, gatt)
            for gr in [ga, gb]:
                if gr[1] == "OR":
                    for i in [0, 2]:
                        wir = gr[i]
                        gatt = gates[wir]
                        if gatt[1] != "AND":
                            bad.append(wir)
                            #print("bad", wir, gatt)

                    ww = [
                        f(gr[0], gates.get(gr[0])),
                        f(gr[2], gates.get(gr[2])),
                    ]
                    ww.sort()
                    subgr += "|" + " - ".join(ww) + "|"
            #print(g, gg[0], v[1], gg[1], subgr)

    return ",".join((sorted(bad)))

x, y, z = solve(wires, gates)
print("Part 1:", z)
print("Part 2:", two())
