DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def part1(original_map: list[str]) -> None:
    guard_location, guard_direction = find_guard(original_map)

    visited = set()
    obstructions = set()
    while True:
        visited.add(guard_location)

        next_location_i = guard_location[0] + DIRECTIONS[guard_direction][0]
        next_location_j = guard_location[1] + DIRECTIONS[guard_direction][1]

        if 0 <= next_location_i < len(original_map) and 0 <= next_location_j < len(
            original_map[0]
        ):
            if original_map[next_location_i][next_location_j] == "#":
                guard_direction = (guard_direction + 1) % 4
            else:
                obstructions.add(((next_location_i, next_location_j)))
                guard_location = (next_location_i, next_location_j)
        else:
            break

    print(f"Part 1: {len(visited)}")

    guard_location, guard_direction = find_guard(original_map)

    working_obstructions = set()
    for a in obstructions:
        working_obstructions.add(
            block_makes_loop(original_map, guard_location, guard_direction, a)
        )

    print(f"Part 2: {len(working_obstructions) - 1}")


def find_guard(original_map: list[str]) -> None:
    for i, line in enumerate(original_map):
        for j, c in enumerate(line):
            match c:
                case "^":
                    return (i, j), 3
                case ">":
                    return (i, j), 0
                case "v":
                    return (i, j), 1
                case "<":
                    return (i, j), 2


def block_makes_loop(original_map, check_location, check_direction, obstruction):
    new_hash_i, new_hash_j = obstruction

    visited = set()
    while (check_location[0], check_location[1], check_direction) not in visited:
        visited.add(((check_location[0], check_location[1], check_direction)))

        next_location_i = check_location[0] + DIRECTIONS[check_direction][0]
        next_location_j = check_location[1] + DIRECTIONS[check_direction][1]

        if 0 <= next_location_i < len(original_map) and 0 <= next_location_j < len(
            original_map[0]
        ):
            if (original_map[next_location_i][next_location_j] == "#") or (
                next_location_i == new_hash_i and next_location_j == new_hash_j
            ):
                check_direction = (check_direction + 1) % 4
            else:
                check_location = (next_location_i, next_location_j)
        else:
            return (-1, -1)

    return (new_hash_i, new_hash_j)


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].strip()
    return inputs_raw


part1(file_reader("06_input.txt"))
