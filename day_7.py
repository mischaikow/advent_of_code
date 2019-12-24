import math

# Helper functions
# Not consistent with day 2!
def digit(number, n):
    return number // 10**(n-1) % 10

# Helper function that performs reads
def readParameter(aList, mode, address):
    if mode == 1:
        return aList[address]
    elif mode == 0:
        return aList[aList[address]]

## The interpreter!
# enhanced to handle EXACTLY two inputs
def interpreter(aList, phaseSetting, signal):
    i = 0
    signalCount = 0
    while i <= len(aList):

        if aList[i] == 99:
            # End the program
            return "Program Complete"

        opcode = digit(aList[i], 2)*10 + digit(aList[i], 1)

        if opcode == 1:
            a = readParameter(aList, digit(aList[i], 3), i+1)
            b = readParameter(aList, digit(aList[i], 4), i+2)
            aList[aList[i+3]] = a + b
            i += 4

        elif opcode == 2:
            a = readParameter(aList, digit(aList[i], 3), i+1)
            b = readParameter(aList, digit(aList[i], 4), i+2)
            aList[aList[i+3]] = a * b
            i += 4
            
        elif opcode == 3:
            if signalCount == 0:
                aList[aList[i+1]] = phaseSetting
                signalCount += 1
            elif signalCount == 1:
                aList[aList[i+1]] = signal
                signalCount += 1
            else:
                print "error"
            i += 2

        elif opcode == 4:
            return readParameter(aList, digit(aList[i], 3), i+1)
            i += 2

        elif opcode == 5:
            if readParameter(aList, digit(aList[i], 3), i+1) != 0:
                i = readParameter(aList, digit(aList[i], 4), i+2)
            else:
                i += 3

        elif opcode == 6:
            if readParameter(aList, digit(aList[i], 3), i+1) == 0:
                i = readParameter(aList, digit(aList[i], 4), i+2)
            else:
                i += 3

        elif opcode == 7:
            if readParameter(aList, digit(aList[i], 3), i+1) < \
               readParameter(aList, digit(aList[i], 4), i+2):
                aList[aList[i+3]] = 1
            else:
                aList[aList[i+3]] = 0
            i += 4

        elif opcode == 8:
            if readParameter(aList, digit(aList[i], 3), i+1) == \
               readParameter(aList, digit(aList[i], 4), i+2):
                aList[aList[i+3]] = 1
            else:
                aList[aList[i+3]] = 0
            i += 4


def amplifierCycle(cycle, signal):
    command_file = open("input.txt", "r")
#    command_file = open("input_test.txt", "r")
    commands = command_file.readline().split(",")
    commands[-1] = commands[-1].replace("\n", '')

    aList = list(map(int, commands))

    for i in cycle:
        signal = interpreter(aList, i, signal)
    return signal



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

def findMax(signal):
    aList = permute([0, 1, 2, 3, 4])
    maximum = 0
    for value in aList:
        temp = amplifierCycle(value, signal)
        maximum = max(temp, maximum)
    return maximum


print findMax(0)
