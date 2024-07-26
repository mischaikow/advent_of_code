from typing import List


def part1(input_str: str) -> int:
    new_str = ''
    pointer = 0
    while pointer < len(input_str):
        if input_str[pointer] == '(':
            end = input_str.find(')', pointer+1)
            repeat_length, repeat_count = input_str[pointer+1:end].split('x')
            repeat_length = int(repeat_length)
            repeat_count = int(repeat_count)

            for _ in range(repeat_count):
                new_str += input_str[end+1:end+1+repeat_length]

            pointer = end + repeat_length
        else:
            new_str += input_str[pointer]
        pointer += 1

    return len(new_str)


def block_length(compute_str: str) -> int:
    end = compute_str.find(')')
    repeat_length, repeat_count = compute_str[pointer+1:end].split('x')
    repeat_length = int(repeat_length)
    repeat_count = int(repeat_count)

    pointer = end+1
    while pointer < len(compute_str):
        if compute_str[pointer] == '(':
            return pointer + block_length(compute_str[pointer:])


def part2(input_str: str) -> int:
    pointer = 0
    ans = 0
    while pointer < len(input_str):
        if input_str[pointer] == '(':
            end = input_str.find(')', pointer+1)
            repeat_length, repeat_count = input_str[pointer+1:end].split('x')
            repeat_length = int(repeat_length)
            repeat_count = int(repeat_count)

            ans += repeat_count * part2(input_str[end+1:end+1+repeat_length])
            pointer = end+1+repeat_length
        else:
            ans += 1
            pointer += 1
    
    return ans


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "")
    return inputs_raw[0]


## print(file_reader("09_input.txt"))
#print(f"Part 1: {part1('A(1x5)BC')}")
#print(f"Part 1: {part1('(3x3)XYZ')}")
#print(f"Part 2: {part2('(3x3)XYZ')}")
#print(f"Part 2: {part2('X(8x2)(3x3)ABCY')}")
#print(f"Part 2: {part2('(27x12)(20x12)(13x14)(7x10)(1x12)A')}")
print(f"Part 1: {part1(file_reader('09_input.txt'))}")
print(f"Part 2: {part2(file_reader('09_input.txt'))}")
