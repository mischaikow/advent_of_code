def part1(claw_machines: list[str], is_part_1: bool):

    adder = 0 if is_part_1 else 10_000_000_000_000
    ans = 0

    pointer = 0
    while pointer < len(claw_machines):
        a = int(claw_machines[pointer][12:14])
        b = int(claw_machines[pointer + 1][12:14])
        c = int(claw_machines[pointer][18:])
        d = int(claw_machines[pointer + 1][18:])

        prize_info = claw_machines[pointer + 2].split()
        x_final = int(prize_info[1][2:-1]) + adder
        y_final = int(prize_info[2][2:]) + adder

        # (x movement, y movement)
        # A buttons = final
        # A^-1 A buttons = A^-1 final
        # buttons = A^-1 final
        det_A = a * d - b * c
        press_count_button_a = (d * x_final - b * y_final) / det_A
        press_count_button_b = (-1 * c * x_final + a * y_final) / det_A

        if press_count_button_a.is_integer() and press_count_button_b.is_integer():
            ans += 3 * int(press_count_button_a) + int(press_count_button_b)

        pointer += 4

    print(f"Part {1 if is_part_1 else 2}: {ans}")


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].strip()
    return inputs_raw


part1(file_reader("13_input.txt"), True)
part1(file_reader("13_input.txt"), False)
