import math

def parse(file):
    modules = {}
    with open(file) as f:
        for line in f.readlines():
            m, destinations = line.strip().split(" -> ")
            kind = m[0]
            if kind in "%&":
                name = m[1:]
            else:
                kind = ">"
                name = m
            destinations = destinations.split(", ")
            modules[name] = (kind, destinations)
    return modules

def initialize(modules):
    state = {}

    conjunctions = set()
    for m, (kind, _) in modules.items():
        if kind == "%":
            state[m] = 0
        if kind == "&":
            conjunctions.add(m)

    for m, (kind, destinations) in modules.items():
        conj = conjunctions & set(destinations)
        for mo in conj:
            s = state.get(mo, {})
            s[m] = 0
            state[mo] = s

    return state

def push_button(modules, state):
    signals = [("button", "broadcaster", 0)]
    sent = {0: 0, 1: 0}
    to_dt = set()

    while signals:
        new_signals = []
        for sender, target, signal in signals:
            sent[signal] += 1

            if target == "dt" and signal == 1:
                to_dt.add(sender)

            if target not in modules:
                continue
            kind, destinations = modules[target]

            if kind == ">":
                output = signal

            if kind == "%":
                if signal == 1:
                    continue
                s = state.get(target, 0)
                state[target] = 1 if s == 0 else 0
                output = state[target]

            if kind == "&":
                state[target][sender] = signal
                if all(v == 1 for v in state[target].values()):
                    output = 0
                else:
                    output = 1

            for d in destinations:
                new_signals.append((target, d, output))

        signals = new_signals

    return state, sent, to_dt

modules = parse("input")

state = initialize(modules)
low = high = 0
for i in range(1000):
    state, sent, _ = push_button(modules, state)
    low += sent[0]
    high += sent[1]

one = low * high

state = initialize(modules)
cycles = {}
to_dt = len(state["dt"])
for i in range(5000):
    state, _, p = push_button(modules, state)
    for c in p:
        cycles[c] = i + 1

    if len(cycles) == to_dt:
        break

two = math.lcm(*cycles.values())

print("Part 1:", one)
print("Part 2:", two)
