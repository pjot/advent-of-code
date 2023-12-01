numbers = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

def extract_numbers(s):
    numbers = [c for c in s if c.isdigit()]
    return int(numbers[0] + numbers[-1])


with open("input") as f:
    one = two = 0
    for line in f.readlines():
        one += extract_numbers(line)

        for n, v in enumerate(numbers):
            line = line.replace(v, f"{v}{n+1}{v}")

        two += extract_numbers(line)

print("Part 1:", one)
print("Part 2:", two)
