def part1(first_row: str, room_length: int) -> int:
    room = [first_row]
    for _ in range(room_length - 1):
        new_line = ""
        for i in range(len(room[-1])):
            left = room[-1][i - 1] if i > 0 else "."
            center = room[-1][i]
            right = room[-1][i + 1] if i < len(room[-1]) - 1 else "."

            next_value = "."
            if (left == "^" and right == ".") or (left == "." and right == "^"):
                next_value = "^"

            new_line += next_value

        room.append(new_line)

    ans = 0
    for line in room:
        for a_char in line:
            if a_char == ".":
                ans += 1

    return ans


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "")
    return inputs_raw[0]


## print(file_reader("18_input.txt"))
print(f"Part 1: {part1(file_reader('18_input.txt'), 40)}")
print(f"Part 2: {part1(file_reader('18_input.txt'), 400_000)}")
