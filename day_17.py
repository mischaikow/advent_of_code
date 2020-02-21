"""Day 17

The Interpreter has to save a poor vacuum robot.

Because the Interpreter has stabilized I've finally put it in it's
own class in it's own file interpreter.py.

"""

from interpreter import Interpreter


def instruct_file_read(fileName):
    # Read and interpret the file
    command_file = open(fileName, 'r')
    commands_raw = command_file.readline().split(',')
    commands_raw[-1] = commands_raw[-1].replace('\n', '')
    return list(map(int, commands_raw))


def show_camera(intcode):
    # Cycle through the intcode and produce the output
    session = Interpreter(intcode)
    scaffold = [[]]
    row = 0
    while True:
        pixel = session.run_interpreter()

        if pixel is None:
            break
        
        if pixel == 10:
            scaffold.append([])
            row += 1
        else:
            scaffold[row].append(str(chr(pixel)))
    return scaffold[:-2]


def compute_alignment(scaffold):
    value = 0
    for row in range(1, len(scaffold)-1):
        for col in range(1, len(scaffold[0])-1):
            if scaffold[row][col] == '#':
                above = scaffold[row-1][col]
                left = scaffold[row][col-1]
                right = scaffold[row][col+1]
                below = scaffold[row+1][col]
                if above == '#' \
                   and left == '#' \
                   and right == '#' \
                   and below == '#':
                    value += row * col
    return value


def main():
    intcode = instruct_file_read("input.txt")
    intcode_two = intcode.copy()
    scaffold = show_camera(intcode)
    print(compute_alignment(scaffold))

    # Part two
    intcode_two[0] = 2
    
    
main()
