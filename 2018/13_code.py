DIRECTIONS = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}


def print_track(trains, track_map):
    t_set = set(trains)
    for i in range(len(track_map)):
        a_line = ""
        for j in range(len(track_map[i])):
            if (i, j) in t_set:
                a_line += "G"
            else:
                a_line += track_map[i][j]
        print(a_line)


def make_train_track(train_snapshot: list[str]) -> list[list]:
    trains = []
    train_facts = []
    track_map = []

    for i, line in enumerate(train_snapshot):
        track_map.append([])
        for j, char in enumerate(line):
            match char:
                case "^":
                    trains.append(((i, j)))
                    train_facts.append(((0, 0)))
                    track_map[-1].append("|")
                case "v":
                    trains.append(((i, j)))
                    train_facts.append(((2, 0)))
                    track_map[-1].append("|")
                case ">":
                    trains.append(((i, j)))
                    train_facts.append(((1, 0)))
                    track_map[-1].append("-")
                case "<":
                    trains.append(((i, j)))
                    train_facts.append(((3, 0)))
                    track_map[-1].append("-")
                case _:
                    track_map[-1].append(char)

    return [trains, train_facts, track_map]


def compute_new_direction(track: str, direction: int, turn_count: int) -> tuple[int]:
    match track:
        case "+":
            match turn_count:
                case 0:
                    direction = (direction - 1) % 4
                case 2:
                    direction = (direction + 1) % 4
            turn_count = (turn_count + 1) % 3
        case "/":
            match direction:
                case 0:
                    direction = 1
                case 1:
                    direction = 0
                case 2:
                    direction = 3
                case 3:
                    direction = 2
        case "\\":
            match direction:
                case 0:
                    direction = 3
                case 1:
                    direction = 2
                case 2:
                    direction = 1
                case 3:
                    direction = 0

    return (direction, turn_count)


def part1(train_track_info: list[list]) -> tuple[int]:
    trains = train_track_info[0]
    train_facts = train_track_info[1]
    track_map = train_track_info[2]

    while True:
        train_check = set()
        new_trains = []
        new_train_facts = []

        while len(trains) > 0:
            ct_i, ct_j = trains.pop()
            direction, turn_count = train_facts.pop()

            ct_i += DIRECTIONS[direction][0]
            ct_j += DIRECTIONS[direction][1]

            new_train_loc = (ct_i, ct_j)
            if new_train_loc in train_check:
                # oops, used (y, x) coordinates
                return (ct_j, ct_i)
            train_check.add(new_train_loc)
            new_trains.append(new_train_loc)

            track = track_map[ct_i][ct_j]

            new_train_facts.append(compute_new_direction(track, direction, turn_count))

        trains = new_trains
        train_facts = new_train_facts


def part2(train_track_info: list[list]) -> tuple[int]:
    trains = []
    for i in range(len(train_track_info[0])):
        trains.append(
            [
                train_track_info[0][i][0],
                train_track_info[0][i][1],
                train_track_info[1][i][0],
                train_track_info[1][i][1],
            ]
        )
    track_map = train_track_info[2]

    while True:
        trains.sort(key=lambda x: (x[0], x[1]))
        # sort trains to handle them
        i = 0
        while i < len(trains):
            ct_i = trains[i][0]
            ct_j = trains[i][1]
            direction = trains[i][2]
            turn_count = trains[i][3]

            ct_i += DIRECTIONS[direction][0]
            ct_j += DIRECTIONS[direction][1]

            for j in range(len(trains)):
                match = False
                if ct_i == trains[j][0] and ct_j == trains[j][1]:
                    match = True
                    if i < j:
                        del trains[j]
                        del trains[i]
                    else:
                        del trains[i]
                        del trains[j]
                        i -= 1
                    break

            if match:
                continue
            trains[i][0] = ct_i
            trains[i][1] = ct_j
            trains[i][2], trains[i][3] = compute_new_direction(
                track=track_map[ct_i][ct_j],
                direction=direction,
                turn_count=turn_count,
            )
            i += 1

        if len(trains) == 1:
            return (trains[0][1], trains[0][0])


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "")
    return inputs_raw


train_data_separated = make_train_track(file_reader("13_input.txt"))
print(f"Part 1: {part1(train_data_separated)}")
train_data_separated = make_train_track(file_reader("13_input.txt"))
print(f"Part 2: {part2(train_data_separated)}")
