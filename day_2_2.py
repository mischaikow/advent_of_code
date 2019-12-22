## My new interpreter
## A little more sophisticated

def code_read(aList):
    i = 0
    while i <= len(aList):
        if aList[i] == 99:
            return aList
        if aList[i] != 1 and aList[i] != 2:
            raise Exception('Bad input')
        else:
            a = aList[aList[i+1]]
            b = aList[aList[i+2]]
            if aList[i] == 1:
                c = a + b
            else:
                c = a * b
            aList[aList[i+3]] = c
        i += 4
    return aList

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
commands = command_file.readline().split(",")
commands[-1] = commands[-1].replace("\n", '')

search_frame(commands)
