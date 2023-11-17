
def part_1(raw_data):
    
    for i, line in enumerate(raw_data):
        points = line.split(" -> ")
        start = points[0].split(",")
        end = points[1].split(",")
        raw_data[i] = [int(start[0]), int(start[1]), int(end[0]), int(end[1])]
        start[0], start[1] = int(start[0]), int(start[1])
        end[0], end[1] = int(end[0]), int(end[1])

    to_consider = []
    max_x, max_y = 0, 0
    for line in raw_data:
        if line[0] == line[2] or line[1] == line[3]:
            to_consider.append(line)
            max_x = max(max_x, line[0], line[2])
            max_y = max(max_y, line[1], line[3])

    max_x += 1
    max_y += 1
    sea_map = [[0] * max_y for _ in range(max_x)]

    for line in to_consider:
        if line[0] == line[2]:
            start = min(line[1], line[3])
            end = max(line[1], line[3])
            for i in range(start, end+1):
                sea_map[line[0]][i] += 1
        else:
            start = min(line[0], line[2])
            end = max(line[0], line[2])
            for i in range(start, end+1):
                sea_map[i][line[1]] += 1

    answer = 0
    for row in sea_map:
        for col in row:
            if col > 1:
                answer += 1

    return answer

    

def part_2(raw_data):
    
    to_consider = []
    max_x, max_y = 0, 0
    for i, line in enumerate(raw_data):
        points = line.split(" -> ")
        start = points[0].split(",")
        end = points[1].split(",")
        to_consider.append([int(start[0]), int(start[1]), int(end[0]), int(end[1])])
        max_x = max(max_x, int(start[0]), int(end[0]))
        max_y = max(max_y, int(start[1]), int(end[1]))

    max_x += 1
    max_y += 1
    sea_map = [[0] * max_y for _ in range(max_x)]

    for line in to_consider:
        if line[0] == line[2]:
            start = min(line[1], line[3])
            end = max(line[1], line[3])
            for i in range(start, end+1):
                sea_map[line[0]][i] += 1
        elif line[1] == line[3]:
            start = min(line[0], line[2])
            end = max(line[0], line[2])
            for i in range(start, end+1):
                sea_map[i][line[1]] += 1
        else:
            start_x = line[0]
            end_x = line[2]
            start_y = line[1]
            end_y = line[3]
            if end_x > start_x:
                x = 1
            else:
                x = -1
            if end_y > start_y:
                y = 1
            else:
                y = -1
            for i in range(1 + abs(end_x - start_x)):
                sea_map[start_x + (x*i)][start_y + (y*i)] += 1

    answer = 0
    for row in sea_map:
        for col in row:
            if col > 1:
                answer += 1

    return answer

 
def file_reader(file_name):
    input_file = open(file_name, 'r')
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace('\n', '')
    return inputs_raw

print(part_1(file_reader('input_05.txt')))
print(part_2(file_reader('input_05.txt')))
