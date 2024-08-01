def part1(dance_raw: list[str]) -> None:
    positions = [chr(x) for x in range(97, 113)]
    looped = ''.join(positions)
    seen_positions = [''.join(positions)]
    for x in range(1000 * 1000 * 1000):
        for step in dance_raw:
            instruction = step[0]
            match instruction:
                case 's':
                    distance = int(step[1:])
                    positions = positions[-1*distance:] + positions[:-1*distance]
                case 'x':
                    pos_a_str, pos_b_str = step[1:].split('/')
                    pos_a = int(pos_a_str)
                    pos_b = int(pos_b_str)
                    positions[pos_a], positions[pos_b] = positions[pos_b], positions[pos_a]
                case 'p':
                    first_char, second_char = step[1:].split('/')
                    pos_a = positions.index(first_char)
                    pos_b = positions.index(second_char)
                    positions[pos_a], positions[pos_b] = positions[pos_b], positions[pos_a]
        
        if x == 0:
            print(f'Part 1: {''.join(positions)}')
        
        if ''.join(positions) == looped:
            loop_length = x+1
            break

        seen_positions.append(''.join(positions))

    print(f'Part 2: {seen_positions[1000000000 % loop_length]}')


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "").split(",")
    return inputs_raw[0]


part1(file_reader("16_input.txt"))
