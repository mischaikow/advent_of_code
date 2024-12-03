import re


def part1(instruct: str):
    ans_one = 0
    ans_two = 0
    is_live = True

    pattern = re.compile("mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)")
    mults = re.findall(pattern, instruct)
    for m in mults:
        if m[:4] == "mul(":
            vals = m[4:-1].split(",")
            ans_one += int(vals[0]) * int(vals[1])
            if is_live:
                ans_two += int(vals[0]) * int(vals[1])
        elif m == "do()":
            is_live = True
        else:
            is_live = False

    print(f"Part 1: {ans_one}")
    print(f"Part 2: {ans_two}")


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    result = ""
    for ir in inputs_raw:
        result += ir
    return result


part1(file_reader("03_input.txt"))
## part2(file_reader("03_input.txt"))
