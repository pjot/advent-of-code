def parse(file):
    inputs = []
    outputs = []
    with open(file) as f:
        for line in f.readlines():
            if not '|' in line:
                continue
            input, output = line.split(' | ')
            inputs.append(input.split())
            outputs.append(output.split())
    return inputs, outputs

inputs, outputs = parse('input.txt')

cnt = 0
for o in outputs:
    for d in o:
        if len(d) in [2, 3, 4, 7]:
            cnt +=1

print(cnt)
