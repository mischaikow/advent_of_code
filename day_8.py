##  Day 8 of the challenge
##  This seems straightforward? But I'm sure there is a smoother solution

# Each pass
def countLevel(aList):
    zeroCount = 0
    oneCount = 0
    twoCount = 0

    for i in aList:
        if i == '0':
            zeroCount += 1
        elif i == '1':
            oneCount += 1
        elif i == '2':
            twoCount += 1

    return (zeroCount, oneCount * twoCount)

# The whole dataset
def checkSumImage(aList, xSize, ySize):
    zeroCountMax = xSize * ySize + 1
    outputMax = 0
    numberOfLayers = len(aList) / (xSize * ySize)
    for i in range(numberOfLayers):
        values = countLevel(aList[(i * xSize * ySize):((i+1) * xSize * ySize)])
        if values[0] < zeroCountMax:
            zeroCountMax = values[0]
            outputMax = values[1]

    return outputMax

image_file = open("input.txt", 'r')
image_file_line = image_file.readline()
image_file_line = image_file_line.replace('\n', '')

print checkSumImage(image_file_line, 25, 6)

