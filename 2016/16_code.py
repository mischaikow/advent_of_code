def part1(disk_size: int, starting_number: str) -> int:
    while len(starting_number) < disk_size:
        new_string = ""
        for a_char in reversed(starting_number):
            new_string += "0" if a_char == "1" else "1"
        starting_number += "0" + new_string

    full_disk = starting_number[:disk_size]

    while len(full_disk) % 2 == 0:
        new_string = ""
        for i in range(1, len(full_disk), 2):
            if full_disk[i] == full_disk[i - 1]:
                new_string += "1"
            else:
                new_string += "0"
        full_disk = new_string

    return full_disk


TEST_INPUT_1 = "110010110100"
DISK_INPUT_1 = 12
TEST_INPUT_2 = "10000"
DISK_INPUT_2 = 20

ACTUAL_INPUT = "10111100110001111"
ACTUAL_DISK = 272
ACTUAL_DISK_2 = 35651584
## print(file_reader("15_input.txt"))
print(f"Part 1: {part1(ACTUAL_DISK, ACTUAL_INPUT)}")
print(f"Part 2: {part1(ACTUAL_DISK_2, ACTUAL_INPUT)}")
## print(f"Part 2: {part2(file_reader('15_input.txt'))}")
