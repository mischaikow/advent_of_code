def part1(inputs_complete: list[str]) -> None:

    complete_mapping = dict()

    pointer = 0
    while inputs_complete[pointer] != "":
        ival, jval = inputs_complete[pointer].split("|")

        if ival not in complete_mapping:
            complete_mapping[ival] = set()
        complete_mapping[ival].add(jval)

        pointer += 1

    pointer += 1

    ans_1 = 0
    ans_2 = 0
    while pointer < len(inputs_complete):
        update_list = inputs_complete[pointer].split(",")

        if is_ordered(update_list, complete_mapping):
            ans_1 += int(update_list[len(update_list) // 2])
        else:
            new_list = sort_poorly(update_list, complete_mapping)
            ans_2 += int(new_list[len(new_list) // 2])

        pointer += 1

    print(f"Part 1: {ans_1}")
    print(f"Part 2: {ans_2}")


def is_ordered(a_list: list[str], mapping: dict[str, set[str]]):
    for i in range(len(a_list)):
        for j in range(i):
            if a_list[j] in mapping[a_list[i]]:
                return False

    return True


def sort_poorly(update_list, complete_mapping):
    while not is_ordered(update_list, complete_mapping):
        for i in range(len(update_list)):
            for j in range(i):
                if update_list[j] in complete_mapping[update_list[i]]:
                    temp = update_list[i]
                    update_list[i] = update_list[j]
                    update_list[j] = temp

    return update_list


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].strip()
    return inputs_raw


part1(file_reader("05_input.txt"))
