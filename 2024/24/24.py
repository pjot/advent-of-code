import itertools
from collections import defaultdict
from dataclasses import dataclass

@dataclass
class Gate:
    a: str
    b: str
    operation: str
    target: str

    def operate(self, a, b):
        if self.operation == "OR":
            return a or b
        if self.operation == "XOR":
            return a ^ b
        if self.operation == "AND":
            return a and b


wires = {}
gates = {}

with open("input") as f:
    w, g = f.read().split("\n\n")

    for line in g.splitlines():
        a, operation, b, _, wire = line.strip().split()

        gates[wire] = Gate(a, b, operation, wire)
        wires[a] = None
        wires[b] = None
        wires[wire] = None

    for line in w.splitlines():
        wire, value = line.strip().split(": ")
        wires[wire] = value == "1"


def solve(wires, gates):
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
            g = gates[wire]
            a, b = wires.get(g.a), wires.get(g.b)
            if a is not None and b is not None:
                wires[wire] = g.operate(a, b)
                done.add(wire)

        none_wires -= done
        if len(done) == 0:
            return 1, 1, 2

    return number("x"), number("y"), number("z")

def two():
    bad = [
        w.target for w in gates.values()
        if w.target.startswith("z") and w.operation != "XOR" and w.target != "z45"
    ]

    for w in gates.values():
        if w.target in bad:
            continue
        if not w.target.startswith("z"):
            continue
        if w.target == "z00":
            continue

        gate_a = gates[w.a]
        gate_b = gates[w.b]

        for gate in [gate_a, gate_b]:
            if gate.operation == "XOR" and gate.a[0] not in "xy":
                bad.append(gate.target)

            if gate.operation == "OR":
                for sub_gate in [gates[gate.a], gates[gate.b]]:
                    if sub_gate.operation != "AND":
                        bad.append(sub_gate.target)

            if gate.operation == "AND" and gate.a[0] in "xy":
                if gate.a not in {"x00", "x44", "y00", "y44"}:
                    bad.append(gate.target)


    return ",".join((sorted(bad)))

x, y, z = solve(wires, gates)
print("Part 1:", z)
print("Part 2:", two())

