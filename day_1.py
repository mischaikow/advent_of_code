## Day 1
## Calculate fuel requirement

## Take a file with a list of numbers, compute each one, and then sum them

def fuel_need(mass):
    return mass/3 - 2

def all_fuel_need(fuel_mass):
    if fuel_mass <= 0:
        return 0
    else:
        next_mass = fuel_mass/3 - 2
        if next_mass <= 0:
            return 0
        else:
            return next_mass + all_fuel_need(next_mass)


ships = open("day_1_1_input.txt", "r")

sum_raw = 0
sum_all = 0
for i in ships:
    mass = int(i.strip('\n'))
    raw_fuel = fuel_need(mass)
    sum_raw += fuel_need(mass)
    sum_all += all_fuel_need(mass)
    

print "Raw Fuel:", sum_raw
print "Total Fuel:", sum_all

