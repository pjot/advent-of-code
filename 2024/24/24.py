import itertools
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

    def parents(self, gates):
        return [gates[self.a], gates[self.b]]

values = {}
gates = {}

with open("input") as f:
    w, g = f.read().split("\n\n")

    for line in g.splitlines():
        a, operation, b, _, wire = line.strip().split()

        gates[wire] = Gate(a, b, operation, wire)
        values[a] = None
        values[b] = None
        values[wire] = None

    for line in w.splitlines():
        wire, value = line.strip().split(": ")
        values[wire] = value == "1"

def solve(values, gates):
    def number(v):
        my_values = [w for w in values.keys() if w.startswith(v)]
        word = ""
        for wire in sorted(my_values):
            c = "1" if values[wire] else "0"
            word = c + word
        return int(word, 2)

    none_values = {
        wire for wire, val in values.items() if val is None
    }

    while none_values:
        done = set()
        for wire in none_values:
            gate = gates[wire]
            a, b = values.get(gate.a), values.get(gate.b)
            if a is not None and b is not None:
                values[wire] = gate.operate(a, b)
                done.add(wire)

        none_values -= done

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

        for gate in w.parents(gates):
            if gate.operation == "XOR" and gate.a[0] not in "xy":
                bad.append(gate.target)

            if gate.operation == "OR":
                for sub_gate in gate.parents(gates):
                    if sub_gate.operation != "AND":
                        bad.append(sub_gate.target)

            if gate.operation == "AND" and gate.a[0] in "xy":
                if gate.a not in {"x00", "x44", "y00", "y44"}:
                    bad.append(gate.target)


    return ",".join((sorted(bad)))

x, y, z = solve(values, gates)
print("Part 1:", z)
print("Part 2:", two())

