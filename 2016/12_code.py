from typing import List, Dict


def processor(memory, instructions):
    pointer = 0
    while 0 <= pointer < len(instructions):
        single_instruction = instructions[pointer]
        match single_instruction[0]:
            case 'cpy':
                info_source = single_instruction[1]
                if info_source.isdigit():
                    memory[single_instruction[2]] = int(info_source)
                else:
                    memory[single_instruction[2]] = memory[info_source]
            case 'inc':
                memory[single_instruction[1]] += 1
            case 'dec':
                memory[single_instruction[1]] -= 1
            case 'jnz':
                conditional = single_instruction[1]
                if conditional.isdigit():
                    conditional = int(conditional)
                else:
                    conditional = memory[conditional]

                if conditional != 0:
                    pointer += int(single_instruction[2]) - 1
            case _:
                print('ruh-roh')
        pointer += 1


def part1(bot_instructions: List[str]) -> None:
    registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    processor(registers, bot_instructions)
    print(f'Part 1: {registers["a"]}')

    registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
    processor(registers, bot_instructions)
    print(f'Part 2: {registers["a"]}')


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "").split(' ')
    return inputs_raw


## print(file_reader("12_input.txt"))
part1(file_reader('12_input.txt'))
#print(f"Part 2: {part2(file_reader('12_input.txt'))}")
