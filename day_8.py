##  Day 8 of the challenge
##  This seems straightforward? But I'm sure there is a smoother solution

##  Helper functions
# Image importer
def imagePull(fileName):
    image_file = open(fileName, 'r')
    image_file_line = image_file.readline()
    image_file_line = image_file_line.replace('\n', '')
    return image_file_line
    
# One pass checksum
def countLevel(aString):
    count = [0, 0, 0]
    for i in aString:
        if i == '0':
            count[0] += 1
        elif i == '1':
            count[1] += 1
        elif i == '2':
            count[2] += 1

    return count

# Filter comparison
def filterCompare(topString, bottomString):
    outputList = []
    for i in range(len(topString)):
        if topString[i] == '2':
            outputList.append(bottomString[i])
        else:
            outputList.append(topString[i])
    return ''.join(outputList)

# Print Images
def printImage(aString, xSize, ySize):
    for i in range(ySize):
        print aString[i*xSize:(i+1)*xSize]


##  Checksum
def checkSumImage(aString, xSize, ySize):
    zeroCountMax = xSize * ySize + 1
    outputMax = 0
    imageSize = xSize * ySize
    layerCount = len(aString) / imageSize

    for i in range(layerCount):
        values = countLevel(aString[(i * imageSize):((i+1) * imageSize)])
        if values[0] < zeroCountMax:
            zeroCountMax = values[0]
            outputMax = values[1] * values[2]

    return outputMax


##  Decode the Image
def imageDecode(aString, xSize, ySize):
    imageSize = xSize * ySize
    layerCount = len(aString) / imageSize

    output = aString[:imageSize]

    for i in range(1, layerCount):
        output = filterCompare(output, \
                               aString[(i*imageSize):((i+1) * imageSize)])

    output = output.replace('1', 'X')
    output = output.replace('0', ' ')
    printImage(output, xSize, ySize)
    return None
    


imageData = imagePull('input.txt')
#print checkSumImage(imageData, 25, 6)

imageDecode(imageData, 25, 6)
