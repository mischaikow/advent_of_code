from collections import deque


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


class Duet:
    def __init__(self, memory: dict[int], instructions: list[str]) -> None:
        self.memory = memory
        self.instructions = instructions
        self.pointer = 0
        self.ans = 0

    def cycle(self) -> int:
        while 0 <= self.pointer < len(self.instructions):
            this_line = self.instructions[self.pointer]
            match this_line[0]:
                case "set":
                    self.memory[this_line[1]] = find_value(self.memory, this_line[2])
                case "sub":
                    self.memory[this_line[1]] -= find_value(self.memory, this_line[2])
                case "mul":
                    self.memory[this_line[1]] *= find_value(self.memory, this_line[2])
                    self.ans += 1
                case "jnz":
                    if find_value(self.memory, this_line[1]) != 0:
                        self.pointer += find_value(self.memory, this_line[2]) - 1
                case _:
                    print(f"Fail state: {this_line[0]}")
                    return self.ans

            self.pointer += 1

        return self.ans


def part1(instructions_raw: list[str]) -> int:
    memory = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0}
    proc = Duet(memory=memory, instructions=instructions_raw)

    return proc.cycle()


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "").split()
    return inputs_raw


print(f"Part 1: {part1(file_reader('23_input.txt'))}")
