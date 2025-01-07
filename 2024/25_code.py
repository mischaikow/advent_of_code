def part1(schematics: list[str]) -> None:
    keys = []
    locks = []

    pointer = 0
    while pointer < len(schematics):
        hash_count = []

        for i in range(5):
            val = 0
            for j in range(7):
                if schematics[pointer + j][i] == "#":
                    val += 1
            hash_count.append(val)

        if schematics[pointer][0] == "#":
            locks.append(hash_count)

        else:
            keys.append(hash_count)

        pointer += 8

    ans = 0
    for k in keys:
        for l in locks:
            fits = True
            for i in range(5):
                if k[i] + l[i] > 7:
                    fits = False
                    break
            if fits:
                ans += 1

    print(f"Part 1: {ans}")


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].strip()
    return inputs_raw


part1(file_reader("25_input.txt"))
