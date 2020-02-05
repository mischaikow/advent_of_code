##  Day 15
##  The Interpreter has to control a repair droid

##  Helper functions:
# Pull a specific digit from a number
def digit(number, n):
    return number // 10**(n-1) % 10

# Read a value, even if it's from outside a list's bounds
# Only for use by the Interpreter
def pullValue(iList, address):
    if address >= len(iList):
        return 0
    elif address < 0:
        raise Exception('Out of bounds memory call')
    else:
        return iList[address]

# Perform parameter reads
def readParameter(iList, mode, address, relativeBase = None):
    if mode == 0:
        return pullValue(iList, pullValue(iList, address))
    elif mode == 1:
        return pullValue(iList, address)
    elif mode == 2:
        return pullValue(iList, relativeBase + pullValue(iList, address))
    else:
        raise Exception('Incorrect mode selectied')

# Perform parameter writes
def writeParameter(iList, mode, address, value, relativeBase = None):
    if mode == 0:
        if address >= len(iList):
            iList.extend([0] * (address - len(iList) + 1))
        elif address < 0:
            raise Exception('Out of bounds memory call')
        iList[address] = value
    elif mode == 2:
        if address + relativeBase >= len(iList):
            iList.extend([0] * (address + relativeBase - len(iList) + 1))
        elif address + relativeBase < 0:
            raise Exception('Out of bounds memory call')
        iList[address + relativeBase] = value
    return iList

# Read and interpret the file
def instructFileRead(fileName):
    command_file = open(fileName, 'r')
    commands_raw = command_file.readline().split(',')
    commands_raw[-1] = commands_raw[-1].replace('\n', '')

    return list(map(int, commands_raw))



###  The Interpreter  ###
def interpreter(iList, signal = 0, pointer = 0, relativeBase = 0):

    while True:

        ##  Halt command
        if iList[pointer] == 99:
            return None

        opcode = 10*digit(iList[pointer], 2) + digit(iList[pointer], 1)
        
        ##  Addition
        if opcode == 1:
            a = readParameter(iList, digit(iList[pointer], 3), pointer+1, \
                              relativeBase)
            b = readParameter(iList, digit(iList[pointer], 4), pointer+2, \
                              relativeBase)
            writeParameter(iList, digit(iList[pointer], 5), \
                           pullValue(iList, pointer+3), a + b, relativeBase)
            pointer += 4

        ##  Multiplication
        elif opcode == 2:
            a = readParameter(iList, digit(iList[pointer], 3), pointer+1, \
                              relativeBase)
            b = readParameter(iList, digit(iList[pointer], 4), pointer+2, \
                              relativeBase)
            writeParameter(iList, digit(iList[pointer], 5), \
                           pullValue(iList, pointer+3), a * b, relativeBase)
            pointer += 4

        ##  Input
        elif opcode == 3:
            writeParameter(iList, digit(iList[pointer], 3), \
                           pullValue(iList, pointer+1), signal, relativeBase)
            pointer += 2

        ##  Output
        elif opcode == 4:
            return iList, signal, pointer+2, relativeBase, \
                readParameter(iList, digit(iList[pointer], 3), pointer+1, relativeBase)

        ##  Not Equal to Zero
        elif opcode == 5:
            if readParameter(iList, digit(iList[pointer], 3), pointer+1, \
                             relativeBase) != 0:
                pointer = readParameter(iList, digit(iList[pointer], 4), \
                                        pointer+2, relativeBase)
            else:
                pointer += 3

        ##  Equal to Zero
        elif opcode == 6:
            if readParameter(iList, digit(iList[pointer], 3), pointer+1, \
                             relativeBase) == 0:
                pointer = readParameter(iList, digit(iList[pointer], 4), \
                                        pointer+2, relativeBase)
            else:
                pointer += 3

        ##  Less Than
        elif opcode == 7:
            if readParameter(iList, digit(iList[pointer], 3), pointer+1, \
                             relativeBase) < \
               readParameter(iList, digit(iList[pointer], 4), pointer+2, \
                             relativeBase):
                writeParameter(iList, digit(iList[pointer], 5), \
                               pullValue(iList, pointer+3), 1, relativeBase)
            else:
                writeParameter(iList, digit(iList[pointer], 5), \
                               pullValue(iList, pointer+3), 0, relativeBase)
            pointer += 4

        ##  Equal
        elif opcode == 8:
            if readParameter(iList, digit(iList[pointer], 3), pointer+1, \
                             relativeBase) == \
               readParameter(iList, digit(iList[pointer], 4), pointer+2, \
                             relativeBase):
                writeParameter(iList, digit(iList[pointer], 5), pullValue(iList, pointer+3), 1, relativeBase)
            else:
                writeParameter(iList, digit(iList[pointer], 5), pullValue(iList, pointer+3), 0, relativeBase)
            pointer += 4

        ##  Adjust the relative base
        elif opcode == 9:
            relativeBase += readParameter(iList, digit(iList[pointer], 3), \
                                          pointer+1, relativeBase)
            pointer += 2

        ##  Break if bad opcode
        else:
            raise Exception('Bad code call')



##  The droid and it's experience
# What each square fetures
class Square:
    def __init__(self):
        self.explore = 0
        self.distance = -2
        self.isStart = False
        self.isOxygen = False


# Helper functions
def setDistance(diagram, droidX, droidY):
    north = diagram[droidY-1][droidX].distance
    south = diagram[droidY+1][droidX].distance
    west  = diagram[droidY][droidX-1].distance
    east  = diagram[droidY][droidX+1].distance

    newDistance = None
    
    if north != -2:
        newDistance = north + 1
    if south != -2:
        if newDistance == None or south < newDistance:
            newDistance = south + 1
    if west != -2:
        if newDistance == None or west < newDistance:
            newDistance = west + 1
    if east != -2:
        if newDistance == None or east < newDistance:
            newDistance = east + 1

    diagram[droidY][droidX].distance = newDistance
            
    if north > newDistance+1:
        setDistance(diagram, droidX, droidY-1)
    if south > newDistance+1:
        setDistance(diagram, droidX, droidY+1)
    if west > newDistance+1:
        setDistance(diagram, droidX-1, droidY)
    if east > newDistance+1:
        setDistance(diagram, droidX+1, droidY)
    

def unknownNeighbors(diagram, droidX, droidY):
    sum = 0
    if diagram[droidY+1][droidX].explore == 0:
        sum += 1
    if diagram[droidY-1][droidX].explore == 0:
        sum += 1
    if diagram[droidY][droidX+1].explore == 0:
        sum += 1
    if diagram[droidY][droidX-1].explore == 0:
        sum += 1
    return sum

def discoverySize(diagram, droidX, droidY):
    sum = 0
    if diagram[droidY+1][droidX].explore > 0:
        sum += 1
    if diagram[droidY-1][droidX].explore > 0:
        sum += 1
    if diagram[droidY][droidX+1].explore > 0:
        sum += 1
    if diagram[droidY][droidX-1].explore > 0:
        sum += 1
    return sum
        
        

def locUpdate(direction, cardinal):
    if cardinal == 'X':
        if direction == 3:
            return -1
        elif direction == 4:
            return 1
    elif cardinal == 'Y':
        if direction == 1:
            return -1
        elif direction == 2:
            return 1
    return 0

# The beating heart: what direction do we go?
def pickDirection(diagram, droidX, droidY):
    north = diagram[droidY-1][droidX].explore
    south = diagram[droidY+1][droidX].explore
    west  = diagram[droidY][droidX-1].explore
    east  = diagram[droidY][droidX+1].explore

    choice = [north, south, west, east]
    biggest = max(choice)
    choice = [biggest+1 if x<0 else x for x in choice]
    loc = choice.index(min(choice))
    return loc + 1

def printBoard(diagram):
    aDistance = -1
    for line in diagram:
        result = ''
        for aSquare in line:
            if aSquare.isStart:
                value = 'S'
            elif aSquare.isOxygen:
                value = 'O'
                aDistance = aSquare.distance
            elif aSquare.explore == -1:
                value = "#"
            elif aSquare.explore > 0:
                value = " " #str(aSquare.distance)
            elif aSquare.explore == 0:
                value = "."
            result += value
        print(result)
    print(aDistance)



# Droid process
def droid(iList):
    diagram = []
    for i in range(60):
        diagram.append([Square() for j in range(60)])

    #Location of the droid
    droidX = 30
    droidY = 30
    #How many squares are neighbors but unknown
    unknown = 4
    statusCode = 0

    pointer = 0
    relativeBase = 0

    diagram[droidY][droidX].isStart = True
    diagram[droidY][droidX].distance = 0
    diagram[droidY][droidX].explore = 1

    while unknown > 0:
        direction = pickDirection(diagram, droidX, droidY)

        goY = locUpdate(direction, 'Y')
        goX = locUpdate(direction, 'X')
        
        result = interpreter(iList, direction, pointer, relativeBase)
        if result == None:
            raise Exception("Unreachable region explored")
        iList = result[0]
        # direction = result [1]
        pointer = result[2]
        relativeBase = result[3]
        statusCode = result[4]
        
        if statusCode == 0:
            diagram[droidY + goY][droidX + goX].explore = -1
            unknown -= discoverySize(diagram, droidX + goX, droidY + goY)

        else:
            droidY += goY
            droidX += goX
            diagram[droidY][droidX].explore += 1
            setDistance(diagram, droidX, droidY)
            if diagram[droidY][droidX].explore == 1:
                unknown += unknownNeighbors(diagram, droidX, droidY)-1

        if statusCode == 2:
            diagram[droidY][droidX].isOxygen = True

    printBoard(diagram)
    
    
##  Main
def main():
    iList = instructFileRead("input.txt")
    droid(iList)
    print("complete")

main()
