## Day 1
## Calculate fuel requirement

## Take a file with a list of numbers, compute each one, and then sum them

def fuel_need(mass):
    return mass/3 - 2

ships = open("input", "r")

sum = 0
for i in ships:
    mass = int(i.strip('\n'))
    sum += fuel_need(mass)

print sum

