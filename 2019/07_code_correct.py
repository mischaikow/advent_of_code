##  Complete solution for Day 7
import math

##  Helper functions:
# Helper function to pull a specific digit
def digit(number, n):
    return number // 10**(n-1) % 10

# Helper function that recursively creates permutations
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


# Helper function that performs reads
def readParameter(aList, mode, address):
    if mode == 1:
        return aList[address]
    elif mode == 0:
        return aList[aList[address]]
    else:
        raise Exception('Incorrect mode selected')



##  The Interpreter
def interpreter(aList, isPhase, phaseSetting, signal, pointer):
    while pointer <= len(aList):
        ##  Halt command
        if aList[pointer] == 99:
            return None

        opcode = 10*digit(aList[pointer], 2) + digit(aList[pointer], 1)

        ##  Addition
        if opcode == 1:
            a = readParameter(aList, digit(aList[pointer], 3), pointer+1)
            b = readParameter(aList, digit(aList[pointer], 4), pointer+2)
            aList[aList[pointer+3]] = a + b
            pointer += 4

        ##  Multiplication
        elif opcode == 2:
            a = readParameter(aList, digit(aList[pointer], 3), pointer+1)
            b = readParameter(aList, digit(aList[pointer], 4), pointer+2)
            aList[aList[pointer+3]] = a * b
            pointer += 4
            
        ##  Input
        elif opcode == 3:
            if isPhase:
                aList[aList[pointer+1]] = phaseSetting
                isPhase = False
            else:
                aList[aList[pointer+1]] = signal
            pointer += 2

        ##  Output
        elif opcode == 4:
            return readParameter(aList, digit(aList[pointer], 3), pointer+1), \
                pointer+2

        ##  Not Equal to Zero
        elif opcode == 5:
            if readParameter(aList, digit(aList[pointer], 3), pointer+1) != 0:
                pointer = readParameter(aList, \
                                        digit(aList[pointer], 4), \
                                        pointer+2)
            else:
                pointer += 3

        ##  Equal to Zero
        elif opcode == 6:
            if readParameter(aList, digit(aList[pointer], 3), pointer+1) == 0:
                pointer = readParameter(aList, \
                                        digit(aList[pointer], 4), \
                                        pointer+2)
            else:
                pointer += 3

        ##  Less Than
        elif opcode == 7:
            if readParameter(aList, digit(aList[pointer], 3), pointer+1) < \
               readParameter(aList, digit(aList[pointer], 4), pointer+2):
                aList[aList[pointer+3]] = 1
            else:
                aList[aList[pointer+3]] = 0
            pointer += 4

        ##  Equal
        elif opcode == 8:
            if readParameter(aList, digit(aList[pointer], 3), pointer+1) == \
               readParameter(aList, digit(aList[pointer], 4), pointer+2):
                aList[aList[pointer+3]] = 1
            else:
                aList[aList[pointer+3]] = 0
            pointer += 4


##  The methods
# Single aplification cycle path
def amplifierCycle(phaseSetting, signal, fileName):
    command_file = open(fileName, 'r')
    commands_raw = command_file.readline().split(',')
    commands_raw[-1] = commands_raw[-1].replace('\n', '')

    aList = list(map(int, commands_raw))

    for anAmp in phaseSetting:
        signal, _ = interpreter(aList, True, anAmp, signal, 0)

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

    isPhase = True
    signal = [signalInput, 0, 0, 0, 0]
    pointer = [0, 0, 0, 0, 0]

    while True:
        for i in range(5):
            temp = interpreter(aList[i], \
                               isPhase, \
                               phaseSetting[i], \
                               signal[i], \
                               pointer[i])

            if temp == None:
                return signal[0]
            elif i == 4:
                signal[0], pointer[i] = temp
            else:
                signal[i+1], pointer[i] = temp
        isPhase = False


# Search for maximum output from multicycle amp path
def findMaxRepeat(signal, fileName, permuteList):
    aList = permute(permuteList)
    maximum = 0
    for value in aList:
        temp = repeatCycle(value, signal, fileName)
        maximum = max(temp, maximum)
    return maximum

    

print "Max for one cycle is: ", findMax(0, "input.txt", [0, 1, 2, 3, 4])
print "Single issue check: ", repeatCycle([9, 8, 7, 6, 5], 0, "input_test.txt")
print "Max for multicycle is: ", \
    findMaxRepeat(0, "input.txt", [5, 6, 7, 8, 9])
