##  Day 11
##  Back to the interpreter


##  Helper functions:
# Pull a specific digit from a number
def digit(number, n):
    return number // 10**(n-1) % 10

# Read a value, even if it's from outside a list's bounds,
# only for the Interpreter
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



##  The Interpreter
def interpreter(iList, signal = 0, phaseSetting = None, pointer = 0, relativeBase = 0):

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
            writeParameter(iList, digit(iList[pointer], 5), pullValue(iList, pointer+3), a + b, relativeBase)
            pointer += 4

        ##  Multiplication
        elif opcode == 2:
            a = readParameter(iList, digit(iList[pointer], 3), pointer+1, \
                              relativeBase)
            b = readParameter(iList, digit(iList[pointer], 4), pointer+2, \
                              relativeBase)
            writeParameter(iList, digit(iList[pointer], 5), pullValue(iList, pointer+3), a * b, relativeBase)
            pointer += 4

        ##  Input 
        elif opcode == 3:
            if phaseSetting != None:
                writeParameter(iList, digit(iList[pointer], 3), pullValue(iList, pointer+1), phaseSetting, relativeBase)
                phaseSetting = None
            else:
                writeParameter(iList, digit(iList[pointer], 3), pullValue(iList, pointer+1), signal, relativeBase)
            pointer += 2

        ##  Output
        elif opcode == 4:
            return readParameter(iList, digit(iList[pointer], 3), \
                                 pointer+1, relativeBase), iList, pointer+2, \
                                 relativeBase
#            print readParameter(iList, digit(iList[pointer], 3), \
#                                pointer+1, relativeBase)
#            pointer += 2

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
                writeParameter(iList, digit(iList[pointer], 5), pullValue(iList, pointer+3), 1, relativeBase)
            else:
                writeParameter(iList, digit(iList[pointer], 5), pullValue(iList, pointer+3), 0, relativeBase)
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

##  The robot
# There's code, which feeds into the interpreter iList
# and a map of the ship's side
def operateRobot(iList):
    shipSide = []
    shipSideCoord = [30, 80]
    shipDirections = [[-1,0], [0,-1], [1,0], [0,1]]
    shipPoint = 0
    pointer = 0
    relativeBase = 0
    visitedPoints = set()
    for i in range(100):
        shipSide.append([0] * 150)
    shipSide[shipSideCoord[0]][shipSideCoord[1]] = 1

    
    while True:
        simpleCoord = 1000*shipSideCoord[0] + shipSideCoord[1]
        if not simpleCoord in visitedPoints:
            visitedPoints.add(simpleCoord)
        print(shipSide[shipSideCoord[0]][shipSideCoord[1]])
        result = interpreter(iList, \
                             shipSide[shipSideCoord[0]][shipSideCoord[1]], \
                             None, pointer, relativeBase)
        if result == None:
            break

        paintColor = result[0]
        iList = result[1]
        pointer = result[2]
        relativeBase = result[3]
        
        result = interpreter(iList, \
                             shipSide[shipSideCoord[0]][shipSideCoord[1]], \
                             None, pointer, relativeBase)

        instruction = result[0]
        iList = result[1]
        pointer = result[2]
        relativeBase = result[3]

        # Paint the board and move the robot
        shipSide[shipSideCoord[0]][shipSideCoord[1]] = paintColor
        if instruction == 0:
            shipPoint = (shipPoint + 1) % 4
        elif instruction == 1:
            shipPoint = (shipPoint + 3) % 4
        shipSideCoord[0] += shipDirections[shipPoint][0]
        shipSideCoord[1] += shipDirections[shipPoint][1]
        if shipSideCoord[0] <= 0 or shipSideCoord[1] <= 0:
            raise Exception('you ran off the side of the ship!')
        
    output = []
    for each in shipSide:
        for i in range(len(each)):
            if each[i] == 0:
                each[i] = '.'
            else:
                each[i] = '#'
        result = ''.join(each)
        print(result)

    print(len(visitedPoints))



myInstructions = instructFileRead('input.txt')
operateRobot(myInstructions)
