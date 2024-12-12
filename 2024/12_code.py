DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def make_grid(full_map: list[str]):
    height = len(full_map)
    width = len(full_map[0])
    result = []
    for _ in range(height + 1):
        result.append([0] * (width + 1))
    return result


def part1(full_map: list[str]):

    visited = []
    for line in full_map:
        visited.append([0 for _ in line])

    ans = 0
    ans_2 = 0
    for i, line in enumerate(full_map):
        for j, val in enumerate(line):
            if visited[i][j] == 0:
                to_visit = [(i, j)]
                visited[i][j] = 1
                total_area = 1
                total_perimeter = 0

                up_down_fencing = make_grid(full_map)
                left_right_fencing = make_grid(full_map)

                while len(to_visit) > 0:
                    i_coord, j_coord = to_visit.pop()
                    for d in DIRECTIONS:
                        i_new = i_coord + d[0]
                        j_new = j_coord + d[1]

                        if (
                            0 <= i_new < len(full_map)
                            and 0 <= j_new < len(full_map[0])
                            and full_map[i_new][j_new] == val
                        ):

                            if visited[i_new][j_new] == 0:
                                to_visit.append(((i_new, j_new)))
                                visited[i_new][j_new] = 1
                                total_area += 1

                        else:
                            total_perimeter += 1
                            if i_new == i_coord:
                                if d[1] == -1:
                                    up_down_fencing[i_new][j_new] = 1
                                else:
                                    up_down_fencing[i_new][j_coord] = 1
                            else:
                                if d[0] == -1:
                                    left_right_fencing[i_new][j_new] = 1
                                else:
                                    left_right_fencing[i_coord][j_new] = 1

                fence_count = 0
                is_up_down_fence = False
                for j_fence in range(len(up_down_fencing[0])):
                    for i_fence in range(len(up_down_fencing)):
                        if (
                            up_down_fencing[i_fence][j_fence] == 1
                            and not is_up_down_fence
                        ):
                            fence_count += 1
                            is_up_down_fence = True
                        elif (
                            up_down_fencing[i_fence][j_fence] == 0 and is_up_down_fence
                        ):
                            is_up_down_fence = False
                        elif (
                            up_down_fencing[i_fence][j_fence] == 1
                            and is_up_down_fence
                            and left_right_fencing[i_fence - 1][j_fence] == 1
                            and left_right_fencing[i_fence - 1][j_fence + 1] == 1
                        ):
                            fence_count += 1

                is_left_right_fence = False
                for i_fence in range(len(left_right_fencing)):
                    for j_fence in range(len(left_right_fencing[0])):
                        if (
                            left_right_fencing[i_fence][j_fence] == 1
                            and not is_left_right_fence
                        ):
                            fence_count += 1
                            is_left_right_fence = True
                        elif (
                            left_right_fencing[i_fence][j_fence] == 0
                            and is_left_right_fence
                        ):
                            is_left_right_fence = False
                        elif (
                            left_right_fencing[i_fence][j_fence] == 1
                            and is_left_right_fence
                            and up_down_fencing[i_fence][j_fence - 1] == 1
                            and up_down_fencing[i_fence + 1][j_fence - 1] == 1
                        ):
                            fence_count += 1

                ans += total_area * total_perimeter
                ans_2 += total_area * fence_count

    print(f"Part 1: {ans}")
    print(f"Part 2: {ans_2}")


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].strip()
    return inputs_raw


part1(file_reader("12_input.txt"))
