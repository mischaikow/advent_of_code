
def part_1(val):
    ans = [0, 0]
    for instruction in val:
        if instruction[0] == "forward":
            ans[0] += instruction[1]
        elif instruction[0] == "down":
            ans[1] += instruction[1]
        else:
            ans[1] -= instruction[1]
    return ans[0] * ans[1]


def part_2(val):
    aim = 0
    ans = [0, 0]
    for instruction in val:
        if instruction[0] == "forward":
            ans[0] += instruction[1]
            ans[1] += instruction[1] * aim
        elif instruction[0] == "down":
            aim += instruction[1]
        else:
            aim -= instruction[1]
    return ans[0] * ans[1]
 

def file_reader(file_name):
    input_file = open(file_name, 'r')
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace('\n', '')
        front, back = inputs_raw[i].split()
        inputs_raw[i] = [front, int(back)]
    return inputs_raw

print(part_1(file_reader('input_02.txt')))
print(part_2(file_reader('input_02.txt')))
