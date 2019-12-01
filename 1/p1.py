import math


def fuel_for_mass(m):
    return int(math.floor(m / 3) - 2)


total_fuel = 0
with open('masses.txt') as masses:
    for l in masses.readlines():
        total_fuel += fuel_for_mass(int(l))

print 'total fuel', total_fuel
