def part1(full_map: list[str]):

    i_size = len(full_map)
    j_size = len(full_map[0])

    antenni = dict()

    for i, line in enumerate(full_map):
        for j, val in enumerate(line):
            if val != ".":
                if val not in antenni:
                    antenni[val] = []
                antenni[val].append(((i, j)))

    antodes = set()
    harmonics = set()
    for key, ant in antenni.items():
        for i, first in enumerate(ant):
            for j, second in enumerate(ant[:i]):
                delta_i = first[0] - second[0]
                delta_j = first[1] - second[1]

                antode_one_i = first[0]
                antode_one_j = first[1]
                while 0 <= antode_one_i < i_size and 0 <= antode_one_j < j_size:
                    harmonics.add(((antode_one_i, antode_one_j)))
                    antode_one_i += delta_i
                    antode_one_j += delta_j

                antode_two_i = second[0]
                antode_two_j = second[1]
                while 0 <= antode_two_i < i_size and 0 <= antode_two_j < j_size:
                    harmonics.add(((antode_two_i, antode_two_j)))
                    antode_two_i -= delta_i
                    antode_two_j -= delta_j

                if (
                    0 <= first[0] + delta_i < i_size
                    and 0 <= first[1] + delta_j < j_size
                ):
                    antodes.add(((first[0] + delta_i, first[1] + delta_j)))
                if (
                    0 <= second[0] - delta_i < i_size
                    and 0 <= second[1] - delta_j < j_size
                ):
                    antodes.add(((second[0] - delta_i, second[1] - delta_j)))

    print(f"Part 1: {len(antodes)}")
    print(f"Part 2: {len(harmonics)}")


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].strip()
    return inputs_raw


part1(file_reader("08_input.txt"))
