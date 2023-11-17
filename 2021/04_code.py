from collections import defaultdict

def part_1(raw_data):
    draws = raw_data[0].split(',')
    draws = [int(word) for word in draws]
    draw_measure = defaultdict(int)
    for i, d in enumerate(draws):
        draw_measure[d] = i

    counter = 1
    winning_table = (0, 1000)
    lines = []
    real_tables = []
    tables = []
    while counter < len(raw_data):
        counter += 1
        real_tables.append([])
        tables.append([])
        lines.append([])
        for _ in range(5):
            temp = raw_data[counter].split()
            real_tables[-1].append([int(k) for k in temp])
            tables[-1].append([draw_measure[int(k)] for k in temp])
            counter += 1
        # The twelve values of a table:
        cross1, cross2 = 0, 0
        for i in range(5):
            lines[-1].append(max(tables[-1][i]))
            lines[-1].append(max([j[i] for j in tables[-1]]))
            cross1 = max(cross1, tables[-1][i][i])
            cross2 = max(cross2, tables[-1][i][4-i])
        lines[-1].append(cross1)
        lines[-1].append(cross2)
        if min(lines[-1]) < winning_table[1]:
            winning_table = (len(lines)-1, min(lines[-1]))
    
    answer = real_tables[winning_table[0]]
    for draw in draws[:winning_table[1]+1]:
        for i in range(5):
            for j in range(5):
                if draw == answer[i][j]:
                    answer[i][j] = 0
    result = 0
    for line in answer:
        result += sum(line)
    return result * draws[winning_table[1]]


def part_2(raw_data):
    draws = raw_data[0].split(',')
    draws = [int(word) for word in draws]
    draw_measure = defaultdict(int)
    for i, d in enumerate(draws):
        draw_measure[d] = i

    counter = 1
    winning_table = (0, 0)
    lines = []
    real_tables = []
    tables = []
    while counter < len(raw_data):
        counter += 1
        real_tables.append([])
        tables.append([])
        lines.append([])
        for _ in range(5):
            temp = raw_data[counter].split()
            real_tables[-1].append([int(k) for k in temp])
            tables[-1].append([draw_measure[int(k)] for k in temp])
            counter += 1
        # The twelve values of a table:
        cross1, cross2 = 0, 0
        for i in range(5):
            lines[-1].append(max(tables[-1][i]))
            lines[-1].append(max([j[i] for j in tables[-1]]))
            cross1 = max(cross1, tables[-1][i][i])
            cross2 = max(cross2, tables[-1][i][4-i])
        lines[-1].append(cross1)
        lines[-1].append(cross2)
        if min(lines[-1]) > winning_table[1]:
            winning_table = (len(lines)-1, min(lines[-1]))
    
    answer = real_tables[winning_table[0]]
    for draw in draws[:winning_table[1]+1]:
        for i in range(5):
            for j in range(5):
                if draw == answer[i][j]:
                    answer[i][j] = 0
    result = 0
    for line in answer:
        result += sum(line)
    return result * draws[winning_table[1]]

 
def file_reader(file_name):
    input_file = open(file_name, 'r')
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace('\n', '')
    return inputs_raw

print(part_1(file_reader('input_04.txt')))
print(part_2(file_reader('input_04.txt')))
