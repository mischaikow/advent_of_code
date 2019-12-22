## Grid cross discovery
## Clunky answer, I'm curious how other people have done this

# Read file
def file_import(fileName):
    return 1

# Build path
def path_build(instructionList):
    positionList = [(0,0)]
    for step in instructionList:
        if step[0] == 'R':
            move = (1, 0)
        if step[0] == 'L':
            move = (-1, 0)
        if step[0] == 'U':
            move = (0, 1)
        if step[0] == 'D':
            move = (0, -1)

        distance = int(step[1:])
        for i in range(distance):
            positionList.append((positionList[-1][0] + move[0],
                                 positionList[-1][1] + move[1]))

    return positionList

                
# How far is a node?
def node_distance(aNode):
    return abs(aNode[0]) + abs(aNode[1])


# Which is the closest node?
def closest_node(nodeList):
    nearestNode = (0, 0)
    nodeDistance = 0
    for i in nodeList:
        if node_distance(i) < nodeDistance or nodeDistance == 0:
            nodeDistance = node_distance(i)
            nearestNode = i

    return nearestNode


# Create a dictionary of wire length to reach nodes
def node_distances(nodeSet, wirePath):
    result = {}
    count = 0
    for node in wirePath:
        if node in nodeSet:
            result[node] = count
        count += 1
    return result


# Read file
command_file = open("input.txt", "r")
listOne = command_file.readline().split(",")
listOne[-1] = listOne[-1].replace("\n", '')
listTwo = command_file.readline().split(",")
listTwo[-1] = listTwo[-1].replace("\n", '')


# Build paths
pathOne = path_build(listOne)
pathOneVisit = set(pathOne[1:])
pathTwo = path_build(listTwo)
pathTwoVisit = set(pathTwo[1:])

# Compare paths
matches = pathOneVisit & pathTwoVisit

print closest_node(matches)
print node_distance(closest_node(matches))

# Build each dictionary of distance of wire to the node
pathOneDict = node_distances(matches, pathOne)
pathTwoDict = node_distances(matches, pathTwo)

# Compare the two dictionaries of distances ot get the shortest sum path
totalDistance = 0
for node in matches:
    newDistance = pathOneDict[node] + pathTwoDict[node]
    if newDistance < totalDistance or totalDistance == 0:
        totalDistance = newDistance

print totalDistance

