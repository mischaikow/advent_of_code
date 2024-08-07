def part1(disc_pos: list[str]) -> int:
    discs = []
    for a_disc in disc_pos:
        a_disc = a_disc.split(" ")
        discs.append(
            (
                (
                    int(a_disc[3]),
                    (int(a_disc[-1][:-1]) + int(a_disc[1][1:])) % int(a_disc[3]),
                )
            )
        )

    # For part 1, commend out this additional disc
    discs.append(((11, 7)))

    time = 0
    while True:
        test = 0
        for a_disc in discs:
            test += (time + a_disc[1]) % a_disc[0]
            if test > 0:
                break
        if test == 0:
            return time
        time += 1


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "")
    return inputs_raw


## print(file_reader("15_input.txt"))
print(f"Part 1: {part1(file_reader('15_input.txt'))}")
## print(f"Part 2: {part2(file_reader('15_input.txt'))}")
