from collections import Counter


def parse_file(filename):
    with open(filename) as f:
        ints = f.readline().strip()
        program = [int(i) for i in ints]
        return program


def parse_image(data, height, width):
    layers = [[]]
    length = height * width
    layer = 0
    for i, value in enumerate(data):
        layers[layer].append(value)
        if (i + 1) % length == 0 and i != 0:
            layer += 1
            layers.append([])

    layers.pop()
    return layers


def count_digits(layer):
    c = Counter()
    for d in layer:
        c[d] += 1
    return c


def part1():
    layers = parse_image(parse_file("image.txt"), 25, 6)
    digits = [count_digits(l) for l in layers]
    lowest = float('inf')
    index = 0
    for i, dc in enumerate(digits):
        if dc[0] < lowest:
            lowest = dc[0]
            index = i

    return digits[index][1] * digits[index][2]


def part2():
    layers = list(parse_image(parse_file("image.txt"), 25, 6))
    for y in range(6):
        print()
        for x in range(25):
            for layer in layers:
                index = x + y * 25
                pixel = layer[index]
                if pixel != 2:
                    if pixel == 1:
                        print("*", end='')
                    if pixel == 0:
                        print(" ", end='')
                    break


print("Part 1:", part1())
print("Part 2:", end="")
part2()
