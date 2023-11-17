from collections import deque

def helper(raw_data):
    ans = []
    for i, row in enumerate(raw_data):
        for j, char in enumerate(row):
            smallest = 10
            if i > 0: smallest = min(smallest, raw_data[i-1][j])
            if j > 0: smallest = min(smallest, raw_data[i][j-1])
            if i < len(raw_data)-1: smallest = min(smallest, raw_data[i+1][j])
            if j < len(row)-1: smallest = min(smallest, raw_data[i][j+1])
            if smallest > char:
                ans.append(((i, j)))
    return ans

def region_size(raw_data, coords):
    ans = 0
    to_visit = deque([coords])
    while to_visit:
        x = to_visit.popleft()
        if raw_data[x[0]][x[1]] < 9:
            ans += 1
            raw_data[x[0]][x[1]] = 9
            if x[0] > 0: to_visit.append(((x[0]-1,x[1])))
            if x[1] > 0: to_visit.append(((x[0],x[1]-1)))
            if x[0] < len(raw_data)-1: to_visit.append(((x[0]+1,x[1])))
            if x[1] < len(raw_data[0])-1: to_visit.append(((x[0],x[1]+1)))
    return ans



def part_1(raw_data):
    ans = 0
    for i, row in enumerate(raw_data):
        for j, char in enumerate(row):
            smallest = 10
            if i > 0: smallest = min(smallest, raw_data[i-1][j])
            if j > 0: smallest = min(smallest, raw_data[i][j-1])
            if i < len(raw_data)-1: smallest = min(smallest, raw_data[i+1][j])
            if j < len(row)-1: smallest = min(smallest, raw_data[i][j+1])
            if smallest > char:
                ans += 1 + char
    return ans

def part_2(raw_data):
    three_biggest = [-1, -1, -1]
    nadirs = helper(raw_data)
    for coords in nadirs:
        temp = region_size(raw_data, coords)
        for i in range(3):
            if temp > three_biggest[i]:
                three_biggest[i], temp = temp, three_biggest[i]
    return three_biggest[0] * three_biggest[1] * three_biggest[2]

 
def file_reader(file_name):
    input_file = open(file_name, 'r')
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace('\n', '')
        inputs_raw[i] = [int(char) for char in inputs_raw[i]]
    return inputs_raw

print(part_1(file_reader('input_09.txt')))
print(part_2(file_reader('input_09.txt')))
