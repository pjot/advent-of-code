def comp(filename,part,memory,ball=[0,0],pad=[0,0]):
    p = [int(x) for x in open(filename).read().split(',')] 
    p += [0] * (memory - len(p))
    relative = 0
    index = 0
    o = [0, 3, 3, 1, 1, 2, 2, 3, 3, 1]
    output = []
    blocks = 0
    score = 0
    if part == 2:
        p[0] = 2
    while (p[index] != 99):
        modes = [int(x) for x in str(p[index])[:-2]][::-1] + [0,0,0]
        opcode = int(str(p[index])[-2:])
        position = [p[index+x+1] if modes[x]==1 else p[(relative if modes[x]==2 else 0)+p[index+x+1]] for x in range(o[opcode])]
        if opcode == 1:
            p[(relative if modes[2]==2 else 0)+p[index+3]] = position[0]+ position[1]
        elif opcode == 2:
            p[(relative if modes[2]==2 else 0)+p[index+3]] = position[0]* position[1]
        elif opcode == 3:
            if ball[0] < pad[0]:
                joy = -1
            elif ball[0] > pad[0]:
                joy = 1
            else:
                joy = 0
            p[(relative if modes[0] == 2 else 0) + p[index+1]] = joy #Input Value
        elif opcode == 4:
            output.append(position[0])
            if part == 1 and len(output) == 3:
                if output[2] == 2:
                    blocks += 1
                if output[2] == 3:
                    pad = [output[0],output[1]]
                if output[2] == 4:
                    ball = [output[0],output[1]]
                output = []
            if part == 2 and len(output) == 3:
                if output[0] == -1 and output[1] == 0:
                    score = output[2]
                elif output[2] == 3:
                    pad = [output[0],output[1]]
                elif output[2] == 4:
                    ball = [output[0],output[1]]
                output = []
        elif opcode == 5:
            index = (position[1]- 3 if position[0]!= 0 else index)
        elif opcode == 6:
            index = (position[1]- 3 if position[0]== 0 else index)
        elif opcode == 7:
            p[(relative if modes[2] == 2 else 0) + p[index+3]] = (1 if position[0]< position[1]else 0)
        elif opcode == 8:
            p[(relative if modes[2] == 2 else 0) + p[index+3]] = (1 if position[0]== position[1]else 0)
        elif opcode == 9:
            relative += position[0]
        index += o[opcode] + 1
    if part == 1:
        return blocks,pad,ball
    else:
        print("Part 2:",score)
filename = 'game.intcode'
print()
blocks,pad,ball  = comp(filename, 1, 10000)
print("Part 1:",blocks)
comp(filename, 2, 10000,ball,pad)
