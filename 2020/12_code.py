"""Day 12 of the 2020 Advent of Code

Did fine on part 1, not so fine on part 2
"""

import math

def shipMove(instruct, shipSpot, shipDirect):
    if instruct[0] == 'N':
        shipSpot[0] += int(instruct[1:])
    elif instruct[0] == 'S':
        shipSpot[0] -= int(instruct[1:])
    elif instruct[0] == 'E':
        shipSpot[1] += int(instruct[1:])
    elif instruct[0] == 'W':
        shipSpot[1]-= int(instruct[1:])
    elif instruct[0] == 'L':
        shipDirect += int(instruct[1:])
    elif instruct[0] == 'R':
        shipDirect -= int(instruct[1:])
    elif instruct[0] == 'F':
        shipSpot[0] += int(instruct[1:]) * \
            int(math.sin(math.radians(shipDirect)))
        shipSpot[1] += int(instruct[1:]) * \
            int(math.cos(math.radians(shipDirect)))
    return shipSpot, shipDirect


def totalMove(instructions):
    shipSpot = [0, 0]
    shipDirect = 0
    for i in instructions:
        shipSpot, shipDirect = shipMove(i, shipSpot, shipDirect)
    print('Part 1:', abs(shipSpot[0]) + abs(shipSpot[1]))


def waypointMove(instruct, shipSpot, waypoint):
    d = instruct[0]
    v = int(instruct[1:])
    if d == 'N':
        waypoint[0] += v
    elif d == 'S':
        waypoint[0] -= v
    elif d == 'E':
        waypoint[1] += v
    elif d == 'W':
        waypoint[1] -= v
    elif d == 'L':
        if v == 270:
            waypoint[0], waypoint[1] = -1 * waypoint[1], waypoint[0]
        if v == 180:
            waypoint[0] *= -1
            waypoint[1] *= -1
        if v == 90:
            waypoint[0], waypoint[1] = waypoint[1], -1 * waypoint[0]
    elif d == 'R':
        if v == 90:
            waypoint[0], waypoint[1] = -1 * waypoint[1], waypoint[0]
        if v == 180:
            waypoint[0] *= -1
            waypoint[1] *= -1
        if v == 270:
            waypoint[0], waypoint[1] = waypoint[1], -1 * waypoint[0]
    elif d == 'F':
        shipSpot[0] += v * waypoint[0]
        shipSpot[1] += v * waypoint[1]
    return shipSpot, waypoint
        

def totalWavepoint(instructions):
    shipSpot = [0, 0]
    waypoint = [1, 10]
    for i in instructions:
        shipSpot, waypoint = waypointMove(i, shipSpot, waypoint)
    print('Part 2:', abs(shipSpot[0]) + abs(shipSpot[1]))

        
def readFile(fileName):
    with open(fileName) as f:
        raw = f.readlines()
    
    instructions_raw = open(fileName).read().strip().split('\n')
    instruction_set = [i.strip() for i in raw]
    return instruction_set

        
def main():
    instructions = readFile('input_12_1.txt')
    totalMove(instructions)
    totalWavepoint(instructions)
    return True


main()
