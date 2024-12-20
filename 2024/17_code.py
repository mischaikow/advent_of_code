def part1(A: int, B: int, C: int, instructions: list[str]) -> None:

    def combo(pointer: int) -> int:
        value = instructions[pointer]
        if value == 7:
            raise ValueError("Attempted a combo value of 7")
        elif value == 6:
            return C
        elif value == 5:
            return B
        elif value == 4:
            return A
        return value

    def print_state(pointer):
        print(instructions)
        print(
            f"{pointer}: opcode {instructions[pointer]} with value {instructions[pointer + 1]}"
        )
        print(f"Register A: {A}")
        print(f"Register B: {B}")
        print(f"Register C: {C}")
        print()

    out = []

    pointer = 0
    while 0 <= pointer < len(instructions):
        # print_state(pointer)

        opcode = instructions[pointer]
        match opcode:
            case 0:
                A = A // (2 ** combo(pointer + 1))
            case 1:
                B ^= instructions[pointer + 1]
            case 2:
                B = combo(pointer + 1) % 8
            case 3:
                if A != 0:
                    pointer = instructions[pointer + 1]
                    continue
            case 4:
                B ^= C
            case 5:
                out.append(combo(pointer + 1) % 8)
            case 6:
                B = A // (2 ** combo(pointer + 1))
            case 7:
                C = A // (2 ** combo(pointer + 1))

        pointer += 2

    return ",".join([str(x) for x in out])


def part2(instructions) -> int:
    A_progress = [0]
    for instruct in reversed(instructions):
        new_progress = []
        while len(A_progress) > 0:
            A = A_progress.pop()
            A <<= 3
            for i in range(8):
                check_value = A + i
                if instruct == compute_cycle(check_value):
                    new_progress.append(check_value)
        A_progress = new_progress

    return min(A_progress)


def compute_cycle(A: int) -> int:
    B = A % 8
    B ^= 2
    C = A >> B
    B ^= 7
    B ^= C
    return B % 8


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].strip()
    return inputs_raw


A_example = 729
B_example = 0
C_example = 0
instructions_example = [0, 1, 5, 4, 3, 0]

A_real = 41644071
B_real = 0
C_real = 0
instructions_real = [2, 4, 1, 2, 7, 5, 1, 7, 4, 4, 0, 3, 5, 5, 3, 0]

print(f"Part 1: {part1(A=A_real, B=B_real, C=C_real, instructions=instructions_real)}")
print(f"Part 2: {part2(instructions=instructions_real)}")
