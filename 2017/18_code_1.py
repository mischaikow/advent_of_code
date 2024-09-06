def is_memory_register(a_str: str) -> bool:
    if a_str.isdigit():
        return False
    if a_str[0] == "-":
        return False
    return True


def find_value(memory: dict[int], v: str) -> int:
    if is_memory_register(v):
        return memory[v]
    return int(v)


def duet(memory: dict[int], instructions: list[str]) -> int:
    pointer = 0
    last_sound = -1

    while 0 <= pointer < len(instructions):
        this_line = instructions[pointer]
        match this_line[0]:
            case "snd":
                last_sound = memory[this_line[1]]
            case "set":
                memory[this_line[1]] = find_value(memory, this_line[2])
            case "add":
                memory[this_line[1]] += find_value(memory, this_line[2])
            case "mul":
                memory[this_line[1]] *= find_value(memory, this_line[2])
            case "mod":
                memory[this_line[1]] %= find_value(memory, this_line[2])
            case "rcv":
                if find_value(memory, this_line[1]) != 0:
                    return last_sound
            case "jgz":
                if find_value(memory, this_line[1]) > 0:
                    pointer += find_value(memory, this_line[2]) - 1
            case _:
                print(f"Fail state: {this_line[0]}")
                return -1

        pointer += 1

    print("Out of bounds")
    return -1


def part1(instructions_raw: list[str]) -> int:
    memory = {}
    for line in instructions_raw:
        if is_memory_register(line[1]) and line[1] not in memory:
            memory[line[1]] = 0
        if len(line) == 3 and is_memory_register(line[2]) and line[2] not in memory:
            memory[line[2]] = 0

    return duet(memory=memory, instructions=instructions_raw)


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "").split()
    return inputs_raw


print(f"Part 1: {part1(file_reader('18_input.txt'))}")
