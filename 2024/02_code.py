def check_interval(is_decreasing: bool, val_1: int, val_2: int) -> bool:
    if is_decreasing:
        return -4 < val_2 - val_1 < 0
    return 0 < val_2 - val_1 < 4


def passes_one(level: list[int]) -> bool:

    is_decreasing = level[1] < level[0]

    for i in range(len(level) - 1):
        if not check_interval(is_decreasing, level[i], level[i + 1]):
            return False

    return True


def passes_two(level: list[int]) -> bool:

    for i in range(len(level)):
        if passes_one(level[:i] + level[i + 1 :]):
            return True
    return False


def part1(feed: list[list[int]]) -> None:
    ans_1 = 0
    ans_2 = 0

    for level in feed:
        if passes_one(level):
            ans_1 += 1
        if passes_two(level):
            ans_2 += 1

    print(f"Part 1: {ans_1}")
    print(f"Part 2: {ans_2}")


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].split()
        inputs_raw[i] = [int(x) for x in inputs_raw[i]]
    return inputs_raw


part1(file_reader("02_input.txt"))
