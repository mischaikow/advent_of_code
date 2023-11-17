"""Day 14 of the 2020 Advent of Code

Catching up
"""

def readFile(fileName):
    with open(fileName) as f:
        raw = f.read().strip().split('\n')
    instruction_set = [i.strip().split(' = ') for i in raw]
    return instruction_set


def makeValueMask(aString):
    zeros = ones = 0
    for val in aString:
        zeros *= 2
        ones *= 2
        if val == '1':
            ones += 1
            zeros += 1
        elif val == 'X':
            zeros += 1
    return zeros, ones


def finalNumbers(instructions):
    numbers = {}
    for step in instructions:
        if step[0] == 'mask':
            zeros, ones = makeValueMask(step[1])
        else:
            memory_spot = int(step[0][4:-1])
            new_value = int(step[1])
            new_value = new_value | ones
            new_value = new_value & zeros
            numbers[memory_spot] = new_value
        
    result = 0
    for memory in numbers:
        result += numbers[memory]
    return result


def makeMaskSet(aString):
    zeros = [0]
    ones = [0]
    for val in aString:
        zeros = [i*2+1 for i in zeros]
        ones = [i*2 for i in ones]
        if val == '1':
            ones = [i+1 for i in ones]
        elif val == 'X':
            ones = ones + [i+1 for i in ones]
            zeros = [i-1 for i in zeros] + zeros
    return zeros, ones


def versionTwo(instructions):
    numbers = {}
    for step in instructions:
        if step[0] == 'mask':
            zeros, ones = makeMaskSet(step[1])
        else:
            temp = int(step[0][4:-1])
            memory_spot = []
            for i in range(len(zeros)):
                memory_spot.append(temp | ones[i])
                memory_spot[i] = memory_spot[i] & zeros[i]
                numbers[memory_spot[i]] = int(step[1])

    result = 0
    for memory in numbers:
        result += numbers[memory]
    return result


def main():
    instructions = readFile('input_14_1.txt')
    print('Part 1:', finalNumbers(instructions))
    print('Part 2:', versionTwo(instructions))
    return True


main()
