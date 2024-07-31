MOVEMENT_EVEN = {
    "n": (0, 1),
    "s": (0, -1),
    "ne": (1, 1),
    "nw": (-1, 1),
    "se": (1, 0),
    "sw": (-1, 0),
}
MOVEMENT_ODD = {
    "n": (0, 1),
    "s": (0, -1),
    "ne": (1, 0),
    "nw": (-1, 0),
    "se": (1, -1),
    "sw": (-1, -1),
}


def measure_distance(location_input: list[int]) -> int:
    ans = 0
    location = location_input.copy()
    while location[0] != 0 or location[1] != 0:
        if location[0] < 0:
            if location[0] % 2 == 0:
                if location[1] < 0:
                    location[0] += MOVEMENT_EVEN["ne"][0]
                    location[1] += MOVEMENT_EVEN["ne"][1]
                else:
                    location[0] += MOVEMENT_EVEN["se"][0]
                    location[1] += MOVEMENT_EVEN["se"][1]
            else:
                if location[1] <= 0:
                    location[0] += MOVEMENT_ODD["ne"][0]
                    location[1] += MOVEMENT_ODD["ne"][1]
                else:
                    location[0] += MOVEMENT_ODD["se"][0]
                    location[1] += MOVEMENT_ODD["se"][1]

        elif location[0] > 0:
            if location[0] % 2 == 0:
                if location[1] < 0:
                    location[0] += MOVEMENT_EVEN["nw"][0]
                    location[1] += MOVEMENT_EVEN["nw"][1]
                else:
                    location[0] += MOVEMENT_EVEN["sw"][0]
                    location[1] += MOVEMENT_EVEN["sw"][1]
            else:
                if location[1] <= 0:
                    location[0] += MOVEMENT_ODD["nw"][0]
                    location[1] += MOVEMENT_ODD["nw"][1]
                else:
                    location[0] += MOVEMENT_ODD["sw"][0]
                    location[1] += MOVEMENT_ODD["sw"][1]
        elif location[1] < 0:
            location[1] += 1
        else:
            location[1] -= 1

        ans += 1
    return ans


def part1(instructions: str) -> None:
    location = [0, 0]
    ans_two = 0

    for step in instructions:
        if location[0] % 2 == 0:
            location[0] += MOVEMENT_EVEN[step][0]
            location[1] += MOVEMENT_EVEN[step][1]
        else:
            location[0] += MOVEMENT_ODD[step][0]
            location[1] += MOVEMENT_ODD[step][1]
        ans_two = max(ans_two, measure_distance(location))

    # Measure distance
    ans_one = measure_distance(location)

    print(f"Part 1: {ans_one}")
    print(f"Part 2: {ans_two}")


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "").split(",")
    return inputs_raw[0]


test_input1 = ["ne", "ne", "ne"]
test_input2 = ["ne", "ne", "sw", "sw"]
test_input3 = ["ne", "ne", "s", "s"]
test_input4 = ["se", "sw", "se", "sw", "sw"]

part1(file_reader("11_input.txt"))
part1(test_input1)
part1(test_input2)
part1(test_input3)
part1(test_input4)
# part2(file_reader("11_input.txt"))
