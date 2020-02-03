import itertools
import functools
import operator


packages = [
    1, 3, 5, 11, 13, 17, 19, 23, 29, 31,
    41, 43, 47, 53, 59, 61, 67, 71, 73, 79,
    83, 89, 97, 101, 103, 107, 109, 113,
]

def entanglement(combo):
    return functools.reduce(operator.mul, combo)

def weight(combo):
    return sum(combo)

def shortest_division(n):
    for i in range(1, len(packages)):
        working = []
        for x in itertools.combinations(packages, i):
            if weight(x) == weight(packages) / n:
                working.append(x)
        if working:
            return working


smallest = min(shortest_division(3), key=entanglement)
print("Part 1:", entanglement(smallest))

smallest = min(shortest_division(4), key=entanglement)
print("Part 2:", entanglement(smallest))
