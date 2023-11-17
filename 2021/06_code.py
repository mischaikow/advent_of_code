
def solution(raw_data, days):
    fish = [0] * 9
    for age in raw_data:
        fish[age] += 1
    for _ in range(days):
        new = [0] * 9
        for i, count in enumerate(fish):
            if i == 0:
                new[6] = count
                new[8] = count
            else:
                new[i-1] += count
        fish = new
    return sum(fish)

def file_reader(file_name):
    input_file = open(file_name, 'r')
    inputs_raw = input_file.readlines()[0].replace('\n', '').split(',')
    return [int(i) for i in inputs_raw]

print(solution(file_reader('input_06.txt'), 80))
print(solution(file_reader('input_06.txt'), 256))
