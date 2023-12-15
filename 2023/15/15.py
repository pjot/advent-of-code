from collections import defaultdict

def parse(file):
    with open(file) as f:
        return f.read().strip().split(",")

def h(s):
    v = 0
    for c in s:
        v += ord(c)
        v *= 17
        v %= 256
    return v

def initialize(sequence):
    boxes = defaultdict(dict)
    for s in sequence:
        if s.endswith("-"):
            label = s[:-1]
            box = h(label)

            boxes[box] = {
                k: v for k, v in boxes[box].items()
                if k != label
            }
        else:
            label, focal_length = s.split("=")
            boxes[h(label)][label] = int(focal_length)

    return boxes

def focusing_power(boxes):
    power = 0
    for box, lenses in boxes.items():
        for slot, focal_length in enumerate(lenses.values()):
            power += (box + 1) * (slot + 1) * focal_length

    return power

sequence = parse("input")

print("Part 1:", sum(h(s) for s in sequence))
boxes = initialize(sequence)
print("Part 2:", focusing_power(boxes))

