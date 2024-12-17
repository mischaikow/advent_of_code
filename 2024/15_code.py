from collections import defaultdict, deque


DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
INSTRUCTION_MAP = {
    ">": DIRECTIONS[0],
    "v": DIRECTIONS[1],
    "^": DIRECTIONS[2],
    "<": DIRECTIONS[3],
}


def part1(full_map: list[str]):

    pointer = 0

    live_map = []
    while full_map[pointer] != "":
        live_map.append(list(full_map[pointer]))
        pointer += 1

    pointer += 1

    instructions = ""
    while pointer < len(full_map):
        instructions += full_map[pointer]
        pointer += 1

    # find the robot
    for i in range(len(live_map)):
        for j in range(len(live_map[i])):
            if live_map[i][j] == "@":
                live_map[i][j] = "."
                robot = (i, j)
                break

    # move the robot
    for instruct in instructions:
        robot_direction = INSTRUCTION_MAP[instruct]
        new_x = robot[0] + robot_direction[0]
        new_y = robot[1] + robot_direction[1]

        if live_map[new_x][new_y] == ".":
            robot = (new_x, new_y)
        elif live_map[new_x][new_y] == "O":
            o_x = new_x
            o_y = new_y
            while live_map[o_x][o_y] == "O":
                o_x += robot_direction[0]
                o_y += robot_direction[1]

            if live_map[o_x][o_y] == ".":
                live_map[o_x][o_y] = "O"
                live_map[new_x][new_y] = "."
                robot = (new_x, new_y)

    # sum the blocks
    ans = 0
    for x, line in enumerate(live_map):
        for y, val in enumerate(line):
            if val == "O":
                ans += 100 * x + y
    print(f"Part 1: {ans}")


MAPPINGS = {"#": ["#", "#"], "O": ["[", "]"], ".": [".", "."], "@": ["@", "."]}


def part2(full_map: list[str]):

    pointer = 0

    live_map = []
    while full_map[pointer] != "":
        live_map.append([])
        for val in full_map[pointer]:
            live_map[-1] += MAPPINGS[val]
        pointer += 1
    pointer += 1

    instructions = ""
    while pointer < len(full_map):
        instructions += full_map[pointer]
        pointer += 1

    # find the robot
    for i in range(len(live_map)):
        for j in range(len(live_map[i])):
            if live_map[i][j] == "@":
                live_map[i][j] = "."
                robot = (i, j)
                break

    # move the robot
    for instruct in instructions:

        robot_direction = INSTRUCTION_MAP[instruct]
        new_x = robot[0] + robot_direction[0]
        new_y = robot[1] + robot_direction[1]

        if live_map[new_x][new_y] == ".":
            robot = (new_x, new_y)

        elif robot_direction[0] == 0 and (
            live_map[new_x][new_y] == "[" or live_map[new_x][new_y] == "]"
        ):
            o_y = new_y
            while live_map[new_x][o_y] == "[" or live_map[new_x][o_y] == "]":
                o_y += robot_direction[1]

            if live_map[new_x][o_y] == ".":
                while (
                    live_map[new_x][o_y - robot_direction[1]] == "["
                    or live_map[new_x][o_y - robot_direction[1]] == "]"
                ):
                    live_map[new_x][o_y] = live_map[new_x][o_y - robot_direction[1]]
                    o_y -= robot_direction[1]
                    live_map[new_x][o_y] = "."

                robot = (new_x, new_y)

        # going down or up, we see [ or ]
        elif robot_direction[1] == 0 and (
            live_map[new_x][new_y] == "[" or live_map[new_x][new_y] == "]"
        ):
            can_move = True
            to_move = defaultdict(set)
            children = deque()
            children.append(((robot[0], robot[1])))
            last_row = robot[0]
            while len(children) > 0:
                curr_x, curr_y = children.popleft()
                next_x = curr_x + robot_direction[0]

                if live_map[next_x][curr_y] == "[":
                    children.append(((next_x, curr_y)))
                    to_move[next_x].add(curr_y)
                    children.append(((next_x, curr_y + 1)))
                    to_move[next_x].add(curr_y + 1)
                    last_row = next_x
                elif live_map[next_x][curr_y] == "]":
                    children.append(((next_x, curr_y)))
                    to_move[next_x].add(curr_y)
                    children.append(((next_x, curr_y - 1)))
                    to_move[next_x].add(curr_y - 1)
                    last_row = next_x
                elif live_map[next_x][curr_y] == "#":
                    can_move = False
                    break

            if can_move:
                while last_row != robot[0]:
                    for col in to_move[last_row]:
                        live_map[last_row + robot_direction[0]][col] = live_map[
                            last_row
                        ][col]
                        live_map[last_row][col] = "."
                    last_row -= robot_direction[0]

                robot = (new_x, new_y)

    # sum the blocks
    ans = 0
    for x, line in enumerate(live_map):
        for y, val in enumerate(line):
            if val == "[":
                ans += 100 * x + y
    print(f"Part 2: {ans}")


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].strip()
    return inputs_raw


part1(file_reader("15_input.txt"))
part2(file_reader("15_input.txt"))
