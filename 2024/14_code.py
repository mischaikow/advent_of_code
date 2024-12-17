FULL_HEIGHT = 103
FULL_WIDTH = 101


def prod(vals: list[int]) -> int:
    ans = 1
    for v in vals:
        ans *= v
    return ans


def part1(robot_list_raw: list[str]) -> None:

    quads = [0, 0, 0, 0]
    for robot in robot_list_raw:
        pos, vel = robot.split()
        pos_x, pos_y = pos[2:].split(",")
        vel_x, vel_y = vel[2:].split(",")

        final_x = (int(pos_x) + 100 * int(vel_x)) % FULL_WIDTH
        final_y = (int(pos_y) + 100 * int(vel_y)) % FULL_HEIGHT

        if final_x < 50:
            if final_y < 51:
                quads[0] += 1
            elif final_y > 51:
                quads[1] += 1
        elif final_x > 50:
            if final_y < 51:
                quads[2] += 1
            elif final_y > 51:
                quads[3] += 1

    print(f"Part 1: {prod(quads)}")


def print_board(robot_list: list[tuple[int]]):
    output = []
    for _ in range(FULL_HEIGHT):
        output.append([" "] * FULL_WIDTH)

    for robot in robot_list:
        output[robot[1]][robot[0]] = "X"

    for line in output:
        print("".join(line))


def part2(robot_list_raw: list[str]) -> None:

    robot_list = []
    for robot in robot_list_raw:
        pos, vel = robot.split()
        pos_x, pos_y = pos[2:].split(",")
        vel_x, vel_y = vel[2:].split(",")

        robot_list.append(((int(pos_x), int(pos_y), int(vel_x), int(vel_y))))

    print(robot_list)

    second_counter = 0
    # found this by recognizing there were patters of mod 101 and 103 that started at second 4 and 76
    # extended the pattern, and found 6771 was when they converged.
    while second_counter < 6771:
        new_robot_list = []
        for robot in robot_list:
            new_robot_list.append(
                (
                    (
                        (robot[0] + robot[2]) % FULL_WIDTH,
                        (robot[1] + robot[3]) % FULL_HEIGHT,
                        robot[2],
                        robot[3],
                    )
                )
            )
        robot_list = new_robot_list
        second_counter += 1

    print_board(robot_list)


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].strip()
    return inputs_raw


part1(file_reader("14_input.txt"))
part2(file_reader("14_input.txt"))
