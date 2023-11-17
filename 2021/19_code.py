from collections import deque
from collections import defaultdict
from copy import copy

class Scanner:
    def __init__(self, beacons):
        self.beacons = beacons
        self.location = [0, 0, 0]
        self.distances = []
        for i in range(len(self.beacons)):
            for j in range(i+1, len(self.beacons), 1):
                total = 0
                for k in range(3):
                    total += (self.beacons[i][k] - self.beacons[j][k]) ** 2
                self.distances.append([i, j, total])

    def compare_distances(self, neighbor_scanner):
        beacons_self = defaultdict(list)
        beacons_neighbor = defaultdict(list)
        match_count = 0
        for i in self.distances:
            for j in neighbor_scanner.distances:
                if i[2] == j[2]:
                    beacons_self[i[0]].append(i[2])
                    beacons_self[i[1]].append(i[2])
                    beacons_neighbor[j[0]].append(i[2])
                    beacons_neighbor[j[1]].append(i[2])
                    match_count += 1
        if match_count >= 66:
            beacon_list_self = []
            beacon_list_neighbor = []
            for b_n in beacons_neighbor:
                beacons_neighbor[b_n].sort() 
            for b_s in beacons_self:
                beacons_self[b_s].sort()
                for b_n in beacons_neighbor:
                    if beacons_self[b_s] == beacons_neighbor[b_n]:
                        beacon_list_self.append(b_s)
                        beacon_list_neighbor.append(b_n)
                        break
            
            move_self = [b - a for a, b in zip(self.beacons[beacon_list_self[0]], self.beacons[beacon_list_self[1]])]
            move_neighbor = [b - a for a, b in zip(neighbor_scanner.beacons[beacon_list_neighbor[0]], neighbor_scanner.beacons[beacon_list_neighbor[1]])]

            sign = { 0:1, 1:1, 2:1 }
            swap = { 0:0, 1:1, 2:2 }
            for i, val in enumerate(move_self):
                for j, n_val in enumerate(move_neighbor):
                    if val == n_val:
                        swap[j] = i
                    elif val == -n_val:
                        swap[j] = i
                        sign[j] = -1

            transform = [-x for x in self.beacons[beacon_list_self[0]]]
            transform[0], transform[1], transform[2] = transform[swap[0]], transform[swap[1]], transform[swap[2]]
            for i in range(3):
                transform[i] *= sign[i]
            for i in range(3):
                self.location[i] = neighbor_scanner.beacons[beacon_list_neighbor[0]][i] + transform[i]
            
            for i in range(len(self.beacons)):
                self.beacons[i][0], self.beacons[i][1], self.beacons[i][2] = self.beacons[i][swap[0]], self.beacons[i][swap[1]], self.beacons[i][swap[2]]
                for j in range(3):
                    self.beacons[i][j] *= sign[j]
                for j in range(3):
                    self.beacons[i][j] += self.location[j]

            return True
        else:
            return False


def solution(scanner_list_raw):

    scanner_list = []
    for s in scanner_list_raw:
        scanner_list.append(Scanner(s))

    visited_list = [True] * len(scanner_list)
    visited_list[0] = False
    to_visit = deque()
    to_visit.append(0)

    while any(visited_list):
        current_scanner = to_visit.popleft()
        for i in range(len(scanner_list)):
            if visited_list[i]:
                if scanner_list[i].compare_distances(scanner_list[current_scanner]):
                    visited_list[i] = False
                    to_visit.append(i)

    final_beacons = set()
    for s in scanner_list:
        final_beacons |= set(tuple(x) for x in s.beacons)

    print('Part 1:', len(final_beacons))

    biggest_distance = 0
    for i in range(len(scanner_list)):
        for j in range(i+1, len(scanner_list), 1):
            biggest_distance = max(biggest_distance, man_distance(scanner_list[i].location, scanner_list[j].location))
    
    print('Part 2:', biggest_distance)


def man_distance(a, b):
    ans = 0
    for i, j in zip(a, b):
        ans += abs(i-j)
    return ans

 
def file_reader(file_name):
    input_file = open(file_name, 'r')
    inputs_raw = input_file.readlines()
    result = []
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace('\n', '')
        if inputs_raw[i].find('scanner') > 0:
            result.append([])
        elif len(inputs_raw[i]) > 1:
            tmp = inputs_raw[i].split(',')
            result[-1].append([int(x) for x in tmp])
    return result

solution(file_reader('input_19.txt'))