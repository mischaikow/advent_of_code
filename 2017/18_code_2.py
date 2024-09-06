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

    def cycle(self, incoming: deque[int]) -> deque[int]:
        message: deque[int] = deque()
        while 0 <= self.pointer < len(self.instructions):
            this_line = self.instructions[self.pointer]
            match this_line[0]:
                case "snd":
                    message.append(find_value(self.memory, this_line[1]))
                case "set":
                    self.memory[this_line[1]] = find_value(self.memory, this_line[2])
                case "add":
                    self.memory[this_line[1]] += find_value(self.memory, this_line[2])
                case "mul":
                    self.memory[this_line[1]] *= find_value(self.memory, this_line[2])
                case "mod":
                    self.memory[this_line[1]] %= find_value(self.memory, this_line[2])
                case "rcv":
                    if len(incoming) > 0:
                        self.memory[this_line[1]] = incoming.popleft()
                    else:
                        return message
                case "jgz":
                    if find_value(self.memory, this_line[1]) > 0:
                        self.pointer += find_value(self.memory, this_line[2]) - 1
                case _:
                    print(f"Fail state: {this_line[0]}")
                    return deque()

            self.pointer += 1

        print("Out of bounds")
        return message

    def message_queue_size(self) -> int:
        return len(self.message)


def part2(instructions_raw: list[str]) -> int:
    memory = {}
    for line in instructions_raw:
        if is_memory_register(line[1]) and line[1] not in memory:
            memory[line[1]] = 0
        if len(line) == 3 and is_memory_register(line[2]) and line[2] not in memory:
            memory[line[2]] = 0

    box_0 = Duet(memory.copy(), instructions_raw)
    memory["p"] = 1
    box_1 = Duet(memory, instructions_raw)

    ans = 0
    message = box_0.cycle(deque())
    while len(message) > 0:
        message = box_1.cycle(message)
        ans += len(message)
        if len(message) > 0:
            message = box_0.cycle(message)

    return ans


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "").split()
    return inputs_raw


print(f"Part 2: {part2(file_reader('18_input.txt'))}")
