def part1(programs: list[list[str]]) -> int:
    left_set = set()
    right_set = set()
    for prog in programs:
        left_set.add(prog[0])
        for child in prog[3:]:
            right_set.add(child)

    for value in left_set:
        if not value in right_set:
            return value


def find_oddity(values: list[int]) -> int:
    print(values)
    first = values[0]
    second = values[1]
    for pointer in range(2, len(values)):
        if values[pointer] != first:
            if values[pointer] != second:
                return pointer
            else:
                return 0
        else:
            if values[pointer] != second:
                return 1
    return -1


def inbalance(p_weights, p_children, point) -> int:
    if not point in p_children:
        return p_weights[point]

    values = []
    for child in p_children[point]:
        values.append(inbalance(p_weights, p_children, child))
        if values[-1] == -1:
            return -1

    if len(values) > 2:
        odd_one = find_oddity(values)

        if odd_one > -1:
            odd_one_weight = p_weights[p_children[point][odd_one]]
            odd_one_total = values[odd_one]
            if odd_one > 0:
                odd_one_target = values[0]
            else:
                odd_one_target = values[1]
            print(f"Part 2: {odd_one_weight + (odd_one_target - odd_one_total)}")
            return -1

    return sum(values) + p_weights[point]


def part2(programs: list[list[str]], root) -> None:
    program_weights = {}
    program_children = {}
    for prog in programs:
        program_weights[prog[0]] = int(prog[1][1:-1])
        if len(prog) > 2:
            program_children[prog[0]] = prog[3:]

    return inbalance(program_weights, program_children, root)


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "").replace(",", "").split()
    return inputs_raw


# print(file_reader('07_input.txt'))
part1_value = part1(file_reader("07_input.txt"))
print(f"Part 1: {part1_value}")
part2(file_reader("07_input.txt"), part1_value)
