"""Day 9 of the Advent of Code event


"""

def readFile(fileName):
    with open(fileName) as f:
        inputs = f.readlines()
    return [int(x.strip()) for x in inputs]


def checkSum(aList, value):    
    for i in range(25):
        for j in range(i+1, 25):
            if value == aList[i] + aList[j]:
                return -1
    return value


def firstFail(numbers):
    sample = numbers[:25]
    for i in range(25, len(numbers)-1):
        result = checkSum(sample, numbers[i])
        if result > 0:
            print('Part 1:', result)
            return result
        sample = numbers[i-24:i+1]
    return -1


def failSet(numbers, key_number):
    i, j = 0, 1
    while True:
        sample = numbers[i:j]
        if sum(sample) == key_number:
            return min(sample) + max(sample)
        elif sum(sample) < key_number:
            j += 1
            if j > len(numbers):
                return False
        elif sum(sample) > key_number:
            i += 1


def main():
    XMAS_data = readFile('input_09_1.txt')
    key_number = firstFail(XMAS_data)
    print('Part 2:', failSet(XMAS_data, key_number))
    return None


main()
