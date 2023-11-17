def print_2d_table(data):
    print('[')
    for row in data:
        print(row)
    print(']')

def part_1(data_raw):
    ans = 0

    table = [[0] * (2 + len(data_raw[0]))]
    for row in data_raw:
        table.append([0] + row + [0])
    table.append([0] * (2 + len(data_raw[0])))

    i_n = [-1, -1, 0, 1, 1, 1, 0, -1]
    j_n = [0, 1, 1, 1, 0, -1, -1, -1]

    ##  For the solution to part 2, change the below range to something
    # bigger, like 500.
    for step in range(500):
        to_glow = []
        
        for i in range(1, len(table)-1):
            for j in range(1, len(table[0])-1):
                table[i][j] += 1
                if table[i][j] > 9:
                    to_glow.append((i,j))

        while to_glow:
            i, j = to_glow.pop()
            if i < 1 or j < 1 or i > len(table)-2 or j > len(table[0])-2:
                pass
            elif table[i][j] != -1:
                table[i][j] = -1
                ans += 1
                for k in range(8):
                    if table[i+i_n[k]][j+j_n[k]] != -1:
                        table[i+i_n[k]][j+j_n[k]] += 1
                    if table[i+i_n[k]][j+j_n[k]] > 9:
                        to_glow.append((i+i_n[k],j+j_n[k]))

        temp = 0
        for i in range(1, len(table)-1):
            for j in range(1, len(table[0])-1):
                if table[i][j] == -1:
                    table[i][j] = 0
                temp += table[i][j]

        if temp == 0:
            #steps are index 0, but the puzzle is index 1 =)
            ##  Part 2 answer:
            return step+1
        
    ##  Part 1 answer:
    return ans

def file_reader(file_name):
    input_file = open(file_name, 'r')
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace('\n', '')
        inputs_raw[i] = [int(val) for val in inputs_raw[i]]
    return inputs_raw

print(part_1(file_reader('input_11.txt')))
