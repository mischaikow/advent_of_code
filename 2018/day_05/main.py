from string import ascii_lowercase as alc


def part1(polymer: str) -> int:
    length_temp = 0
    while length_temp != len(polymer):
        new_polymer = ""
        length_temp = len(polymer)
        i = 0
        while i < len(polymer) - 1:
            if polymer[i] != polymer[i + 1] and (
                polymer[i] == polymer[i + 1].upper()
                or polymer[i] == polymer[i + 1].lower()
            ):
                i += 1
            else:
                new_polymer += polymer[i]
            i += 1

        if i == len(polymer) - 1:
            new_polymer += polymer[i]

        polymer = new_polymer

    return len(polymer)


def part2(polymer: str) -> None:
    shortest_polymer = len(polymer)
    for alpha_char in alc:
        new_poly = ""
        for p_char in polymer:
            if p_char.lower() != alpha_char:
                new_poly += p_char
        shortest_polymer = min(shortest_polymer, part1(new_poly))

    print(f"Part 2: {shortest_polymer}")


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "")
    return inputs_raw[0]


ans = part1(file_reader("input.txt"))
print(f"Part 1: {ans}")
part2(file_reader("input.txt"))
