from collections import defaultdict

def solution(data_raw, enhancements):
    first_line = {}
    
    for i, val in enumerate(data_raw[0]):
        first_line[i] = val

    padding = 3
    image = [['.'] * (len(data_raw[2]) + 2*padding) for _ in range(padding)]
    for line in data_raw[2:]:
        new_line = ['.'] * padding + list(line) + ['.'] * padding
        image.append(new_line)
    new_lines = [['.'] * (len(data_raw[2]) + 2*padding) for _ in range(padding)]
    image += new_lines

    for step in range(enhancements):
        blank = '.' if step % 2 else '#'
        new_image = [[blank] * (4 + len(image[0]))]
        new_image.append([blank] * (4 + len(image[0])))
        new_image.append([blank] * (4 + len(image[0])))
        for i in range(1, len(image)-1, 1):
            new_image.append([blank])
            new_image[-1].append(blank)
            new_image[-1].append(blank)
            for j in range(1, len(image[0])-1, 1):
                rep = []
                for ii in [-1, 0, 1]:
                    for jj in [-1, 0, 1]:
                        rep.append('1' if image[i+ii][j+jj] == '#' else '0')
                        lookup = int(''.join(rep), 2)
                new_image[-1].append(first_line[lookup])
            new_image[-1].append(blank)
            new_image[-1].append(blank)
            new_image[-1].append(blank)
        new_image.append([blank] * (4 + len(image[0])))
        new_image.append([blank] * (4 + len(image[0])))
        new_image.append([blank] * (4 + len(image[0])))
        image = new_image

    ans = 0
    for line in image:
        for val in line:
            if val == '#':
                ans += 1

    return ans

def part_2(data_raw):
    return None
 
def file_reader(file_name):
    input_file = open(file_name, 'r')
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace('\n', '')
    return inputs_raw

print(solution(file_reader('input_20.txt'), 2))
print(solution(file_reader('input_20.txt'), 50))
