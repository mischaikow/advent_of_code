from collections import deque

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def part1(full_map: list[str]) -> None:

    score_map = []
    to_visit = deque()

    for i in range(len(full_map)):
        score_map.append([])
        for j, val in enumerate(full_map[i]):
            if val == "S":
                to_visit.append(((i, j)))
                score_map[-1].append([0, 1000, 1000, 1000])
            else:
                score_map[-1].append([-1, -1, -1, -1])

            if val == "E":
                final_goal = (i, j)

    while len(to_visit) > 0:
        last_i, last_j = to_visit.popleft()

        for d, arrow in enumerate(DIRECTIONS):
            next_i = last_i + arrow[0]
            next_j = last_j + arrow[1]

            if full_map[next_i][next_j] == "." or full_map[next_i][next_j] == "E":
                next_score = score_map[last_i][last_j][d] + 1
                for dd in range(4):
                    adjust = 0 if d == dd else 1000
                    if (
                        score_map[next_i][next_j][dd] == -1
                        or next_score + adjust < score_map[next_i][next_j][dd]
                    ):
                        score_map[next_i][next_j][dd] = next_score + adjust
                        to_visit.append(((next_i, next_j)))

    print(f"Part 1: {min(score_map[final_goal[0]][final_goal[1]])}")

    to_visit = deque()
    hot_list = set()
    visited = set()
    to_visit.append(((final_goal[0], final_goal[1], 0)))
    hot_list.add(final_goal)

    while len(to_visit) > 0:
        last_i, last_j, last_d = to_visit.popleft()

        for d, arrow in enumerate(DIRECTIONS):
            next_i = last_i + arrow[0]
            next_j = last_j + arrow[1]

            if full_map[next_i][next_j] == "S":
                hot_list.add(((next_i, next_j)))

            elif full_map[next_i][next_j] == "." and (next_i, next_j) not in visited:
                visited.add(((next_i, next_j)))

                opposite_direction = (d + 2) % 4

                if final_goal == (last_i, last_j) and score_map[next_i][next_j][
                    opposite_direction
                ] < min(score_map[last_i][last_j]):
                    to_visit.append(((next_i, next_j, opposite_direction)))
                    hot_list.add(((next_i, next_j)))

                elif final_goal != (last_i, last_j):
                    if (
                        opposite_direction == last_d
                        and score_map[next_i][next_j][opposite_direction]
                        < score_map[last_i][last_j][opposite_direction]
                    ):
                        to_visit.append(((next_i, next_j, opposite_direction)))
                        hot_list.add(((next_i, next_j)))

                    elif (
                        d != last_d
                        and score_map[next_i][next_j][opposite_direction]
                        < score_map[last_i][last_j][last_d] - 1000
                    ):
                        to_visit.append(((next_i, next_j, opposite_direction)))
                        hot_list.add(((next_i, next_j)))

    print(f"Part 2: {len(hot_list)}")


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].strip()
    return inputs_raw


part1(file_reader("16_input.txt"))
