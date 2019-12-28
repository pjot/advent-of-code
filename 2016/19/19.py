def make_elfs(n):
    elfs = {}
    for i in range(n):
        elfs[i] = True
    return elfs


elfs = 3012210
e = make_elfs(elfs)
p = 0
zap = True
zapped = 0
while zapped < elfs - 1:
    if zapped % 1000 == 0:
        print('zapped', zapped)
    p = (p + 1) % elfs
    if e[p] is True:
        if zap:
            zapped += 1
            e[p] = False
            zap = False
        else:
            zap = True

print([k + 1 for k, v in e.items() if v is True])