def convert(s):
    n = 0
    for i, c in enumerate(reversed(s)):
        if c == "=":
            c = -2
        elif c == "-":
            c = -1
        else:
            c = int(c)
        n += 5 ** i * c
    return n

def replace(s, i, c):
    l = list(s)
    l[i] = c
    return "".join(l)

file_sum = 0
with open("input.txt") as f:
    for line in f.readlines():
        file_sum += convert(line.strip())

snafu = "=" * 30
for digit, _ in enumerate(snafu):
    for c in "=-012":
        candidate = replace(snafu, digit, c)
        if convert(candidate) <= file_sum:
            snafu = candidate

snafu = snafu.lstrip("0")

print("Part 1:", snafu)
