import math


def iterate(m):
    return int(math.floor(m / 3)) - 2


def fuel_for_mass(m):
    total = 0
    while m > 0:
        m = iterate(m)
        if m > 0:
            total += m
    return total


total_fuel = 0
partial_fuel = 0
with open('masses.txt') as masses:
    for l in masses.readlines():
        total_fuel += fuel_for_mass(int(l))
        partial_fuel += iterate(int(l))

print 'part 1:', partial_fuel
print 'part 2:', total_fuel
