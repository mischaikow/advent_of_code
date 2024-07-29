def part1(captch_code: list[list[int]]) -> None:
    ans = 0
    for a_line in captch_code:
        ans += max(a_line) - min(a_line)
    print(f"Part 1: {ans}")


def perfect_divisor(numbers: list[int]) -> int:
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if max(numbers[i], numbers[j]) % min(numbers[i], numbers[j]) == 0:
                return max(numbers[i], numbers[j]) // min(numbers[i], numbers[j])


def part2(captch_code: list[list[int]]) -> None:
    ans = 0
    for a_line in captch_code:
        ans += perfect_divisor(a_line)
    print(f"Part 2: {ans}")


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "").split()
        inputs_raw[i] = [int(x) for x in inputs_raw[i]]
    return inputs_raw


# print(file_reader('02_input.txt'))
part1(file_reader("02_input.txt"))
part2(file_reader("02_input.txt"))
