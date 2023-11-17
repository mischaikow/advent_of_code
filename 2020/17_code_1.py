"""2020 Advent of Code - Day 17 Part 1

3d cube: status[x][y][z]
"""

def readFile(fileName, steps):
    with open(fileName) as f:
        start = f.read().strip().split('\n')

    for i in range(len(start)):
        start[i] = (['.'] * (steps+2)) + list(start[i]) + (['.'] * (steps+2))
    plane = [['.'] * len(start[0]) for _ in range(steps+2)] \
            + start \
            + [['.'] * len(start[0]) for _ in range(steps+2)]
    
    result = [[(['.'] * len(plane[0])) for _ in range(len(plane))] \
            for _ in range(2*steps + 5)]
    result[steps + 2] = plane
    return result


def neighborCount(x, y, z, status):
    count = 0
    for x_t in range(x-1, x+2):
        for y_t in range(y-1, y+2):
            for z_t in range(z-1, z+2):
                if not all([x_t == x, y_t == y, z_t == z]):
                    if status[x_t][y_t][z_t] == '#':
                        count += 1
    return count


def takeSteps(status, steps):
    for a_step in range(steps):
        count_measure = [[[0] * len(status[0][0]) \
                for _ in range(len(status[0]))] \
                for _ in range(len(status))]
        for x in range(1, len(status)-1):
            for y in range(1, len(status[0])-1):
                for z in range(1, len(status[0][0])-1):
                    count_measure[x][y][z] = neighborCount(x, y, z, status)

        for x in range(len(status)):
            for y in range(len(status[0])):
                for z in range(len(status[0][0])):
                    if status[x][y][z] == '.' \
                            and count_measure[x][y][z] == 3:
                        status[x][y][z] = '#'
                    elif status[x][y][z] == '#' \
                            and count_measure[x][y][z] < 2:
                        status[x][y][z] = '.'
                    elif status[x][y][z] == '#' \
                            and count_measure[x][y][z] > 3:
                        status[x][y][z] = '.'

    count = 0
    for x in range(len(status)):
        for y in range(len(status[0])):
            for z in range(len(status[0][0])):
                if status[x][y][z] == '#':
                    count += 1

    return count


def main():
    steps = 6
    start_cube = readFile('input_17_1.txt', steps)
    print('Part 1:', takeSteps(start_cube, steps))
    return None


main()
