
def part_1(raw_data):
    raw_data.sort()
    median = raw_data[len(raw_data)//2]
    ans = 0
    for val in raw_data:
        ans += abs(val - median)
    return ans

def part_2(raw_data):
    average = int(round(sum(raw_data) / len(raw_data), 0))
    adjusted_average = average - 1
    ans = 0
    for val in raw_data:
        distance = abs(val - adjusted_average)
        ans += (distance * (distance + 1)) // 2
    return ans

def file_reader(file_name):
    input_file = open(file_name, 'r')
    inputs_raw = input_file.readlines()[0].replace('\n', '').split(',')
    return [int(i) for i in inputs_raw]

print(part_1(file_reader('input_07.txt')))
print(part_2(file_reader('input_07.txt')))
