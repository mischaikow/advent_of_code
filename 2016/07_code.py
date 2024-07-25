from typing import List


def part1(input_str: List[str]) -> int:
    ans = 0
    for ipadd in input_str:
        in_bracket = False
        is_valid = False
        for pointer in range(len(ipadd) - 3):
            if ipadd[pointer] == "[":
                in_bracket = True
            elif ipadd[pointer] == "]":
                in_bracket = False
            elif (
                ipadd[pointer] == ipadd[pointer + 3]
                and ipadd[pointer + 1] == ipadd[pointer + 2]
                and ipadd[pointer] != ipadd[pointer + 1]
            ):
                if in_bracket:
                    is_valid = False
                    break
                else:
                    is_valid = True

        if is_valid:
            ans += 1

    return ans


def part2(input_str: List[str]) -> int:
    ans = 0
    for ipadd in input_str:
        in_bracket = False
        in_bracket_abas = set()
        out_bracket_abas = set()
        for pointer in range(len(ipadd) - 2):
            if ipadd[pointer] == "[":
                in_bracket = True
            elif ipadd[pointer] == "]":
                in_bracket = False
            elif (
                ipadd[pointer] == ipadd[pointer + 2]
                and ipadd[pointer + 1] != "["
                and ipadd[pointer + 1] != "]"
            ):
                if in_bracket:
                    in_bracket_abas.add(ipadd[pointer : pointer + 3])
                else:
                    out_bracket_abas.add(ipadd[pointer : pointer + 3])

        for in_aba in in_bracket_abas:
            if in_aba[1] + in_aba[0] + in_aba[1] in out_bracket_abas:
                ans += 1
                break

    return ans


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "")
    return inputs_raw


## print(file_reader("07_input.txt"))
print(f"Part 1: {part1(file_reader('07_input.txt'))}")
print(f"Part 2: {part2(file_reader('07_input.txt'))}")
