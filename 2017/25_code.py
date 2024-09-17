def part1(ports_raw: list[str]) -> int:
    pointer = 0
    state = "A"
    values = set()

    for _ in range(12_261_543):
        match state:
            case "A":
                if pointer in values:
                    values.remove(pointer)
                    pointer -= 1
                    state = "C"
                else:
                    values.add(pointer)
                    pointer += 1
                    state = "B"
            case "B":
                if pointer in values:
                    pointer += 1
                    state = "C"
                else:
                    values.add(pointer)
                    pointer -= 1
                    state = "A"
            case "C":
                if pointer in values:
                    values.remove(pointer)
                    pointer -= 1
                    state = "D"
                else:
                    values.add(pointer)
                    pointer += 1
                    state = "A"
            case "D":
                if pointer in values:
                    pointer -= 1
                    state = "C"
                else:
                    values.add(pointer)
                    pointer -= 1
                    state = "E"
            case "E":
                if pointer in values:
                    pointer += 1
                    state = "A"
                else:
                    values.add(pointer)
                    pointer += 1
                    state = "F"
            case "F":
                if pointer in values:
                    pointer += 1
                    state = "E"
                else:
                    values.add(pointer)
                    pointer += 1
                    state = "A"
            case _:
                print("uh oh")
                return

    return len(values)


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "")
    return inputs_raw


print(f"Part 1: {part1(file_reader('25_input.txt'))}")
