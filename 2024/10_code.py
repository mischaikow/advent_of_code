DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def part1(full_map: list[str]):

    int_map = []
    for line in full_map:
        int_map.append([int(x) for x in line])

    ans = 0
    trailhead_ratings = 0
    for i, line in enumerate(int_map):
        for j, val in enumerate(line):
            if val == 0:
                path_endings = set()
                paths = [(i, j, 0)]
                while len(paths) > 0:
                    i_coord, j_coord, alt = paths.pop()
                    for d in DIRECTIONS:
                        new_i_coord = i_coord + d[0]
                        new_j_coord = j_coord + d[1]
                        if (
                            0 <= new_i_coord < len(int_map)
                            and 0 <= new_j_coord < len(int_map[0])
                            and int_map[new_i_coord][new_j_coord] == alt + 1
                        ):
                            if int_map[new_i_coord][new_j_coord] == 9:
                                path_endings.add(((new_i_coord, new_j_coord)))
                                trailhead_ratings += 1
                            else:
                                paths.append(((new_i_coord, new_j_coord, alt + 1)))

                ans += len(path_endings)

    print(f"Part 1: {ans}")
    print(f"Part 2: {trailhead_ratings}")


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].strip()
    return inputs_raw


part1(file_reader("10_input.txt"))
