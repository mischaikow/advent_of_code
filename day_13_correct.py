##  Day 13
##  The interpreter gets an interface
##  
from asciimatics.screen import ManagedScreen
from time import sleep

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

# Image lookup
def iconSearch(number):
    # 0 is an empty tile. No game object appears in this tile.
    if number == 0:
        return ' '
    # 1 is a wall tile. Walls are indestructible barriers.
    elif number == 1:
        return 'X'
    # 2 is a block tile. Blocks can be broken by the ball.
    elif number == 2:
        return 'O'
    # 3 is a horizontal paddle tile. The paddle is indestructible.
    elif number == 3:
        return '-'
    # 4 is a ball tile. The ball moves diagonally and bounces off objects.
    elif number == 4:
        return '*'

# Print a single screenshot
def printScreen(aList):
    for line in aList:
        print(line)

    


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


##  The game
def theGame(fileName):
    vArray = []
    for i in range(25):
        vArray.append([' '] * 45)
    output = [0] * 20

    iList = instructFileRead(fileName)
    signal = 0
    pointer = 0
    relativeBase = 0

    barPos = 0
    ballPos = 0

    counter = 0

    with ManagedScreen() as screen:
    
        while True:
            result = interpreter(iList, signal, pointer, relativeBase)
            if result == None:
                break
            iList = result[0]
            #signal = result[1]
            pointer = result[2]
            relativeBase = result[3]
            xPos = result[4]
            
            result = interpreter(iList, signal, pointer, relativeBase)
            iList = result[0]
            #signal = result[1]
            pointer = result[2]
            relativeBase = result[3]
            yPos = result[4]

            result = interpreter(iList, signal, pointer, relativeBase)
            iList = result[0]
            #signal = result[1]
            pointer = result[2]
            relativeBase = result[3]
            imageObj = result[4]
            
            if xPos == -1 and yPos == 0:
                vArray[24][0] = str(imageObj)
                score = str(imageObj)
            else:
                vArray[yPos][xPos] = iconSearch(imageObj)

            #    if counter > 880:
            #        for i in range(len(vArray)):
            #            output = ''.join(vArray[i])
            #            screen.print_at(output, 0, i)
                    
            #    screen.refresh()

            if imageObj == 3:
                barPos = xPos
            
            if imageObj == 4:
                if xPos == barPos:
                    signal = 0
                elif xPos < barPos:
                    signal = -1
                elif xPos > barPos:
                    signal = 1
                    
                ballPos = xPos
            
            counter += 1

    print(score)

                
    #for i in range(len(screen)):
    #    screen[i] = ''.join(screen[i])
    #printScreen(screen)
    #print(counter)

##  Execution
theGame('input.txt')



#def demo(screen):
#    while True:
#        screen.print_at('Hello world!',
#                        randint(0, screen.width), randint(0, screen.height),
#                        colour=randint(0, screen.colours - 1),
#                        bg=randint(0, screen.colours - 1))
#        ev = screen.get_key()
#        if ev in (ord('Q'), ord('q')):
#            return
#        screen.refresh()

#Screen.wrapper(demo)
