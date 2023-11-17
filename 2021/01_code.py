def part_1(data):
    ans = 0
    last = data[0]
    for i in data[1:]:
        if i > last:
            ans += 1
        last = i
    return ans

def part_2(data):
    ans = 0
    for i in range(3, len(data)):
        if data[i] > data[i-3]:
            ans += 1
    return ans

def file_reader(file_name):
    input_file = open(file_name, 'r')
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace('\n', '')
        inputs_raw[i] = int(inputs_raw[i])
    return inputs_raw

print(part_1(file_reader('input_01.txt')))
print(part_2(file_reader('input_01.txt')))
