import math


def fuel_required(mass):
    fuel = math.floor(int(mass) / 3) - 2
    return fuel


total = 0

with open("day_1_input.txt", "r") as f:
    input = f.readlines()

for module in input:
    f = fuel_required(module)
    total += f

print(total)
