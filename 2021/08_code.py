def part_1(raw_data):
    ans = 0
    for val in raw_data:
        for num in val[1]:
            if len(num) in {2, 3, 4, 7}:
                ans += 1
    return ans

def part_2(raw_data):
    ans = 0
    for data, val in raw_data:
        words = [''] * 10
        data.sort(key=len)
        for num in data:
            num = set(num)
            if len(num) == 2:
                words[1] = num
            elif len(num) == 3:
                words[7] = num
            elif len(num) == 4:
                words[4] = num
            elif len(num) == 5:
                if all((x in num) for x in words[1]):
                    words[3] = num
                elif all((x in num) for x in (words[4] - words[1])):
                    words[5] = num
                else:
                    words[2] = num
            elif len(num) == 6:
                if all((x in num) for x in words[4]):
                    words[9] = num
                elif all((x in num) for x in words[1]):
                    words[0] = num
                else:
                    words[6] = num
            elif len(num) == 7:
                words[8] = num

        temp = 0
        for num in val:
            temp *= 10
            for i in range(10):
                if words[i] == set(num):
                    temp += i
                    break

        ans += temp

    return ans

 
def file_reader(file_name):
    input_file = open(file_name, 'r')
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace('\n', '')
        inputs_raw[i] = inputs_raw[i].split(' | ')
        inputs_raw[i][0] = inputs_raw[i][0].split(' ')
        inputs_raw[i][1] = inputs_raw[i][1].split(' ')
    return inputs_raw

print(part_1(file_reader('input_08.txt')))
print(part_2(file_reader('input_08.txt')))
