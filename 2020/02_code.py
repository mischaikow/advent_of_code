"""Day 2 of the 2020 Advent of Code event


"""

def fileReader(fileName):
    input_file = open(fileName, 'r')
    inputs_raw = input_file.readlines()
    code_letter, code_min, code_max, passwords = [], [], [], []
    for i in range(len(inputs_raw)):
        temp = inputs_raw[i]
        code_min.append(int(temp[:temp.index('-')]))
        code_max.append(int(temp[temp.index('-')+1:temp.index(' ')]))
        code_letter.append(temp[temp.index(' ')+1:temp.index(':')])
        temp = temp[temp.index(' ')+1:]
        passwords.append(temp[temp.index(' ')+1:temp.index('\n')])
    return code_letter, code_min, code_max, passwords


def goodPassCounter(fileName):
    counter = 0
    code_letter, code_min, code_max, passwords = fileReader(fileName)
    for i in range(len(passwords)):
        occurrence = passwords[i].count(code_letter[i])
        if code_min[i] <= occurrence and code_max[i] >= occurrence:
            counter += 1
    return counter


def newGoodPassCounter(fileName):
    counter = 0
    code_letter, code_min, code_max, passwords = fileReader(fileName)
    for i in range(len(passwords)):
        if (passwords[i][code_min[i] - 1] == code_letter[i]) ^ \
           (passwords[i][code_max[i] - 1] == code_letter[i]):
            counter += 1
    return counter


def main():
    print("Part one:", goodPassCounter('input_02_1.txt'))
    print("Part two:", newGoodPassCounter('input_02_1.txt'))
    

main()
