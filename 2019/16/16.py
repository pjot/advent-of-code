from math import ceil


def split(n):
    return [int(d) for d in str(n)]


def apply_phase(numbers, phase):
    multipliers = (
        [0] * phase +
        [1] * phase +
        [0] * phase +
        [-1] * phase
    )
    r = []
    for p, _ in enumerate(numbers):
        phase = p + 1
        multipliers = (
            [0] * phase +
            [1] * phase +
            [0] * phase +
            [-1] * phase
        )
        s = 0
        for i, d in enumerate(numbers):
            m_index = (i + 1) % len(multipliers)
            m = multipliers[m_index]
            new = d * m
            s += new
        r.append(abs(s) % 10)
    return r


inp = split(
    '597680928399277585651912986252151063' +
    '718901180514262508559247641944115280' +
    '0471870988640290343556962798248530192' +
    '16492408200598271610246316122900051063' +
    '04724846680415690183371469037418126383450370741078684974598662642' +
    '9567940128252714873292435831175378735653321667441288450068068787179559465341588373704519359197'+
    '90469815143341599820016469368684893122766857261426799636559525003877090579845725676481276977781270627558901433501'+
    '565337409716858949203430181103278194428546385063911239478804717744977998841434061688000383456176494210691861957243370'+
    '245170223862304663932874454624234226361642678259020094801774825694423060700312504286475305674864442250709029812379')

n = split('03036732577212944063491565474664')
m_len = len(n)
offset = int("".join(str(i) for i in n[:7]))
needed = 10000 * m_len - offset
mult = ceil(needed / m_len)
#print(needed, needed / m_len, mult)
#real_o = 
n = n * mult
#print("".join(str(i) for i in n))
for i in range(1, 101):
    print(i)
    n = apply_phase(n, i)
    #print(n)

#print("".join(str(i) for i in n))
print(n[needed:8])

#print(n[offset:8])