import copy
from collections import defaultdict, deque

stacks = defaultdict(deque)

def read(stacks):
    tops = ""
    for stack in range(1, 10):
        if len(stacks[stack]) > 0:
            tops += stacks[stack].pop()
    return tops


with open("input.txt") as f:
    for line in f.readlines():
        line = line.rstrip()

        if line == "":
            one = stacks
            two = copy.deepcopy(stacks)
            continue

        elif line.startswith("move"):
            _, count, __, a, ___, b = line.split()
            a, b, count = int(a), int(b), int(count)

            t = deque()
            for _ in range(count):
                # part one
                one[b].append(one[a].pop())
                # part two
                t.appendleft(two[a].pop())

            two[b].extend(t)

        else:
            for stack in range(1, 10):
                start = (stack - 1) * 4
                if len(line) > start:
                    if line[start] == "[":
                        stacks[stack].appendleft(line[start+1])

print("Part 1:", read(one))
print("Part 2:", read(two))
