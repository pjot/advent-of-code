from collections import Counter


def parse_file(filename, pixels_per_layer):
    with open(filename) as f:
        ints = f.readline().strip()
        data = [int(i) for i in ints]

    layers = [[]]
    layer = 0
    for i, value in enumerate(data):
        layers[layer].append(value)
        if (i + 1) % pixels_per_layer == 0 and i != 0:
            layer += 1
            layers.append([])

    layers.pop()
    return layers


def count_digits(layer):
    c = Counter()
    for d in layer:
        c[d] += 1
    return c


layers = parse_file("image.txt", 25 * 6)
digits = [count_digits(l) for l in layers]
lowest = float('inf')
index = 0
for i, dc in enumerate(digits):
    if dc[0] < lowest:
        lowest = dc[0]
        index = i
print("Part 1:", digits[index][1] * digits[index][2])

print("Part 2:", end="")
for y in range(6):
    print()
    for x in range(25):
        for layer in layers:
            index = x + y * 25
            pixel = layer[index]
            if pixel == 1:
                print("*", end='')
                break
            if pixel == 0:
                print(" ", end='')
                break
