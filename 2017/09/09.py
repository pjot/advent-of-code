def remove_garbage(s):
    s = s.replace('!!', '')
    o = ''
    garbage_count = 0
    garbage = False
    cancel = False
    for c in s:
        if garbage and not cancel and c != '!' and c != '>':
            garbage_count += 1

        if c == '!':
            cancel = True
        elif c == '<' and not cancel:
            garbage = True
            cancel = False
        elif c == '>' and not cancel:
            if garbage:
                garbage = False
            else:
                o += c
            cancel = False
        elif not garbage:
            o += c
            cancel = False
        else:
            cancel = False

    return o, garbage_count


def count_score(s):
    level = 0
    score = 0
    for c in s:
        if c == '{':
            level += 1
        if c == '}':
            score += level
            level -= 1
    return score


score = 0
removed = 0
with open('input') as f:
    for line in f.readlines():
        cleaned, garbage = remove_garbage(line.strip())
        score += count_score(cleaned)
        removed += garbage

print('Part 1:', score)
print('Part 2:', removed)