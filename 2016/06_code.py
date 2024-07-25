from typing import List
from collections import defaultdict


def part1(input_str: List[str]) -> None:
    counters = [defaultdict(int) for _ in range(len(input_str[0]))]
    for a_line in input_str:
        for pointer in range(len(a_line)):
            counters[pointer][a_line[pointer]] += 1

    ans = ""
    two_ans = ""
    for a_counter in counters:
        record = 0
        answer = ""
        pt2_record = len(input_str)
        pt2_answer = ""
        for key, value in a_counter.items():
            if value > record:
                record = value
                answer = key
            if value < pt2_record:
                pt2_record = value
                pt2_answer = key
        ans += answer
        two_ans += pt2_answer

    print(f"Part 1: {ans}")
    print(f"Part 2: {two_ans}")


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "")
    return inputs_raw


# print(file_reader('06_input.txt'))
part1(file_reader("06_input.txt"))
## part2(file_reader('06_input.txt'))
