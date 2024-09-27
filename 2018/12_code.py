def part1(encoding: list[str]) -> None:
    raw_initial_state = encoding[0]
    pots_list = raw_initial_state.split(" ")
    current_pots = ["."] * len(pots_list[2])

    for i in range(len(pots_list[2])):
        current_pots[i] = pots_list[2][i]
    current_pots = "".join(current_pots)
    minimum_pot = 0

    mapping = {}
    for line in encoding[2:]:
        line_list = line.split(" ")
        mapping[line_list[0]] = line_list[2]

    count = 0
    ans = 0
    j = 0
    while True:
        j += 1
        new_pots = ""
        new_pots += mapping["..." + current_pots[:2]]
        new_pots += mapping[".." + current_pots[:3]]
        new_pots += mapping["." + current_pots[:4]]
        for i in range(len(current_pots) - 4):
            new_pots += mapping[current_pots[i : i + 5]]
        new_pots += mapping[current_pots[-4:] + "."]
        new_pots += mapping[current_pots[-3:] + ".."]
        new_pots += mapping[current_pots[-2:] + "..."]
        minimum_pot -= 1
        while new_pots[0] == ".":
            new_pots = new_pots[1:]
            minimum_pot += 1
        current_pots = new_pots

        old_count = count
        old_ans = ans
        ans = 0
        count = 0
        for i in range(len(current_pots)):
            if current_pots[i] == "#":
                ans += i + minimum_pot
                count += 1

        if j == 20:
            print(f"Part 1: {ans}")

        if old_count == count and old_ans == (ans - count):
            break

    result = count * (50_000_000_000 - j) + ans
    print(f"Part 2: {result}")


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "")
    return inputs_raw


light_data_raw = file_reader("12_input.txt")
part1(light_data_raw)
