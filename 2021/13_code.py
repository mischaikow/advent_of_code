
def solution(raw_data):
    points = []
    folds = []
    x_max, y_max = 0, 0
    for i in range(len(raw_data)):
        if len(raw_data[i]) > 0:
            if raw_data[i][0] == 'f':
                dummy = raw_data[i].split(' ')
                dummy = dummy[2].split('=')
                folds.append([dummy[0], int(dummy[1])])
            else:
                points.append([int(c) for c in raw_data[i].split(',')])
                x_max = max(x_max, points[-1][0]+1)
                y_max = max(y_max, points[-1][1]+1)

    table = [[0] * y_max for _ in range(x_max)]
    for p in points:
        table[p[0]][p[1]] = 1

    toPrint = True
    for f in folds:
        if f[0] == 'x':
            for y in range(len(table[0])):
                for x in range(f[1], len(table)):
                    table[2*f[1] - x][y] |= table[x][y]
            table = table[:f[1]+1]
        elif f[0] == 'y':
            for x in range(len(table)):
                for y in range(f[1], len(table[x])):
                    table[x][2*f[1] - y] |= table[x][y]
                table[x] = table[x][:f[1]+1]

        if toPrint:
            toPrint = False 
            ans = 0
            for row in table:
                for cell in row:
                    ans += cell

    print('\nTHE FINAL CODE IS:\n')
    for y in range(len(table[0])):
        newline = []
        for x in range(len(table)):
            newline.append('#' if table[x][y] else ' ')
        print(''.join(newline))

    return ans

def file_reader(file_name):
    input_file = open(file_name, 'r')
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace('\n', '')
    return inputs_raw

print(solution(file_reader('input_13.txt')))
