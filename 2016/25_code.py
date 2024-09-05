inc_dec = {'inc', 'dec'}


def next_command(current_command: str) -> str:
    match current_command:
        case 'cpy':
            return 'jnz'
        case 'jnz':
            return 'cpy'
        case 'inc':
            return 'dec'
        case 'dec':
            return 'inc'
        case 'tgl':
            return 'inc'
        case _:
            print(f'you missed {current_command}')
            return ''


def mismatch(a: str, b: str, c: str, multis: set[str]) -> str:
    if not a in multis:
        return a
    if not b in multis:
        return b
    if not c in multis:
        return c


def special_multiply(memory, instructions, pointer):
    if instructions[pointer][0] in inc_dec and \
            instructions[pointer+1][0] in inc_dec and \
            instructions[pointer+2][0] == 'jnz' and \
            instructions[pointer+2][2] == '-2' and \
            instructions[pointer+3][0] in inc_dec and \
            instructions[pointer+4][0] == 'jnz' and \
            instructions[pointer+4][2] == '-5':

        multiplier_1 = instructions[pointer+2][1]
        multiplier_2 = instructions[pointer+4][1]
        mult_1_value = int(multiplier_1) if multiplier_1.isdigit() else memory[multiplier_1]
        mult_2_value = int(multiplier_2) if multiplier_2.isdigit() else memory[multiplier_2]
        value_add = mult_1_value * mult_2_value

        destination = mismatch(instructions[pointer][1],
                               instructions[pointer+1][1],
                               instructions[pointer+3][1],
                               {multiplier_1, multiplier_2})
        

        if instructions[pointer][1] == destination:
            if instructions[pointer][0] == 'inc':
                memory[destination] += abs(value_add)
            if instructions[pointer][0] == 'dec':
                memory[destination] -= abs(value_add)
        elif instructions[pointer+1][1] == destination:
            if instructions[pointer+1][0] == 'inc':
                memory[destination] += abs(value_add)
            if instructions[pointer+1][0] == 'dec':
                memory[destination] -= abs(value_add)
        else:
            return False
    else:
        return False
    return True

        

def processor(memory, instructions) -> list[int]:
    pointer = 0
    ticker_tape = []
    counter = 0
    while 0 <= pointer < len(instructions):

#        if counter == 0:
#            print(f'Instruction value {pointer+1}: {' '.join(instructions[pointer])}')
#            print(memory)
#            cycles = input('--')
#            if cycles != '':
#                counter = int(cycles)
#        else:
#            counter -= 1

        single_instruction = instructions[pointer]
        if single_instruction[0] in inc_dec and special_multiply(memory, instructions, pointer):
            pointer += 5
        else:
            match single_instruction[0]:
                case 'cpy':
                    info_source = single_instruction[1]
                    if info_source.isdigit() or info_source[0] == '-':
                        memory[single_instruction[2]] = int(info_source)
                    else:
                        memory[single_instruction[2]] = memory[info_source]
                case 'inc':
                    memory[single_instruction[1]] += 1
                case 'dec':
                    memory[single_instruction[1]] -= 1
                case 'jnz':
                    conditional = single_instruction[1]
                    if conditional.isdigit() or conditional[0] == '-':
                        conditional = int(conditional)
                    else:
                        conditional = memory[conditional]

                    if conditional != 0:
                        if single_instruction[2].isdigit() or single_instruction[2][0] == '-':
                            pointer += int(single_instruction[2]) - 1
                        else:
                            pointer += memory[single_instruction[2]] - 1
                case 'tgl':
                    target = memory[single_instruction[1]] + pointer
                    if 0 <= target < len(instructions):
                        reference_instruction = instructions[target][0]
                        instructions[target][0] = next_command(reference_instruction)
                case 'out':
                    value = single_instruction[1]
                    if value.isdigit():
                        ticker_tape.append(value)
                    else:
                        ticker_tape.append(memory[value])
                    if len(ticker_tape) >= 14:
                        return ticker_tape
                case _:
                    print('ruh-roh')
            pointer += 1


def part1(bot_instructions: list[list[str]]) -> None:
    registers = {"a": 0, "b": 0, "c": 0, "d": 0}
    for i in range(1, 1_000_000):
        registers["a"] = i
        ticket = processor(registers, bot_instructions)
        if sum(ticket) == len(ticket) // 2:
            if ticket[0] == ticket[2] == ticket[4] == ticket[6] == ticket[8] == ticket[10] == ticket[12] and \
                    ticket[1] == ticket[3] == ticket[5] == ticket[7] == ticket[9] == ticket[11] == ticket[13]:
                print(ticket)
                print(i)
                return

def part0(bot_instructions: list[list[str]]) -> None:
    registers = {"a": 2, "b": 0, "c": 0, "d": 0}
    processor(registers, bot_instructions)


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "").split()
    return inputs_raw


## print(file_reader("25_input.txt"))
part1(file_reader('25_input.txt'))
## part0(file_reader('25_input.txt'))
