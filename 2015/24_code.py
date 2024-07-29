
def list_product(values: list[int]) -> int:
    ans = 1
    for value in values:
        ans *= value
    return ans


def remainder_split(possibility, packages, target):
    left_side_group = [[]]
    for ap in packages:
        if ap in possibility:
            continue
        new_additions = []
        for group in left_side_group:
            new_group = group.copy()
            new_group.append(ap)
            if sum(new_group) < target:
                new_additions.append(new_group)
            if sum(new_group) == target:
                return True
        left_side_group += new_additions
    return False
    


def part1(packages: list[int]) -> None:
    total = sum(packages)
    container_weight = total // 3
    packages.sort(reverse=True)
    front_seat_group = [[]]
    final_group = []
    too_long = total
    shortest_answer = total
    for ap in packages:
        new_additions = []
        for group in front_seat_group:
            new_group = group.copy()
            new_group.append(ap)
            if len(new_group) > too_long:
                continue
            if sum(new_group) < container_weight:
                new_additions.append(new_group)
            if sum(new_group) == container_weight:
                if len(final_group) == 0:
                    too_long = len(new_group)
                if shortest_answer > len(new_group):
                    shortest_answer = len(new_group)
                final_group.append(new_group)
        front_seat_group += new_additions

    qe = total ** packages[0]
    for possibility in final_group:
        if len(possibility) == shortest_answer and remainder_split(possibility, packages, container_weight):
            qe = min(qe, list_product(possibility))

    print(f'Part 1: {qe}')


def remainder_three_split(possibility, packages, target):
    right_side_group = [[]]
    for ap in packages:
        if ap in possibility:
            continue
        new_additions = []
        for group in right_side_group:
            new_group = group.copy()
            new_group.append(ap)
            if sum(new_group) < target:
                new_additions.append(new_group)
            if sum(new_group) == target:
                if remainder_split(possibility + new_group, packages, target):
                    return True
        right_side_group += new_additions
    return False



def part2(packages: list[int]) -> None:
    total = sum(packages)
    container_weight = total // 4
    packages.sort(reverse=True)
    front_seat_group = [[]]
    final_group = []
    too_long = total
    shortest_answer = total

    for ap in packages:
        new_additions = []
        for group in front_seat_group:
            new_group = group.copy()
            new_group.append(ap)
            if len(new_group) > too_long:
                continue
            if sum(new_group) < container_weight:
                new_additions.append(new_group)
            if sum(new_group) == container_weight:
                if len(final_group) == 0:
                    too_long = len(new_group)
                if shortest_answer > len(new_group):
                    shortest_answer = len(new_group)
                final_group.append(new_group)
        front_seat_group += new_additions

    qe = total ** packages[0]
    for possibility in final_group:
        if len(possibility) == shortest_answer and remainder_three_split(possibility, packages, container_weight):
            qe = min(qe, list_product(possibility))

    print(f'Part 2: {qe}')


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = int(inputs_raw[i].replace("\n", ""))
    return inputs_raw


## print(file_reader("24_input.txt"))
part1(file_reader('24_input.txt'))
part2(file_reader('24_input.txt'))
