from collections import defaultdict


OPERATIONS = {
    "<": lambda x, y: x < y,
    ">": lambda x, y: x > y,
    ">=": lambda x, y: x >= y,
    "<=": lambda x, y: x <= y,
    "==": lambda x, y: x == y,
    "!=": lambda x, y: x != y,
}


def part1(jumps: list[list[str]]) -> None:
    registers = defaultdict(int)

    highest_value = 0

    for instruct in jumps:
        if OPERATIONS[instruct[5]](registers[instruct[4]], int(instruct[6])):
            if instruct[1] == "inc":
                registers[instruct[0]] += int(instruct[2])
            else:
                registers[instruct[0]] -= int(instruct[2])
            highest_value = max(highest_value, registers[instruct[0]])

    ans = 0
    for value in registers.values():
        ans = max(ans, value)
    print(f"Part 1: {ans}")
    print(f"Part 2: {highest_value}")


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "").split(" ")
    return inputs_raw


# print(file_reader('08_input.txt'))
part1(file_reader("08_input.txt"))
# part2(file_reader("08_input.txt"))
