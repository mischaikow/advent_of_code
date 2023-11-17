"""Day 10 of the Advent of Code event


"""

def readFile(fileName):
    with open(fileName) as f:
        jolt_list = f.readlines()
    return [int(x.strip()) for x in jolt_list]


def diffCount(jolt_list):
    jolt_list.sort()
    one_count = three_count = 1
    for i in range(1, len(jolt_list)):
        if jolt_list[i] - jolt_list[i-1] == 1:
            one_count += 1
        elif jolt_list[i] - jolt_list[i-1] == 3:
            three_count += 1
    return one_count * three_count


def comboCount(jolt_list):
    jolt_list.sort()
    delta_list = [jolt_list[0] - 0]
    for i in range(1, len(jolt_list)):
        delta_list.append(jolt_list[i] - jolt_list[i-1])
    delta_list.append(3)
    # The set is small, so this is done manually
    one_counter = 0
    answer = 1
    multiplier = [1, 1, 2, 4, 7, 13]
    for i in delta_list:
        if i == 1:
            one_counter += 1
        else:
            answer *= multiplier[one_counter]
            one_counter = 0
    return answer


def main():
    jolt_list = readFile('input_10_1.txt')
    print("Part 1:", diffCount(jolt_list))
    print("Part 2:", comboCount(jolt_list))
    return True


main()
