## A little mini program
## all code comes in quads:  0, 1, 2, 3

def code_read(aList):
    for i in range(len(aList)/4):
        if aList[i*4] == 99:
            return aList
        if aList[i*4] != 1 and aList[i*4] != 2:
            return "Program Error"
        else:
            a = aList[aList[(i*4) + 1]]
            b = aList[aList[(i*4) + 2]]
            if aList[i*4] == 1:
                c = a + b
            if aList[i*4] == 2:
                c = a * b
            aList[aList[(i*4) + 3]] = c
    return aList


## Read the file and transform it into a list
command_file = open("input.txt", "r")
commands = command_file.readline().split(",")
commands[-1] = commands[-1].replace("\n",'')
commands_int = list(map(int, commands))

commands_int[1] = 98
commands_int[2] = 2

print commands_int
print code_read(commands_int)


