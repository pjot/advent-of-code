ev = 0
raw = 0
esc = 0
with open("input") as f:
    for l in f.readlines():
        l = l.strip()
        es = l.replace('"', '..').replace('\\', '..')
        es += '..'
        ev += len(eval(l))
        raw += len(l)
        esc += len(es)

print("Part 1:", raw - ev)
print("Part 2:", esc - raw)
