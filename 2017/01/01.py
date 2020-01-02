def captcha_one(s):
    cnt = 0
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            cnt += int(s[i])
    if s[0] == s[-1]:
        cnt += int(s[0])
    return cnt


def captcha_two(s):
    l = len(s)
    cnt = 0
    for i in range(len(s)):
        if s[i] == s[(i + l//2) % l]:
            cnt += int(s[i])
    return cnt


with open('input') as f:
    s = f.readline().strip()


print('Part 1:', captcha_one(s))
print('Part 2:', captcha_two(s))