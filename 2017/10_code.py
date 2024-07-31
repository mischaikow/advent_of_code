def list_flip(a_list, start, length) -> None:
    for loc in range(length // 2):
        (
            a_list[(start + loc) % len(a_list)],
            a_list[(start + length - 1 - loc) % len(a_list)],
        ) = (
            a_list[(start + length - 1 - loc) % len(a_list)],
            a_list[(start + loc) % len(a_list)],
        )


def part1(raw_string: str) -> None:
    numbers = raw_string.split(",")
    input_lengths = [int(x) for x in numbers]
    circle = [x for x in range(256)]
    counter = 0
    pointer = 0

    for length in input_lengths:
        list_flip(circle, pointer, length)
        pointer += length + counter
        counter += 1

    print(f"Part 1: {circle[0] * circle[1]}")


def part2(raw_string: str) -> None:
    input_lengths = []
    for character in raw_string:
        input_lengths.append(ord(character))
    input_lengths += [17, 31, 73, 47, 23]

    circle = [x for x in range(256)]
    counter = 0
    pointer = 0

    for _ in range(64):
        for length in input_lengths:
            list_flip(circle, pointer, length)
            pointer = (pointer + length + counter) % len(circle)
            counter += 1

    # shrink the circle
    hex_string = ""
    for i in range(16):
        n = 0
        for j in range(16):
            n ^= circle[16 * i + j]
        n_hex = hex(n)[2:]
        if len(n_hex) == 1:
            n_hex = "0" + n_hex
        hex_string += n_hex

    print(f"Part 2: {hex_string}")


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "")
    return inputs_raw[0]


part1(file_reader("10_input.txt"))
part2(file_reader("10_input.txt"))
