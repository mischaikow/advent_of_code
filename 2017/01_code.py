def part1(captch_code: str) -> None:
    ans_one = 0
    ans_two = 0
    pointer = 0
    while pointer < len(captch_code):
        if captch_code[pointer] == captch_code[(pointer + 1) % len(captch_code)]:
            ans_one += int(captch_code[pointer])
        if (
            captch_code[pointer]
            == captch_code[(pointer + len(captch_code) // 2) % len(captch_code)]
        ):
            ans_two += int(captch_code[pointer])
        pointer += 1

    print(f"Part 1: {ans_one}")
    print(f"Part 2: {ans_two}")


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "")
    return inputs_raw[0]


# print(file_reader('01_input.txt'))
part1(file_reader("01_input.txt"))
# print(part2(file_reader('01_input.txt')))
