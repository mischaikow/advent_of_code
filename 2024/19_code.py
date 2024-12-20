def part1(towels_raw: list[str]) -> None:

    towel_patterns = set(towels_raw[0].split(", "))
    max_towel = 0
    for x in towel_patterns:
        max_towel = max(max_towel, len(x))

    part1_ans = 0
    part2_ans = 0

    for towel in towels_raw[2:]:
        towels_seen = dict()
        for i in range(len(towel) - 1, -1, -1):
            towels_seen[towel[i:]] = 0
            for j in range(max_towel + 1):
                if len(towel[i:]) == j:
                    if towel[i:] in towel_patterns:
                        towels_seen[towel[i:]] += 1
                    break

                elif towel[i : i + j] in towel_patterns:
                    towels_seen[towel[i:]] += towels_seen[towel[i + j :]]

        part1_ans += 1 if towels_seen[towel] > 0 else 0
        part2_ans += towels_seen[towel]

    print(f"Part 1: {part1_ans}")
    print(f"Part 2: {part2_ans}")


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].strip()
    return inputs_raw


part1(file_reader("19_input.txt"))
