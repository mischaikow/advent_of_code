"""Day 11 of the Advent of Code


"""

def readFile(fileName):
    with open(fileName) as f:
        raw = f.readlines()
    polished = [list(x.strip()) for x in raw]
    for x in polished:
        x.insert(0, 'B')
        x.append('B')
    polished.insert(0, ['B'] * len(polished[0]))
    polished.append(['B'] * len(polished[0]))
    return polished


def modelCycle(aTable):
    occu_count = [[0] * len(aTable[0]) for x in aTable]
    for i in range(1, len(aTable)-1):
        for j in range(1, len(aTable[i])-1):
            if aTable[i][j] == '#':
                occu_count[i-1][j-1] += 1
                occu_count[i-1][j+1] += 1
                occu_count[i-1][j] += 1
                occu_count[i+1][j-1] += 1
                occu_count[i+1][j+1] += 1
                occu_count[i+1][j] += 1
                occu_count[i][j-1] += 1
                occu_count[i][j+1] += 1

    change = False
    for i in range(1, len(aTable)-1):
        for j in range(1, len(aTable[i])-1):
            if aTable[i][j] == '#' and occu_count[i][j] >= 4:
                aTable[i][j] = 'L'
                change = True
            elif aTable[i][j] == 'L' and occu_count[i][j] == 0:
                aTable[i][j] = '#'
                change = True

    return change


def goToStable(aTable):
    changed = True
    count = 0
    while changed:
        changed = modelCycle(aTable)
    for i in aTable:
        for j in i:
            if j == '#':
                count += 1
    return count


def modelCycleSight(aTable):
    occu_count = [[0] * len(aTable[0]) for x in aTable]

    def arrowCheck(x, x_delta, y, y_delta):
        while aTable[x][y] != 'B':
            x += x_delta
            y += y_delta
            if aTable[x][y] == '#' or aTable[x][y] == 'L':
                occu_count[x][y] += 1
                return None
        return None

    for i in range(1, len(aTable)-1):
        for j in range(1, len(aTable[i])-1):
            if aTable[i][j] == '#':
                arrowCheck(i, -1, j, -1)
                arrowCheck(i, -1, j, 1)
                arrowCheck(i, -1, j, 0)
                arrowCheck(i, 1, j, -1)
                arrowCheck(i, 1, j, 1)
                arrowCheck(i, 1, j, 0)
                arrowCheck(i, 0, j, -1)
                arrowCheck(i, 0, j, 1)
    
    change = False
    for i in range(1, len(aTable)-1):
        for j in range(1, len(aTable[i])-1):
            if aTable[i][j] == '#' and occu_count[i][j] >= 5:
                aTable[i][j] = 'L'
                change = True
            elif aTable[i][j] == 'L' and occu_count[i][j] == 0:
                aTable[i][j] = '#'
                change = True

    return change


def goToStableSight(aTable):
    changed = True
    count = 0
    while changed:
        print(aTable[7][2:15])
        changed = modelCycleSight(aTable)
    for i in aTable:
        for j in i:
            if j == '#':
                count += 1
    return count






def main():
    seat_map = readFile('input_11_1.txt')
    print('Part 1:', goToStable(seat_map))
    seat_map = readFile('input_11_1.txt')
    print('Part 2:', goToStableSight(seat_map))
    return None


main()
