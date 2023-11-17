
def part_1(state):
    counter = 0
    measure = True

    while measure:
        new_state = [['.'] * len(state[0]) for _ in range(len(state))]
        counter += 1
        measure = False

        # go east
        for i, line in enumerate(state):
            for j, val in enumerate(line):
                jj = j + 1 if j+1 < len(line) else 0
                if state[i][j] == '>':
                    if state[i][jj] == '.':
                        measure = True
                        new_state[i][jj] = '>'
                    else:
                        new_state[i][j] = '>'
                elif state[i][j] == 'v':
                    new_state[i][j] = 'v'

        state = new_state
        new_state = [['.'] * len(state[0]) for _ in range(len(state))]

        # go south
        for i, line in enumerate(state):
            for j, val in enumerate(line):
                ii = i + 1 if i+1 < len(state) else 0
                if state[i][j] == 'v':
                    if state[ii][j] == '.':
                        measure = True
                        new_state[ii][j] = 'v'
                    else:
                        new_state[i][j] = 'v'
                elif state[i][j] == '>':
                    new_state[i][j] = '>'

        state = new_state

    print(counter)

def file_reader(file_name):
    input_file = open(file_name, 'r')
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = list(inputs_raw[i].replace('\n', ''))
    return inputs_raw

part_1(file_reader('input_25.txt'))
