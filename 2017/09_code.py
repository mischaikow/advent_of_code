def part1(river: str) -> None:
    counter = 0
    garbage_volume = 0
    depth = 0
    pointer = 0
    is_garbage = False
    while pointer < len(river):
        if river[pointer] == "!":
            pointer += 1
        elif river[pointer] == "<" and not is_garbage:
            is_garbage = True
        elif river[pointer] == ">" and is_garbage:
            is_garbage = False
        elif is_garbage:
            garbage_volume += 1
        elif river[pointer] == "{" and not is_garbage:
            depth += 1
        elif river[pointer] == "}" and not is_garbage:
            counter += depth
            depth -= 1

        pointer += 1

    print(f"Part 1: {counter}")
    print(f"Part 2: {garbage_volume}")


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "")
    return inputs_raw[0]


# print(file_reader('09_input.txt'))
part1(file_reader("09_input.txt"))
# part2(file_reader("09_input.txt"))
