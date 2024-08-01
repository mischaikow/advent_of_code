def part1(scanner_info: list[list[str]]) -> None:
    scanners = dict()
    for a_scan in scanner_info:
        scanners[int(a_scan[0])] = int(a_scan[1])

    ans = 0
    for time, range in scanners.items():
        if time % ((range - 1) * 2) == 0:
            ans += time * range

    print(f"Part 1: {ans}")

    delay = 0
    caught = True
    while caught:
        caught = False
        delay += 1
        for time, range in scanners.items():
            if (time + delay) % ((range - 1) * 2) == 0:
                caught = True
                break

    print(f"Part 2: {delay}")


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "").split(": ")
    return inputs_raw


part1(file_reader("13_input.txt"))
