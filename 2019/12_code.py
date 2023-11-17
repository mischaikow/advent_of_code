##  Day 12
##  Back to the math problems

##  Helper functions
# File importer
def readFile(fileName):
    moon_file = open(fileName, 'r')
    moon_lines_raw = moon_file.readlines()
    output = []
    for line in moon_lines_raw:
        line = line.replace('<x=','')
        line = line.replace(' y=','')
        line = line.replace(' z=','')
        line = line.replace('>','')
        line = line.split(',')
        output.append(list(map(int, line)))
    return output

# Compute energy
def energy(locations, velocities):
    # compute potential energy
    potentialEnergy = []
    for moon in locations:
        potentialEnergy.append(abs(moon[0]) + abs(moon[1]) + abs(moon[2]))
        
    # compute kinetic energy
    kineticEnergy = []
    for moon in velocities:
        kineticEnergy.append(abs(moon[0]) + abs(moon[1]) + abs(moon[2]))

    # compute total energy
    totalEnergy = []
    for i in range(len(locations)):
        totalEnergy.append(potentialEnergy[i] * kineticEnergy[i])
        
    totalEnergyValue = sum(totalEnergy)
    return totalEnergyValue


##  One time step, calculated
def timeStep(locations, velocities):
    # Compute gravity
    for i in range(len(locations)):
        for j in range(i+1,len(locations)):
            for step in range(3):
                if locations[i][step] > locations[j][step]:
                    velocities[i][step] -= 1
                    velocities[j][step] += 1
                elif locations[i][step] < locations[j][step]:
                    velocities[i][step] += 1
                    velocities[j][step] -= 1

    # Compute movement
    for i in range(len(locations)):
        for step in range(3):
            locations[i][step] += velocities[i][step]

    return locations, velocities


##  Take multiple steps and calculate energy
def multiStepEnergy(locations, velocities, stepCount):
    # run stepCount cycles
    for _ in range(stepCount):
        locations, velocities = timeStep(locations, velocities)
        print(energy(locations, velocities))

    

##  Take multiple steps and compare to the initial state
def multiStepRepeat(locations, velocities):
    checkLocations = [_.copy() for _ in locations]
    checkVelocities = [_.copy() for _ in velocities]
    counter = 0
    while True:
        locations, velocities = timeStep(locations, velocities)
        counter += 1
        if locations == checkLocations and velocities == checkVelocities:
            print("Hit:", counter)
            break
        else:
            print("Miss:", counter)
    
# start with manually entered plants
locations = readFile('input.txt')
velocities = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
multiStepEnergy(locations,velocities,1000)
#multiStepRepeat(locations, velocities)
