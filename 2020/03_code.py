"""Day 3 of the 2020 Advent of Code event


"""

def fileReader(fileName):
    input_file = open(fileName, 'r')
    inputs_raw = input_file.readlines()
    inputs_raw = [aString.replace('\n', '') for aString in inputs_raw]
    return inputs_raw


def countTrees(strArr, hMove, vMove):
    count = 0
    width = len(strArr[0])
    vTrack, hTrack = 0, 0
    while vTrack < len(strArr):
        count += strArr[vTrack][hTrack] == '#'
        hTrack = (hTrack + hMove) % width
        vTrack += vMove
    return count


def treeProduct(strArr, aList):
    treeAnswer = 1
    for i in aList:
        treeAnswer *= countTrees(strArr, i[0], i[1])
    return treeAnswer


def main(fileName):
    myMap = fileReader(fileName)
    print('Part 1:', countTrees(myMap, 3, 1))
    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    print('Part 2:', treeProduct(myMap, slopes))
    

main('input_03_1.txt')
