from itertools import permutations


def iterate(pwd, i):
    p = i.split(' ')
    if p[0] == 'swap' and p[1] == 'position':
        p1 = int(p[2])
        p2 = int(p[5])
        pwd[p1], pwd[p2] = pwd[p2], pwd[p1]
    elif p[0] == 'swap' and p[1] == 'letter':
        l1 = pwd.index(p[2])
        l2 = pwd.index(p[5])
        pwd[l1], pwd[l2] = pwd[l2], pwd[l1]
    elif p[0] == 'reverse':
        p1 = int(p[2])
        p2 = int(p[4]) + 1
        one = pwd[0:p1]
        two = list(reversed(pwd[p1:p2]))
        three = pwd[p2:]
        pwd = one + two + three
    elif p[0] == 'rotate' and p[3] in ['step', 'steps']:
        steps = int(p[2])
        if p[1] == 'left':
            pwd = pwd[steps:] + pwd[:steps]
        else:
            pwd = pwd[-steps:] + pwd[:-steps]
    elif p[0] == 'move':
        pw = list(pwd)
        p1 = int(p[2])
        p2 = int(p[5])
        pp = pw[p1]
        pw = [v for i, v in enumerate(pwd) if i != p1]
        pw.insert(p2, pp)
        pwd = pw
    elif p[0] == 'rotate' and p[1] == 'based':
        l = p[6]
        i = pwd.index(l) + 1
        if i > 4:
            i += 1
        i = i % len(pwd)
        pwd = pwd[-i:] + pwd[:-i] 
    
    return pwd

def run(password, inputs):
    for i in inputs:
        password = iterate(password, i)
    return password

inputs = []
with open('input') as f:
    for l in f.readlines():
        inputs.append(l.strip())

password = list('abcdefgh')
print('Part 1:', ''.join(run(password, inputs)))

for test in permutations('fbgdceah'):
    if run(list(test), inputs) == list('fbgdceah'):
        print('Part 2:', ''.join(test))
        break