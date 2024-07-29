def redistribute(memory: list[int]) -> None:
    target = max(memory)
    pointer = memory.index(target)
    memory[pointer] = 0
    for spot in range(pointer + 1, pointer + 1 + target):
        memory[spot % len(memory)] += 1


def part1(memory_banks: list[int]) -> None:
    pool = set()
    pool.add(tuple(memory_banks))

    counter = 0
    while True:
        old_size = len(pool)
        redistribute(memory_banks)
        pool.add(tuple(memory_banks))
        counter += 1
        if old_size == len(pool):
            print(f"Part 1: {counter}")
            return


def part2(memory_banks: list[int]) -> None:
    pool = set()

    counter = 0
    first_pass = True
    while True:
        old_size = len(pool)
        redistribute(memory_banks)
        pool.add(tuple(memory_banks))
        counter += 1
        if old_size == len(pool):
            if first_pass:
                pool = set()
                counter = -1
                first_pass = False
            else:
                print(f"Part 2: {counter}")
                return


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "").split()
        inputs_raw[i] = [int(x) for x in inputs_raw[i]]
    return inputs_raw[0]


test_input = [2, 4, 1, 2]

# print(file_reader('06_input.txt'))
# part1(test_input)
part1(file_reader("06_input.txt"))
part2(file_reader("06_input.txt"))
