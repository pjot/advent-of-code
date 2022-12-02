def place(p):
    if p in "AX":
        return 0
    if p in "BY":
        return 1
    return 2

ONE = [
    #  r,   p,   s  <-- me
    [1+3, 2+6, 3+0], # r, them
    [1+0, 2+3, 3+6], # p
    [1+6, 2+0, 3+3], # s
]

TWO = [
    #  l,   d,   w  <-- me
    [3+0, 1+3, 2+6], # r, them
    [1+0, 2+3, 3+6], # p
    [2+0, 3+3, 1+6], # s
]

one = 0
two = 0

with open("input.txt") as f:
    for line in f.readlines():
        l = line.strip()
        them, me = l.split()
        them = place(them)
        me = place(me)

        one += ONE[them][me]
        two += TWO[them][me]

print("Part 1:", one)
print("Part 2:", two)
