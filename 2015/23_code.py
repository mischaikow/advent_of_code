

def processor(memory, instructions):
    pointer = 0
    while 0 <= pointer < len(instructions):
        single_instruction = instructions[pointer]
        match single_instruction[0]:
            case 'hlf':
                memory[single_instruction[1]] = memory[single_instruction[1]] // 2
            case 'tpl':
                memory[single_instruction[1]] *= 3
            case 'inc':
                memory[single_instruction[1]] += 1
            case 'jmp':
                distance = single_instruction[1]
                if distance[1:].isdigit():
                    distance = int(distance)
                else:
                    distance = memory[distance]

                pointer += distance - 1
            case 'jie':
                conditional = single_instruction[1][:-1]
                if conditional[1:].isdigit():
                    conditional = int(conditional)
                else:
                    conditional = memory[conditional]

                if conditional % 2 == 0:
                    pointer += int(single_instruction[2]) - 1
            case 'jio':
                conditional = single_instruction[1][:-1]
                if conditional[1:].isdigit():
                    conditional = int(conditional)
                else:
                    conditional = memory[conditional]

                if conditional == 1:
                    pointer += int(single_instruction[2]) - 1
            case _:
                print(single_instruction[0])
        pointer += 1


def part1(bot_instructions: list[str]) -> None:
    registers = {'a': 0, 'b': 0}
    processor(registers, bot_instructions)
    print(f'Part 1: {registers["b"]}')

    registers = {'a': 1, 'b': 0}
    processor(registers, bot_instructions)
    print(f'Part 2: {registers["b"]}')


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "").split(' ')
    return inputs_raw


## print(file_reader("23_input.txt"))
part1(file_reader('23_input.txt'))
#print(f"Part 2: {part2(file_reader('23_input.txt'))}")
