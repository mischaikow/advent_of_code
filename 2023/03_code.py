def part1(str_list):
    ans = 0

    for i in range(len(str_list)):
        j = 0
        while j < len(str_list[0]):
            if str_list[i][j].isdigit():
                is_hot = False
                number = 0
                while j < len(str_list[0]) and str_list[i][j].isdigit():
                    number = number*10 + int(str_list[i][j])
                    is_hot = is_hot or check_surroundings(str_list, i, j)
                    j += 1
                if is_hot:
                    ans += number
            j += 1

    print(ans)


def part2(str_list):
    ans = 0

    for i in range(len(str_list)):
        for j in range(len(str_list[0])):
            if str_list[i][j] == '*':
                values = []
                if i > 0:
                    if not str_list[i-1][j].isdigit():
                        if j > 0 and str_list[i-1][j-1].isdigit():
                            values.append(pull_number(str_list, i-1, j-1))
                        if j < len(str_list[0])-1 and str_list[i-1][j+1].isdigit():
                            values.append(pull_number(str_list, i-1, j+1))
                    elif str_list[i-1][j].isdigit():
                        values.append(pull_number(str_list, i-1, j))
                if i < len(str_list)-1:
                    if not str_list[i+1][j].isdigit():
                        if j > 0 and str_list[i+1][j-1].isdigit():
                            values.append(pull_number(str_list, i+1, j-1))
                        if j < len(str_list[0])-1 and str_list[i+1][j+1].isdigit():
                            values.append(pull_number(str_list, i+1, j+1))
                    elif str_list[i+1][j].isdigit():
                        values.append(pull_number(str_list, i+1, j))
                if j > 0 and str_list[i][j-1].isdigit():
                    values.append(pull_number(str_list, i, j-1))
                if j < len(str_list[0])-1 and str_list[i][j+1].isdigit():
                    values.append(pull_number(str_list, i, j+1))

                if len(values) == 2:
                    print(f'At coord ({i}, {j}) -- first num: {values[0]}, second num: {values[1]}')
                    ans += values[0] * values[1]

    print(ans)


def pull_number(str_list, i, j):
    while j > 0 and str_list[i][j-1].isdigit():
        j -= 1

    ans = 0
    while j < len(str_list[0]) and str_list[i][j].isdigit():
        print(ans)
        ans = ans*10 + int(str_list[i][j])
        j += 1

    return ans


def check_is_symbol(a_char):
    if a_char.isdigit():
        return False
    if a_char == '.':
        return False
    return True

def check_surroundings(str_list, i, j):
    if i > 0:
        if check_is_symbol(str_list[i-1][j]):
            return True
        if j > 0:
            if check_is_symbol(str_list[i-1][j-1]):
                return True
        if j < len(str_list[0])-1:
            if check_is_symbol(str_list[i-1][j+1]):
                return True
    if i < len(str_list)-1:
        if check_is_symbol(str_list[i+1][j]):
            return True
        if j > 0:
            if check_is_symbol(str_list[i+1][j-1]):
                return True
        if j < len(str_list[0])-1:
            if check_is_symbol(str_list[i+1][j+1]):
                return True
    if j > 0:
        if check_is_symbol(str_list[i][j-1]):
            return True
    if j < len(str_list[0])-1:
        if check_is_symbol(str_list[i][j+1]):
            return True
    return False
        




def file_reader(file_name):
    input_file = open(file_name, 'r')
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace('\n','')
    return inputs_raw

part1(file_reader('03_input.txt'))
part2(file_reader('03_input.txt'))
