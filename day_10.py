##  Day 10
##  Another math problem?
import math

## My thinking is that I will visit the astroids one at a time, starting in
# the top left corner, and progressing row-by-row. Each astroid then explores
# all of unexplored space and checking if visibility is maintained. If an
# asteroid is encountered, visibility is checked.

##  the first value is up-down
##  the second value is left-right

##  Helper functions
# Map importer, takes file name as input and returns a 2-d array
def readMap(fileName):
    aFile = open(fileName, 'r')
    output = aFile.readlines()
    for i in range(len(output)):
        output[i] = output[i].replace('\n', '')
    return output
    
# Create a list of all my asteroids and set their "hits" to zero
def asteroidHitList(twoArray):
    output = []
    for i in range(len(twoArray)):
        for j in range(len(twoArray[0])):
            if twoArray[i][j] == '#':
                output.append([i, j ,0])
    return output

# Create a list of asteroids relative to a nexus
def asteroidRelativeList(twoArray, homeBase):
    output = []
    for i in range(len(twoArray)):
        for j in range(len(twoArray[0])):
            if twoArray[i][j] == '#':
                distance = abs(i - homeBase[0]) + abs(j - homeBase[1])
                if j > homeBase[1]:
                    angle = math.atan((i - homeBase[0]) / (j - homeBase[1]))
                elif j < homeBase[1]:
                    angle = math.pi + \
                        math.atan((i - homeBase[0]) / (j - homeBase[1]))
                elif i < homeBase[0]:
                    angle = -math.pi/2
                elif i > homeBase[0]:
                    angle = math.pi/2
                    
                if distance != 0:
                    output.append((i, j, distance, angle))
    return output

def distanceKey(anAsteroid):
    return anAsteroid[2]

def angleKey(anAsteroid):
    return anAsteroid[3]


##  Methods
# Given an asteroid, check other asteroids to see if they can see each other
def sightCheck(pointer, astList, astMap):
    delta = [0, 0]
    for i in range(pointer+1, len(astList)):
        delta[0] = astList[i][0] - astList[pointer][0]
        delta[1] = astList[i][1] - astList[pointer][1]
        opportunities = math.gcd(delta[0], delta[1])
        if opportunities == 1:
            astList[i][2] += 1
            astList[pointer][2] += 1
        else:
            for count in range(1, opportunities):
                iCoord = astList[pointer][0] + delta[0]*count//opportunities
                jCoord = astList[pointer][1] + delta[1]*count//opportunities
                if astMap[iCoord][jCoord] == '#':
                    break
                if count == opportunities-1:
                    astList[i][2] += 1
                    astList[pointer][2] += 1
    return astList

# Loop through all the asteroids in our list
def compAsteroids(fileName):
    astMap = readMap(fileName)
    astList = asteroidHitList(astMap)
    for pointer in range(len(astList)):
        astList = sightCheck(pointer, astList, astMap)
    return astList

# Call compAsteroids and return the max value
def asteroidTarget(fileName):
    astList = compAsteroids(fileName)
    maxHit = max([_[2] for _ in astList])
    for anAsteroid in astList:
        if anAsteroid[2] == maxHit:
            print(anAsteroid)
            break

# Loop through the potential laser targets and hit if possible
def laserShooter(relativeList):
    relativeList.sort(key = distanceKey)
    relativeList.sort(key = angleKey)

    counter = 0
    asteroidsPopped = 0 
    lastAngle = -5
    while True:
        if counter >= len(relativeList):
            counter = 0
            lastAngle = -5

        if lastAngle == relativeList[counter][3]:
            counter += 1
        else:
            if asteroidsPopped == 199:
                return relativeList.pop(counter)
            else:
                lastAngle = relativeList.pop(counter)[3]
                print(lastAngle)
                asteroidsPopped += 1
            

asteroidTarget('input.txt')
relativeList = asteroidRelativeList(readMap('input.txt'), (25,37))
#relativeList = asteroidRelativeList(readMap('input_test.txt'), (2,2))
print(laserShooter(relativeList))
