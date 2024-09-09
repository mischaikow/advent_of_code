LINES = ["|", "-"]


def part1(packet_map: list[str]) -> int:
    ans = []

    coords = [0, 0]

    for i in range(len(packet_map[0])):
        if packet_map[0][i] == "|":
            coords[1] = i
            break

    d = [1, 0]
    step_counter = 0

    while True:
        current_value = packet_map[coords[0]][coords[1]]

        if current_value == "+":
            if packet_map[coords[0] + d[1]][coords[1] + d[0]] == " ":
                temp = d[0]
                d[0] = -1 * d[1]
                d[1] = -1 * temp
            else:
                temp = d[0]
                d[0] = d[1]
                d[1] = temp

        elif current_value == " ":
            print(f"Part 1: {''.join(ans)}")
            return step_counter

        elif current_value not in LINES:
            ans.append(current_value)

        coords[0] += d[0]
        coords[1] += d[1]
        step_counter += 1


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "")
    return inputs_raw


print(f"Part 2: {part1(file_reader('19_input.txt'))}")
