##  Day 12 - part 2
##  Had to look up the idea of using the greatest common divisor to
# check for cycles
import math

##  Helper functions
# File importer
def readFile(fileName):
    moon_file = open(fileName, 'r')
    moon_lines_raw = moon_file.readlines()
    output = []
    for line in moon_lines_raw:
        line = line.replace('<x=', '')
        line = line.replace(' y=', '')
        line = line.replace(' z=', '')
        line = line.replace('>', '')
        line = line.split(',')
        output.append(list(map(int, line)))
    return output

##  One time step, calculated for a single axis
def timeStepAxis(locations, velocities):
    # Compute gravity
    for i in range(len(locations)):
        for j in range(i+1, len(locations)):
            if locations[i] > locations[j]:
                velocities[i] -= 1
                velocities[j] += 1
            elif locations[i] < locations[j]:
                velocities[i] += 1
                velocities[j] -= 1

    # Compute movement
    for i in range(len(locations)):
        locations[i] += velocities[i]

    return locations, velocities

##  Take multiple steps for a single axis and return loop time
def findLoop(locations):
    originalLocations = locations.copy()
    originalVelocities = [0] * len(locations)
    velocities = [0] * len(locations)
    counter = 0
    while True:
        locations, velocities = timeStepAxis(locations, velocities)
        counter += 1
        if locations == originalLocations and \
           velocities == originalVelocities:
            return counter

##  Explore the space for x, y, and z:
def searchRepeats(fileName):
    locations = readFile(fileName)
    results = []
    for i in [0, 1, 2]:
        axisLoc = [_[i] for _ in locations]
        results.append(findLoop(axisLoc))
    print(results)

    inter = abs(results[0] * results[1]) // \
        math.gcd(results[0], results[1])
    final = abs(inter * results[2]) // math.gcd(inter, results[2])

    print(final)

searchRepeats('input.txt')
        
