# left is +1, right is -1
DIRECTIONS = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def part1(starting_map: list[str]) -> int:
    infections = set()

    for i in range(len(starting_map)):
        for j in range(len(starting_map[i])):
            if starting_map[i][j] == "#":
                infections.add(((i, j)))

    vc_d = 1
    vc_loc = (len(starting_map) // 2, len(starting_map[0]) // 2)

    ans = 0
    # cycle:
    for _ in range(10_000):
        if vc_loc in infections:
            vc_d = (vc_d - 1) % 4
        else:
            vc_d = (vc_d + 1) % 4

        if vc_loc in infections:
            infections.remove(vc_loc)
        else:
            infections.add(vc_loc)
            ans += 1

        vc_loc = (vc_loc[0] + DIRECTIONS[vc_d][0], vc_loc[1] + DIRECTIONS[vc_d][1])

    return ans


def part2(starting_map: list[str]) -> int:
    infections = set()
    weakened = set()
    flagged = set()

    for i in range(len(starting_map)):
        for j in range(len(starting_map[i])):
            if starting_map[i][j] == "#":
                infections.add(((i, j)))

    vc_d = 1
    vc_loc = (len(starting_map) // 2, len(starting_map[0]) // 2)

    ans = 0
    # cycle:
    for _ in range(10_000_000):
        if vc_loc in infections:
            vc_d = (vc_d - 1) % 4
        elif vc_loc in weakened:
            pass
        elif vc_loc in flagged:
            vc_d = (vc_d + 2) % 4
        else:
            vc_d = (vc_d + 1) % 4

        if vc_loc in infections:
            infections.remove(vc_loc)
            flagged.add(vc_loc)
        elif vc_loc in weakened:
            weakened.remove(vc_loc)
            infections.add(vc_loc)
            ans += 1
        elif vc_loc in flagged:
            flagged.remove(vc_loc)
        else:
            weakened.add(vc_loc)

        vc_loc = (vc_loc[0] + DIRECTIONS[vc_d][0], vc_loc[1] + DIRECTIONS[vc_d][1])

    return ans


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "")
    return inputs_raw


print(f"Part 1: {part1(file_reader('22_input.txt'))}")
print(f"Part 2: {part2(file_reader('22_input.txt'))}")
