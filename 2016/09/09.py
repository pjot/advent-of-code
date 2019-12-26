def decompress(s, recursive=False):
    l = 0
    pos = 0
    while pos < len(s):
        c = s[pos]
        if c == '(':
            end = 1
            while s[pos + end] != ')':
                end += 1

            dim = s[pos+1:pos+end]
            parts = dim.split('x')
            length = int(parts[0])
            repeats = int(parts[1])

            part = s[pos+end+1:pos+end+1+length]
            if recursive:
                part = decompress(part, recursive=True)
            else:
                part = len(part)
            repeated = part * repeats
            l += repeated
            pos += end + 1 + length
        else:
            l += 1
            pos += 1
    return l

one = 0
two = 0
with open('input') as f:
    for line in f.readlines():
        one += decompress(line.strip())
        two += decompress(line.strip(), recursive=True)

print('Part 1:', one)
print('Part 2:', two)

