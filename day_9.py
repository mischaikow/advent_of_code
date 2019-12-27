##  Day 9, we revisit the interpreter
import math

##  Helper functions:
# Helper function to pull a specific digit from a number
def digit(number, n):
    return number // 10**(n-1) % 10

# Helper function that recursitvely creates permutations
def permute(aList):
    if len(aList) == 2:
        return [[aList[0], aList[1]], [aList[1], aList[0]]]
    else:
        result = []
        for i in range(len(aList)):
            temp = permute(aList[:i] + aList[i+1:])
            for j in range(math.factorial(len(aList)-1)):
                temp[j].append(aList[i])
            result += temp
        return result


# Helper function that does simple list read
def pullValue(iList, address):
    if address >= len(iList):
        return 0
    else:
        return iList[address]

# Helper function that performs reads
def readParameter(iList, mode, address, relativeBase = None):
    if mode == 0:
        return pullValue(iList, pullValue(iList, address))
    elif mode == 1:
        return pullValue(iList, address)
    elif mode == 2:
        return pullValue(iList, relativeBase + pullValue(iList, address))
    else:
        raise Exception('Incorrect mode selectied')

# Helper function that performs writes
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


##  The Interpreter
def interpreter(iList, signal = 0, phaseSetting = None, pointer = 0):
    relativeBase = 0

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
#            return readParameter(iList, digit(iList[pointer], 3), pointer+1, \
#                                relativeBase), pointer+2
            print readParameter(iList, digit(iList[pointer], 3), pointer+1, \
                                relativeBase)
            pointer += 2

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


##  The methods
# Single aplification cycle path
def amplifierCycle(phaseSetting, signal, fileName):
    command_file = open(fileName, 'r')
    commands_raw = command_file.readline().split(',')
    commands_raw[-1] = commands_raw[-1].replace('\n', '')

    aList = list(map(int, commands_raw))

    for anAmp in phaseSetting:
        signal, _ = interpreter(aList, signal, anAmp)

    return signal


# Use the single cycle path to find max possible signal
def findMax(signal, fileName, permuteList):
    aList = permute(permuteList)
    maximum = 0
    for value in aList:
        temp = amplifierCycle(value, signal, fileName)
        maximum = max(temp, maximum)
    return maximum


# Multiple cycle amplification path
def repeatCycle(phaseSetting, signalInput, fileName):
    command_file = open(fileName, 'r')
    commands_raw = command_file.readline().split(',')
    commands_raw[-1] = commands_raw[-1].replace('\n', '')

    aList = []
    for _ in range(5):
        aList.append(list(map(int, commands_raw)))

    signal = [signalInput, 0, 0, 0, 0]
    pointer = [0, 0, 0, 0, 0]

    while True:
        for i in range(5):
            temp = interpreter(aList[i], \
                               signal[i], \
                               phaseSetting[i], \
                               pointer[i])

            phaseSetting[i] = None
            if temp == None:
                return signal[0]
            elif i == 4:
                signal[0], pointer[i] = temp
            else:
                signal[i+1], pointer[i] = temp


# Search for maximum output from multicycle amp path
def findMaxRepeat(signal, fileName, permuteList):
    aList = permute(permuteList)
    maximum = 0
    for value in aList:
        temp = repeatCycle(value, signal, fileName)
        maximum = max(temp, maximum)
    return maximum


# Single interpreter run
def intRun(fileName, instruction):
    command_file = open(fileName, 'r')
    commands_raw = command_file.readline().split(',')
    commands_raw[-1] = commands_raw[-1].replace('\n', '')

    return interpreter(list(map(int, commands_raw)), instruction, None)


# print "Max for one cycle is: ", findMax(0, "input.txt", [0, 1, 2, 3, 4])
# print "Single issue check: ", repeatCycle([9, 8, 7, 6, 5], 0, "input_test.txt")
# print "Max for multicycle is: ", findMaxRepeat(0, "input_test.txt", [5, 6, 7, 8, 9])

intRun('input.txt', 2)
