def part1(wire_info: list[str]) -> None:
    knowns = dict()
    pointer = 0

    while wire_info[pointer] != "":
        wire, value = wire_info[pointer].split(": ")
        knowns[wire] = int(value) == 1
        pointer += 1
    digit_count = pointer // 2

    pointer += 1

    crosses = []
    while pointer < len(wire_info):
        crosses.append(wire_info[pointer].split())
        pointer += 1

    has_missing_knowns = True
    while has_missing_knowns:
        has_missing_knowns = False
        for cross in crosses:
            if cross[0] not in knowns or cross[2] not in knowns:
                has_missing_knowns = True
            else:
                knowns[cross[4]] = operation(
                    knowns[cross[0]], knowns[cross[2]], cross[1]
                )

    ans = 0
    for key, value in knowns.items():
        if key[0] == "z" and value:
            ans += 2 ** int(key[1:])
    print(f"Part 1: {ans}")

    # Manual debugging :)
    for cross in crosses:
        if cross[4] == "z12":
            cross[4] = "fgc"
        elif cross[4] == "fgc":
            cross[4] = "z12"

        elif cross[4] == "z29":
            cross[4] = "mtj"
        elif cross[4] == "mtj":
            cross[4] = "z29"

        elif cross[4] == "dtv":
            cross[4] = "z37"
        elif cross[4] == "z37":
            cross[4] = "dtv"

        elif cross[4] == "vvm":
            cross[4] = "dgr"
        elif cross[4] == "dgr":
            cross[4] = "vvm"

    # put them together:
    print(",".join(sorted(["z12", "fgc", "z29", "mtj", "z37", "dtv", "vvm", "dgr"])))
    print()

    ##  Map it all out and find some gaps:
    # First layer -
    and_layer_one = [""] * digit_count
    xor_layer_one = [""] * digit_count
    for cross in crosses:
        if (cross[0][0] == "x" or cross[0][0] == "y") and cross[1] == "AND":
            and_layer_one[int(cross[0][1:])] = cross[4]
        if (cross[0][0] == "x" or cross[0][0] == "y") and cross[1] == "XOR":
            xor_layer_one[int(cross[0][1:])] = cross[4]

    # Second layer -
    xor_set_one = set(xor_layer_one)
    and_layer_two = [""] * digit_count
    xor_layer_two = [""] * digit_count
    for cross in crosses:
        if cross[1] == "XOR":
            if cross[0] in xor_set_one:
                xor_layer_two[xor_layer_one.index(cross[0])] = cross[4]
            if cross[2] in xor_set_one:
                xor_layer_two[xor_layer_one.index(cross[2])] = cross[4]
        if cross[1] == "AND":
            if cross[0] in xor_set_one:
                and_layer_two[xor_layer_one.index(cross[0])] = cross[4]
            if cross[2] in xor_set_one:
                and_layer_two[xor_layer_one.index(cross[2])] = cross[4]

    # Or layer -
    and_set_one = set(and_layer_one)
    or_next_layer = [""] * (digit_count + 1)
    for cross in crosses:
        if cross[1] == "OR":
            if cross[0] in and_set_one:
                or_next_layer[and_layer_one.index(cross[0])] = cross[4]
            elif cross[2] in and_set_one:
                or_next_layer[and_layer_one.index(cross[2])] = cross[4]

    print("a1 , x1 , x2 , a2 , or")
    print("--   --   --   --   --")
    for i in range(digit_count):
        print(
            f"{and_layer_one[i]}, {xor_layer_one[i]}, {xor_layer_two[i]}, {and_layer_two[i]}, {or_next_layer[i]}"
        )


def operation(val_a, val_b, gate):
    if gate == "AND":
        return val_a and val_b
    elif gate == "OR":
        return val_a or val_b
    elif gate == "XOR":
        return val_a != val_b


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].strip()
    return inputs_raw


part1(file_reader("24_input.txt"))
