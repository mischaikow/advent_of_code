def part1(jumps: list[int]) -> None:
    pointer = 0
    counter = 0
    added_offset = [0] * len(jumps)
    while 0 <= pointer < len(jumps):
        added_offset[pointer] += 1
        pointer += jumps[pointer] + added_offset[pointer] - 1
        counter += 1
    print(f"Part 1: {counter}")


def part2(jumps: list[int]) -> None:
    pointer = 0
    counter = 0
    added_offset = [0] * len(jumps)
    while 0 <= pointer < len(jumps):
        old_pointer = pointer
        pointer += jumps[pointer] + added_offset[pointer]
        if jumps[old_pointer] + added_offset[old_pointer] >= 3:
            added_offset[old_pointer] -= 1
        else:
            added_offset[old_pointer] += 1
        counter += 1
    print(f"Part 2: {counter}")


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = int(inputs_raw[i].replace("\n", ""))
    return inputs_raw


# print(file_reader('05_input.txt'))
part1(file_reader("05_input.txt"))
part2(file_reader("05_input.txt"))
