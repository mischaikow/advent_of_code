DIRECTIONS = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]


def part1(word_chart: list[str]):
    i_size = len(word_chart)
    j_size = len(word_chart[0])
    ans = 0

    for i in range(i_size):
        for j in range(j_size):
            if word_chart[i][j] == "X":
                for d in DIRECTIONS:
                    steps = 1
                    for counter in range(1, 4):
                        i_new = i + counter * d[0]
                        j_new = j + counter * d[1]
                        if (
                            i_new < 0
                            or i_new >= i_size
                            or j_new < 0
                            or j_new >= j_size
                            or word_chart[i_new][j_new] != "XMAS"[counter]
                        ):
                            break
                        steps += 1
                    if steps == 4:
                        ans += 1

    print(f"Part 1: {ans}")


def part2(word_chart: list[str]):
    i_size = len(word_chart)
    j_size = len(word_chart[0])
    dd = [(-1, 1), (1, -1), (1, 1), (-1, -1)]
    ans = 0

    for i in range(1, i_size - 1):
        for j in range(1, j_size - 1):
            if word_chart[i][j] == "A":
                ## What a beauty.
                if (
                    word_chart[i + dd[0][0]][j + dd[0][1]] == "M"
                    and word_chart[i + dd[1][0]][j + dd[1][1]] == "S"
                ):
                    if (
                        word_chart[i + dd[2][0]][j + dd[2][1]] == "M"
                        and word_chart[i + dd[3][0]][j + dd[3][1]] == "S"
                    ):
                        ans += 1
                    elif (
                        word_chart[i + dd[2][0]][j + dd[2][1]] == "S"
                        and word_chart[i + dd[3][0]][j + dd[3][1]] == "M"
                    ):
                        ans += 1
                elif (
                    word_chart[i + dd[0][0]][j + dd[0][1]] == "S"
                    and word_chart[i + dd[1][0]][j + dd[1][1]] == "M"
                ):
                    if (
                        word_chart[i + dd[2][0]][j + dd[2][1]] == "M"
                        and word_chart[i + dd[3][0]][j + dd[3][1]] == "S"
                    ):
                        ans += 1
                    elif (
                        word_chart[i + dd[2][0]][j + dd[2][1]] == "S"
                        and word_chart[i + dd[3][0]][j + dd[3][1]] == "M"
                    ):
                        ans += 1

    print(f"part 2: {ans}")


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    return inputs_raw


part1(file_reader("04_input.txt"))
part2(file_reader("04_input.txt"))
