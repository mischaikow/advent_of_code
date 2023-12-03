

def part1(doc):
    ans = 0

    for line in doc:
        line_val = 0
        for char in line:
            if char.isdigit():
                line_val += 10*int(char)
                break
        for char in reversed(line):
            if char.isdigit():
                line_val += int(char)
                break
        ans += line_val

    print(ans)


def part2(doc):
    number_word_start = {'z', 'o', 't', 'f', 's', 'e', 'n'}

    ans = 0

    for line in doc:
        line_val = 0
        for i in range(len(line)):
            if line[i].isdigit():
                line_val += 10*int(line[i])
                break
            elif line[i] in number_word_start and str_val(line[i:]) > 0:
                line_val += 10*str_val(line[i:])
                break
        for i in range(len(line)-1, -1, -1):
            if line[i].isdigit():
                line_val += int(line[i])
                break
            elif line[i] in number_word_start and str_val(line[i:]) > 0:
                line_val += str_val(line[i:])
                break
        ans += line_val

    print(ans)


def str_val(a_str):
    word_dict = {
            "zero": 0,
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9
        }

    for key in word_dict:
        if a_str[:len(key)] == key:
            return word_dict[key]

    return -1


def file_reader(file_name: str):
    input_file = open(file_name, 'r')
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace('\n', '')
    return inputs_raw

part1(file_reader('01_input.txt'))
part2(file_reader('01_input.txt'))
