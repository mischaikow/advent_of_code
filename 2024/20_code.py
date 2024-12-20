from collections import deque

TIME = 100
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def part1(racecourse: list[str]) -> None:

    candidate_spots = []
    for i in range(1, len(racecourse) - 1):
        for j in range(1, len(racecourse[0]) - 1):
            if racecourse[i][j] == "#":
                right = racecourse[i + DIRECTIONS[0][0]][j + DIRECTIONS[0][1]]
                down = racecourse[i + DIRECTIONS[1][0]][j + DIRECTIONS[1][1]]
                left = racecourse[i + DIRECTIONS[2][0]][j + DIRECTIONS[2][1]]
                up = racecourse[i + DIRECTIONS[3][0]][j + DIRECTIONS[3][1]]
                if (right in (".", "E") and left in (".", "E")) or (
                    up in (".", "E") and down in (".", "E")
                ):
                    candidate_spots.append(((i, j)))

    legal_time = run_race(racecourse)

    ans = 0
    for i, spot in enumerate(candidate_spots):
        if i % 100 == 0:
            print(f"{i} / {len(candidate_spots)}")
        quickcourse = [list(x) for x in racecourse.copy()]
        quickcourse[spot[0]][spot[1]] = "."
        if run_race(quickcourse) <= legal_time - TIME:
            ans += 1

    print(f"Part 1: {ans}")


def run_race(racecourse: list[str]) -> int:
    times = []
    for _ in racecourse:
        times.append([-1] * len(racecourse[0]))

    to_visit = deque()
    for i, line in enumerate(racecourse):
        for j, val in enumerate(line):
            if val == "S":
                to_visit.append(((i, j)))
            if val == "E":
                the_end = (i, j)

    times[to_visit[0][0]][to_visit[0][1]] = 0

    while len(to_visit) > 0:
        tile_i, tile_j = to_visit.popleft()
        current_time = times[tile_i][tile_j]

        for d in DIRECTIONS:
            new_i = tile_i + d[0]
            new_j = tile_j + d[1]
            if racecourse[new_i][new_j] == "." or racecourse[new_i][new_j] == "E":
                if times[new_i][new_j] == -1 or current_time + 1 < times[new_i][new_j]:
                    times[new_i][new_j] = current_time + 1
                    if racecourse[new_i][new_j] == ".":
                        to_visit.append(((new_i, new_j)))

    return times[the_end[0]][the_end[1]]


def part2(racecourse: list[str]) -> int:
    times = []
    for _ in racecourse:
        times.append([-1] * len(racecourse[0]))

    to_visit = deque()
    for i, line in enumerate(racecourse):
        for j, val in enumerate(line):
            if val == "S":
                to_visit.append(((i, j)))
            if val == "E":
                the_end = (i, j)

    times[to_visit[0][0]][to_visit[0][1]] = 0

    while len(to_visit) > 0:
        tile_i, tile_j = to_visit.popleft()
        current_time = times[tile_i][tile_j]

        for d in DIRECTIONS:
            new_i = tile_i + d[0]
            new_j = tile_j + d[1]
            if racecourse[new_i][new_j] == "." or racecourse[new_i][new_j] == "E":
                if times[new_i][new_j] == -1 or current_time + 1 < times[new_i][new_j]:
                    times[new_i][new_j] = current_time + 1
                    if racecourse[new_i][new_j] == ".":
                        to_visit.append(((new_i, new_j)))

    ans = set()
    for i in range(1, len(racecourse) - 1):
        for j in range(1, len(racecourse[0]) - 1):
            if racecourse[i][j] == "." or racecourse[i][j] == "E":
                for radii in range(21):
                    for ii in range(radii + 1):
                        jj = radii - ii
                        if 0 <= i + ii < len(racecourse) and 0 <= j + jj < len(
                            racecourse[0]
                        ):
                            if racecourse[i + ii][j + jj] in (".", "S"):
                                if times[i][j] - times[i + ii][j + jj] >= TIME + radii:
                                    ans.add(((i, j, i + ii, j + jj)))

                        if 0 <= i + ii < len(racecourse) and 0 <= j - jj < len(
                            racecourse[0]
                        ):
                            if racecourse[i + ii][j - jj] in (".", "S"):
                                if times[i][j] - times[i + ii][j - jj] >= TIME + radii:
                                    ans.add(((i, j, i + ii, j - jj)))

                        if 0 <= i - ii < len(racecourse) and 0 <= j + jj < len(
                            racecourse[0]
                        ):
                            if racecourse[i - ii][j + jj] in (".", "S"):
                                if times[i][j] - times[i - ii][j + jj] >= TIME + radii:
                                    ans.add(((i, j, i - ii, j + jj)))

                        if 0 <= i - ii < len(racecourse) and 0 <= j - jj < len(
                            racecourse[0]
                        ):
                            if racecourse[i - ii][j - jj] in (".", "S"):
                                if times[i][j] - times[i - ii][j - jj] >= TIME + radii:
                                    ans.add(((i, j, i - ii, j - jj)))

    print(f"Part 2: {len(ans)}")


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].strip()
    return inputs_raw


part1(file_reader("20_input.txt"))
part2(file_reader("20_input.txt"))
