##  Build the obital counter
##  Keep it going

def create_map(aList):
    galaxyMap = {}
    for orbit in aList:
        inside, outside = str.split(orbit, ')')
        if not inside in galaxyMap:
            galaxyMap[inside] = None
        galaxyMap[outside] = inside

    return galaxyMap


def count_depth(galaxy_map, start):
    if start == None:
        return -1
    else:
        return count_depth(galaxy_map, galaxy_map[start]) + 1

def list_depth(galaxy_map, start):
    result = []
    while start != None:
        result.append(start)
        start = galaxy_map[start]
    return result
    
def orbit_count_checksum(galaxy_map):
    count = 0
    for space_thing in galaxy_map:
        count += count_depth(galaxy_map, space_thing)
    return count


def minimum_orbit_transfers(galaxy_map, nodeA, nodeB):
    listA = list_depth(galaxy_map, nodeA)
    listB = list_depth(galaxy_map, nodeB)
    for i in range(len(listA)):
        for j in range(len(listB)):
            if listA[i] == listB[j]:
                return len(listA[1:i] + listB[1:(j+1)])
                
    
## Read file
galaxy_map_file = open("input.txt", "r")
galaxy_map_raw = galaxy_map_file.readlines()
for i in range(len(galaxy_map_raw)):
    galaxy_map_raw[i] = galaxy_map_raw[i].replace("\n", '')
    
galaxy_map = create_map(galaxy_map_raw)

print minimum_orbit_transfers(galaxy_map, 'YOU', 'SAN')
