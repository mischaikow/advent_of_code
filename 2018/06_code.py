DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def part1(raw_coordinates: list[tuple[int]]) -> int:
    size = dict()
    to_visit = []
    space = dict()
    for i in range(len(raw_coordinates)):
        size[i] = 1
        to_visit.append(((i, raw_coordinates[i])))
        space[raw_coordinates[i]] = (0, i)

    distance = 0
    while distance < 1_000:
        next_round = []
        distance += 1
        while len(to_visit) > 0:
            coord, location = to_visit.pop()
            if location in space and space[location][0] == -1:
                continue

            for d in DIRECTIONS:
                new_location = (location[0] + d[0], location[1] + d[1])
                if new_location in space:
                    if (
                        space[new_location][0] == distance
                        and coord != space[new_location][1]
                    ):
                        size[space[new_location][1]] -= 1
                        space[new_location] = (-1, -1)
                else:
                    next_round.append(((coord, new_location)))
                    space[new_location] = (distance, space[location][1])
                    size[space[location][1]] += 1
        to_visit = next_round

    for coord, _ in to_visit:
        size.pop(coord, None)

    ans = [v for v in size.values()]
    return max(ans)


def part2(raw_coordinates: list[tuple[int]]) -> int:
    max_x = 0
    min_x = 1000
    max_y = 0
    min_y = 1000
    for c in raw_coordinates:
        max_x = max(c[0], max_x)
        min_x = min(c[0], min_x)
        max_y = max(c[1], max_y)
        min_y = min(c[1], min_y)

    def in_zone(raw_coordinates, i, j):
        total_distance = 0
        for c in raw_coordinates:
            total_distance += abs(i - c[0]) + abs(j - c[1])
        return total_distance < 10_000

    ans = 0
    max_distance = 10_000 // len(raw_coordinates)
    for i in range(min_x - max_distance, max_x + max_distance):
        for j in range(min_x - max_distance, max_x + max_distance):
            if in_zone(raw_coordinates, i, j):
                ans += 1

    return ans


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "").split(", ")
        inputs_raw[i] = (int(inputs_raw[i][0]), int(inputs_raw[i][1]))
    return inputs_raw


raw_coordinates = file_reader("06_input.txt")
print(f"Part 1: {part1(raw_coordinates=raw_coordinates)}")
print(f"Part 2: {part2(raw_coordinates=raw_coordinates)}")
