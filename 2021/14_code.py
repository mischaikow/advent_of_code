from collections import defaultdict
from collections import Counter
from copy import copy

def part_1(data_raw, cycles):
    polymer = list(data_raw[0])
    poly_insert_dict = defaultdict(str)

    for relay in data_raw[2:]:
        poly_insert_dict[relay[0:2]] = relay[6]

    for _ in range(cycles):
        temp = [''] * (2 * len(polymer) - 1)
        temp[0] = polymer[0]
        for i in range(len(polymer)-1):
            temp[2*i + 1] = poly_insert_dict[polymer[i] + polymer[i+1]]
            temp[2*i + 2] = polymer[i+1]
        polymer = temp

    count = Counter(polymer)
    small, big = len(polymer), 0
    for val in count:
        big = max(big, count[val])
        small = min(small, count[val])

    return big - small

def part_2(data_raw, cycles):
    pair_counter = defaultdict(int)
    for i in range(len(data_raw[0]) - 1):
        pair_counter[data_raw[0][i:i+2]] += 1

    pair_map = defaultdict(list)
    for relay in data_raw[2:]:
        start = relay[:2]
        end = start[0] + relay[6] + start[1]
        pair_map[start] = [end[:2], end[1:]]

    for _ in range(cycles):
        temp = defaultdict(int)
        for pair in pair_counter:
            for result in pair_map[pair]:
                temp[result] += pair_counter[pair]
        pair_counter = temp
    
    ans_storage = defaultdict(int)
    for pair in pair_counter:
        for char in pair:
            ans_storage[char] += pair_counter[pair]

    ans_storage[data_raw[0][0]] += 1
    ans_storage[data_raw[0][-1]] += 1

    small, big = 2 ** cycles * len(data_raw[0]), 0
    for val in ans_storage:
        big = max(big, ans_storage[val])
        small = min(small, ans_storage[val])

    return (big - small) // 2

 
def file_reader(file_name):
    input_file = open(file_name, 'r')
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace('\n', '')
    return inputs_raw

print(part_1(file_reader('input_14.txt'), 10))
print(part_2(file_reader('input_14.txt'), 40))
