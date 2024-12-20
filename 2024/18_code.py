from collections import deque

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def part1(corruptions: list[str], time_elapsed: int) -> int:

    memory_map = []
    score_map = []
    for _ in range(71):
        memory_map.append(["."] * 71)
        score_map.append([-1] * 71)

    for i in range(time_elapsed):
        x, y = corruptions[i].split(",")
        x = int(x)
        y = int(y)

        memory_map[x][y] = "X"

    memory_map[0][0] = "S"
    memory_map[70][70] = "E"
    score_map[0][0] = 0

    to_visit = deque()
    to_visit.append(((0, 0)))

    while len(to_visit) > 0:
        last_i, last_j = to_visit.popleft()

        for arrow in DIRECTIONS:
            next_i = last_i + arrow[0]
            next_j = last_j + arrow[1]

            if (
                0 <= next_i < 71
                and 0 <= next_j < 71
                and (
                    memory_map[next_i][next_j] == "."
                    or memory_map[next_i][next_j] == "E"
                )
            ):
                next_score = score_map[last_i][last_j] + 1
                if (
                    score_map[next_i][next_j] == -1
                    or next_score < score_map[next_i][next_j]
                ):
                    score_map[next_i][next_j] = next_score
                    to_visit.append(((next_i, next_j)))

    return score_map[70][70]


def part2(corruptions: list[str]) -> tuple:
    low = 1024
    high = len(corruptions) - 1

    while low < high:
        mid = (high + low) // 2
        if part1(corruptions, mid) == -1:
            high = mid - 1
        else:
            low = mid + 1

    print(part1(corruptions, low))
    print(part1(corruptions, low + 1))
    return corruptions[low].split(",")


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].strip()
    return inputs_raw


raw_input = file_reader("18_input.txt")
print(f"Part 1: {part1(raw_input, 1024)}")
print(f"Part 2: {part2(raw_input)}")
