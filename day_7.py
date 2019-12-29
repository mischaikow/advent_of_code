import math

##  Helper functions:
# Helper function to pull a specific digit
def digit(number, n):
    return number // 10**(n-1) % 10

# Helper function that performs reads
def readParameter(aList, mode, address):
    if mode == 1:
        return aList[address]
    elif mode == 0:
        return aList[aList[address]]

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

    
## The interpreter!
# enhanced to handle EXACTLY two inputs
def interpreter(aList, phaseSetting, signalCount, signal, i):
    
    while i <= len(aList):

        if aList[i] == 99:
            # Halt command
            print "Halt"
            return None

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
            return readParameter(aList, digit(aList[i], 3), i+1), i+2

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
#    command_file = open("input.txt", "r")
    command_file = open("input_test.txt", "r")
    commands = command_file.readline().split(",")
    commands[-1] = commands[-1].replace("\n", '')

    aList = list(map(int, commands))

    for i in cycle:
        signal = interpreter(aList, i, signal)

    return signal


def findMax(signal):
    aList = permute([9, 8, 7, 6, 5])
    maximum = 0
    for value in aList:
        value = [9, 7, 8, 5, 6]
        temp = amplifierCycle(value, signal)
        if temp > maximum:
            maximum = temp
            result = value
        print maximum
        break
    return result


def repeatCycle(cycle, signalInput):
#    command_file = open("input.txt", "r")
    command_file = open("input_test.txt", "r")
    commands = command_file.readline().split(",")
    commands[-1] = commands[-1].replace("\n", '')

    aList = []
    for _ in range(5):
        aList.append(list(map(int, commands)))

    phaseSignal = 0
    signal = [signalInput, 0, 0, 0, 0]
    arrow = [0, 0, 0, 0, 0]

    while True:
        for i in range(5):
            output = "Step: " + str(i+1) + " and output " + str(signal[0])
            print output
            if i == 4:
                print aList[i]
                temp = interpreter(aList[i], cycle[i], phaseSignal, signal[i], arrow[i])
                if temp == None:
                    return signal[0]
                else:
                    signal[0], arrow[i] = temp
            else:
                temp = interpreter(aList[i], cycle[i], phaseSignal, signal[i], arrow[i])
                if temp == None:
                    return signal[0]
                else:
                    signal[i+1], arrow[i] = temp
        phaseSignal = 1
        

#print findMax(0)
print repeatCycle([9, 7, 8, 5, 6], 0)
