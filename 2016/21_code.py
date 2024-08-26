def scramble_step(com: list[str], pass_list: list[str]) -> list[str]:
    command_type = com[0] + ' ' + com[1]

    match command_type:
        case 'swap position':
            position_1 = int(com[2])
            position_2 = int(com[5])
            temp = pass_list[position_1]
            pass_list[position_1] = pass_list[position_2]
            pass_list[position_2] = temp
        case 'swap letter':
            position_1 = pass_list.index(com[2])
            position_2 = pass_list.index(com[5])
            temp = pass_list[position_1]
            pass_list[position_1] = pass_list[position_2]
            pass_list[position_2] = temp
        case 'rotate left':
            sub_list_1 = pass_list[int(com[2]):]
            sub_list_2 = pass_list[:int(com[2])]
            pass_list = sub_list_1 + sub_list_2
        case 'rotate right':
            sub_list_1 = pass_list[len(pass_list) - int(com[2]):]
            sub_list_2 = pass_list[:len(pass_list) - int(com[2])]
            pass_list = sub_list_1 + sub_list_2
        case 'rotate based':
            position = pass_list.index(com[6])
            if position >= 4:
                position += 1
            position += 1
            position %= len(pass_list)
            sub_list_1 = pass_list[len(pass_list) - position:]
            sub_list_2 = pass_list[:len(pass_list) - position]
            pass_list = sub_list_1 + sub_list_2
        case 'reverse positions':
            sub_list_1 = pass_list[:int(com[2])]
            sub_list_2 = pass_list[int(com[2]):int(com[4]) + 1]
            sub_list_2.reverse()
            sub_list_3 = pass_list[int(com[4]) + 1:]
            pass_list = sub_list_1 + sub_list_2 + sub_list_3
        case 'move position':
            value = pass_list[int(com[2])]
            sub_list_1 = pass_list[:int(com[2])]
            sub_list_2 = pass_list[int(com[2]) + 1:]
            pass_list = sub_list_1 + sub_list_2
            sub_list_1 = pass_list[:int(com[5])]
            sub_list_2 = pass_list[int(com[5]):]
            pass_list = sub_list_1 + [value] + sub_list_2
        case _:
            print('ERROR')
            print(com)
            print('')
    
    return pass_list


def part1(instructions: list[list[str]], pass_string: str) -> str:
    pass_list = list(pass_string)

    for com in instructions:
        pass_list = scramble_step(com, pass_list)

    return ''.join(pass_list)

def scramble_step_reverse(com: list[str], pass_list: list[str]) -> list[str]:
    command_type = com[0] + ' ' + com[1]

    match command_type:
        case 'swap position':
            position_1 = int(com[2])
            position_2 = int(com[5])
            temp = pass_list[position_1]
            pass_list[position_1] = pass_list[position_2]
            pass_list[position_2] = temp
        case 'swap letter':
            position_1 = pass_list.index(com[2])
            position_2 = pass_list.index(com[5])
            temp = pass_list[position_1]
            pass_list[position_1] = pass_list[position_2]
            pass_list[position_2] = temp
        case 'rotate left':
            sub_list_1 = pass_list[len(pass_list) - int(com[2]):]
            sub_list_2 = pass_list[:len(pass_list) - int(com[2])]
            pass_list = sub_list_1 + sub_list_2
        case 'rotate right':
            sub_list_1 = pass_list[int(com[2]):]
            sub_list_2 = pass_list[:int(com[2])]
            pass_list = sub_list_1 + sub_list_2
        case 'rotate based':
            position = pass_list.index(com[6])
            change = {0:1, 1:1, 2:6, 3:2, 4:7, 5:3, 6:0, 7:4}
            steps = change[position]
            sub_list_1 = pass_list[steps:]
            sub_list_2 = pass_list[:steps]
            pass_list = sub_list_1 + sub_list_2
        case 'reverse positions':
            sub_list_1 = pass_list[:int(com[2])]
            sub_list_2 = pass_list[int(com[2]):int(com[4]) + 1]
            sub_list_2.reverse()
            sub_list_3 = pass_list[int(com[4]) + 1:]
            pass_list = sub_list_1 + sub_list_2 + sub_list_3
        case 'move position':
            value = pass_list[int(com[5])]
            sub_list_1 = pass_list[:int(com[5])]
            sub_list_2 = pass_list[int(com[5]) + 1:]
            pass_list = sub_list_1 + sub_list_2
            sub_list_1 = pass_list[:int(com[2])]
            sub_list_2 = pass_list[int(com[2]):]
            pass_list = sub_list_1 + [value] + sub_list_2
        case _:
            print('ERROR')
            print(com)
            print('')
    
    return pass_list


def part2(instructions: list[list[str]], pass_string: str) -> str:
    pass_list = list(pass_string)

    for com in reversed(instructions):
        pass_list = scramble_step_reverse(com, pass_list)

    return ''.join(pass_list)



def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "").split(" ")
    return inputs_raw

ACTUAL_INPUT_1 = 'abcdefgh'
ACTUAL_INPUT_2 = 'fbgdceah'

## print(file_reader("21_input.txt"))
print(f"Part 1: {part1(file_reader('21_input.txt'), ACTUAL_INPUT_1)}")
print(f"Part 2: {part2(file_reader('21_input.txt'), ACTUAL_INPUT_2)}")
