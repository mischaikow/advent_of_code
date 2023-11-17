import math

def snail_add(n_1, n_2):
    result = ['['] + n_1 + [','] + n_2 + [']']
    while True:
        isExplode, isSplit = False, False
        isExplode, result = snail_explode(result)
        if not isExplode:
            isSplit, result = snail_split(result)
        if not isSplit and not isExplode:
            break
    return result

def snail_split(number):
    for i, char in enumerate(number):
        if isinstance(char, int) and char > 9:
            insert = ['[',
                    math.floor(char/2),
                    ',',
                    math.ceil(char/2),
                    ']']
            return True, number[:i] + insert + number[i+1:]
    return False, number

def snail_explode(number):
    depth = 0
    for i, char in enumerate(number):
        if char == '[':
            depth += 1
        elif char == ']':
            depth -= 1
        elif depth == 5:
            left_val = char
            right_val = number[i+2]

            for j in range(i-1, -1, -1):
                if isinstance(number[j], int):
                    number[j] += left_val
                    break

            for j in range(i+4, len(number), 1):
                if isinstance(number[j], int):
                    number[j] += right_val
                    break

            return True, number[:i-1] + [0] + number[i+4:]
    return False, number

def snail_magnitude(number):
    if len(number) == 0:
        return 0
    if len(number) == 1:
        return number[0]
    depth = 0
    for i in range(len(number)):
        if number[i] == '[':
            depth += 1
        elif number[i] == ']':
            depth -= 1
        elif depth == 1 and number[i] == ',':
            midpoint = i
    return 3*snail_magnitude(number[1:midpoint]) + 2*snail_magnitude(number[midpoint+1:len(number)-1])

def part_1(snail_numbers):
    value = snail_numbers[0]
    for sn in snail_numbers[1:]:
        value = snail_add(value, sn)
    return snail_magnitude(value)

def part_2(snail_numbers):
    ans = 0
    for i in range(len(snail_numbers)):
        for j in range(len(snail_numbers)):
            if i != j:
                ans = max(ans, snail_magnitude(snail_add(snail_numbers[i],
                    snail_numbers[j])))
    return ans

def file_reader(file_name):
    input_file = open(file_name, 'r')
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace('\n','')
        inputs_raw[i] = list(inputs_raw[i])
        for j in range(len(inputs_raw[i])):
            if inputs_raw[i][j].isnumeric():
                inputs_raw[i][j] = int(inputs_raw[i][j])
    return inputs_raw

print(part_1(file_reader('input_18.txt')))
print(part_2(file_reader('input_18.txt')))
