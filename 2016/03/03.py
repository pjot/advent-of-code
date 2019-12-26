import re
import sys


def parse_two(file):
    numbers = []
    with open(file) as f:
        lines = len(f.readlines())
    with open(file) as f:
        for l in range(int(lines / 3)):
            l1 = list(map(int, re.split(r' +', f.readline().strip())))
            l2 = list(map(int, re.split(r' +', f.readline().strip())))
            l3 = list(map(int, re.split(r' +', f.readline().strip())))
            for i in range(3):
                n = [l1[i], l2[i], l3[i]]
                numbers.append(n)
    return numbers


def parse_one(file):
    with open(file) as f:
        return [
            list(map(int, re.split(r' +', s.strip())))
            for s in f.readlines()
        ]


def is_triangle(numbers):
    s = sorted(numbers)
    return s[0] + s[1] > s[2]

    
def count_triangles(parser):
    numbers = parser('input')
    return len(list(filter(is_triangle, numbers)))


print('Part 1:', count_triangles(parse_one))
print('Part 2:', count_triangles(parse_two))