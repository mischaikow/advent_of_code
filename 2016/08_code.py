def part1(input_str: list[str]) -> int:
    display = [[0] * 50 for _ in range(6)]
    for a_line in input_str:
        if a_line[0] == "rect":
            w, h = a_line[1].split("x")
            width = int(w)
            height = int(h)
            print(f"({width}, {height})")
            for i in range(height):
                for j in range(width):
                    display[i][j] = 1

        elif a_line[0] == "rotate":
            _, r_target = a_line[2].split("=")
            rotate_target = int(r_target)
            rotate_volume = int(a_line[4])

            if a_line[1] == "row":
                new = (
                    display[rotate_target][
                        len(display[rotate_target]) - rotate_volume :
                    ]
                    + display[rotate_target][
                        : len(display[rotate_target]) - rotate_volume
                    ]
                )
                display[rotate_target] = new

            else:
                old = []
                for i in range(len(display)):
                    old.append(display[i][rotate_target])
                new = (
                    old[len(display) - rotate_volume :]
                    + old[: len(display) - rotate_volume]
                )

                for i in range(len(display)):
                    display[i][rotate_target] = new[i]

    dummy = []
    for line in display:
        dummy.append([])
        for val in line:
            if val == 0:
                dummy[-1].append(".")
            elif val == 1:
                dummy[-1].append("X")

    for l in dummy:
        print("".join([str(x) for x in l]))

    ans = 0
    for line in display:
        ans += sum(line)
    return ans


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "").split()
    return inputs_raw


## print(file_reader("08_input.txt"))
print(f"Part 1: {part1(file_reader('08_input.txt'))}")
## print(f"Part 2: {part2(file_reader('08_input.txt'))}")
