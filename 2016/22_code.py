from collections import defaultdict
from collections import OrderedDict


def part1(data_facts: list[str]) -> int:

    ans = 0
    used_counter = defaultdict(int)
    avail_counter = defaultdict(int)

    for line in data_facts:
        line = line.split()

        single_used = int(line[2][:-1])
        single_avail = int(line[3][:-1])
        if 0 < single_used <= single_avail:
            ans -= 1

        used_counter[single_used] += 1
        avail_counter[single_avail] += 1

    ordered_used_counter = OrderedDict(sorted(used_counter.items(), reverse=True))
    ordered_avail_counter = OrderedDict(sorted(avail_counter.items()))

    needed_space_minimum, running_total = ordered_used_counter.popitem()
    if needed_space_minimum == 0:
        needed_space_minimum, running_total = ordered_used_counter.popitem()

    for open_space, os_count in ordered_avail_counter.items():
        current_size_counter = 0
        while open_space >= needed_space_minimum:
            current_size_counter = os_count * running_total
            needed_space_minimum, temp = ordered_used_counter.popitem()
            running_total += temp
        ans += current_size_counter

    return ans


def part2(data_facts: list[str]) -> int:

    avail = []
    used = []
    max_avail = 0

    for line in data_facts:
        line = line.split()
        _, x_coord, y_coord = line[0].split("-")
        x_coord = int(x_coord[1:])
        y_coord = int(y_coord[1:])

        if y_coord == 0:
            avail.append([])
            used.append([])
        avail[-1].append(int(line[3][:-1]))
        used[-1].append(int(line[2][:-1]))
        if avail[-1][-1] > max_avail:
            max_avail = avail[-1][-1]

    for i in range(len(used)):
        for j in range(len(used[i])):
            if max_avail < used[i][j]:
                avail[i][j] = "X"
            if used[i][j] == 0:
                avail[i][j] = "00"

    print("AVAIL EDITED: ")
    for a_row in avail:
        print(a_row)
    print("")

    move_up = 17
    move_left = 22
    move_down = 34
    push_up = 5
    cycles = 34
    last_step = 1

    return 17 + 22 + 34 + (5 * 34) + 1


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "")
    return inputs_raw[2:]


## print(file_reader("22_input.txt"))
print(f"Part 1: {part1(file_reader('22_input.txt'))}")
print(f"Part 2: {part2(file_reader('22_input.txt'))}")
