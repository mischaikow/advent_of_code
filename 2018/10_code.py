def part1(raw_light_data: list[str]) -> None:
    light_spots = []
    light_speeds = []

    for a_light in raw_light_data:
        light_x = int(a_light[10:16].strip())
        light_y = int(a_light[17:24].strip())
        light_dx = int(a_light[36:38].strip())
        light_dy = int(a_light[39:42].strip())

        light_spots.append([light_x, light_y])
        light_speeds.append([light_dx, light_dy])

    print_light_spots = [x.copy() for x in light_spots]

    steps = 9_900
    for i in range(len(light_spots)):
        light_spots[i][0] += steps * light_speeds[i][0]
        light_spots[i][1] += steps * light_speeds[i][1]

    minimum = 1_000 * 1_000
    for j in range(500):
        low_x = 1_000
        high_x = -1_000
        low_y = 1_000
        high_y = -1_000

        for i in range(len(light_spots)):
            light_spots[i][0] += light_speeds[i][0]
            light_spots[i][1] += light_speeds[i][1]

            low_x = min(light_spots[i][0], low_x)
            high_x = max(light_spots[i][0], high_x)
            low_y = min(light_spots[i][1], low_y)
            high_y = max(light_spots[i][1], high_y)

        box_size = (high_x - low_x) * (high_y - low_y)
        if box_size < minimum:
            minimum = box_size
            small_j = j + steps
            x_y_coords = [high_x, low_x, high_y, low_y]

    small_j += 1

    to_print = [
        [" "] * (1 + x_y_coords[0] - x_y_coords[1])
        for _ in range(1 + x_y_coords[2] - x_y_coords[3])
    ]

    for i in range(len(light_spots)):
        print_light_spots[i][0] += small_j * light_speeds[i][0]
        print_light_spots[i][1] += small_j * light_speeds[i][1]

        to_print[print_light_spots[i][1] - x_y_coords[3]][
            print_light_spots[i][0] - x_y_coords[1]
        ] = "X"

    print(small_j)
    for line in to_print:
        print("".join(line))

    return


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "")
    return inputs_raw


light_data_raw = file_reader("10_input.txt")
part1(light_data_raw)
