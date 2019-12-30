inputs = []
with open('input') as f:
    for line in f.readlines():
        parts = line.split('-')
        lo = int(parts[0])
        hi = int(parts[1])
        inputs.append((lo, hi))

def iterate(l):
    for lo, hi in inputs:
        if lo <= l <= hi:
            l = hi + 1
    return l

lowest = 0
l2 = iterate(lowest)
while l2 != lowest:
    lowest = l2
    l2 = iterate(lowest)

print('Part 1:', lowest)

merged = []
for lo, hi in sorted(inputs, key=lambda c: c[0]):
    found = False
    for i in range(len(merged)):
        l, h = merged[i]
        lo_found = l <= lo <= h
        hi_found = l <= hi <= h
        if lo_found or hi_found:
            found = True

        if hi_found and not lo_found:
            merged[i] = (lo, h)

        if lo_found and not hi_found:
            merged[i] = (l, hi)

    if not found:
        merged.append((lo, hi))
        
blacklisted = 0
for lo, hi in merged:
    blacklisted += hi - lo + 1

print('Part 2:', 4294967295 + 1 - blacklisted)
