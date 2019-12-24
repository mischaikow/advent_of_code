## Day 5 of the challenge
## A more sophisticated interpreter

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
def interpreter(aList):
    i = 0
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
            aList[aList[i+1]] = input("System ID: ")
            i += 2

        elif opcode == 4:
            print "Diagnostic code:", \
                readParameter(aList, digit(aList[i], 3), i+1)
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

            
def search_frame(aList):
    for noun in range(99):
        for verb in range(99):
            newList = list(map(int, aList))
            newList[1] = noun
            newList[2] = verb
            if code_read(newList)[0] == 19690720:
                print 100 * noun + verb



## Read the file and transform it into a list
command_file = open("input.txt", "r")
#command_file = open("input_test.txt", "r")
commands = command_file.readline().split(",")
commands[-1] = commands[-1].replace("\n", '')

interpreter(list(map(int, commands)))
