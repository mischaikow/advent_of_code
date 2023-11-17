from collections import deque

def part_1(data_raw):
    path_cost = [[-1] * len(data_raw[0]) for _ in range(len(data_raw))]
    path_cost[0][0] = 0

    to_visit = deque()
    to_visit.append(((0,0)))

    while to_visit:
        n = to_visit.popleft()
        up = [-1, 0, 1, 0]
        right = [0, 1, 0, -1]
        for d in range(4):
            if n[0] + up[d] >= 0 and n[1] + right[d] >= 0 and \
                    n[0] + up[d] < len(data_raw) and \
                    n[1] + right[d] < len(data_raw[0]):
                if path_cost[n[0]+up[d]][n[1]+right[d]] == -1 or \
                        data_raw[n[0]+up[d]][n[1]+right[d]] + \
                        path_cost[n[0]][n[1]] < \
                        path_cost[n[0]+up[d]][n[1]+right[d]]:
                    path_cost[n[0]+up[d]][n[1]+right[d]] = \
                            data_raw[n[0]+up[d]][n[1]+right[d]] + \
                            path_cost[n[0]][n[1]]
                    to_visit.append(((n[0]+up[d], n[1]+right[d])))

    return path_cost[-1][-1]

def part_2(data_raw):
    big_data_raw = [[0] * (5 * len(data_raw[0])) \
            for _ in range(5 * len(data_raw))]

    for i in range(len(data_raw)):
        for j in range(len(data_raw[0])):
            for ii in range(5):
                for jj in range(5):
                    big_data_raw[i + (ii*len(data_raw))][j + (jj*len(data_raw[0]))] = \
                            ((data_raw[i][j] + ii + jj - 1) % 9) + 1

    return part_1(big_data_raw)

def file_reader(file_name):
    input_file = open(file_name, 'r')
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace('\n', '')
        inputs_raw[i] = [int(x) for x in inputs_raw[i]]
    return inputs_raw

print(part_1(file_reader('input_15.txt')))
print(part_2(file_reader('input_15.txt')))
