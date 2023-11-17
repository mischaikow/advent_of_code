
def part_1(inst):
    ans = 0
    for x in range(-50, 51, 1):
        for y in range(-50, 51, 1):
            for z in range(-50, 51, 1):
                for step in range(len(inst)-1, -1, -1):
                    c = inst[step]
                    if c[1] <= x <= c[2] and \
                            c[3] <= y <= c[4] and \
                            c[5] <= z <= c[6]:
                        ans += c[0]
                        break

    return ans

def is_three_overlap(box_1, box_2):
    return not (box_1[1] >= box_2[2] or box_1[2] <= box_2[1]) and \
            not (box_1[3] >= box_2[4] or box_1[4] <= box_2[3]) and \
            not (box_1[5] >= box_2[6] or box_1[6] <= box_2[5])

def three_filter(box, seen):
    chopped_box = [box]
    for box_2 in seen:
        new_chopped_box = []
        for box_1 in chopped_box:
            if is_three_overlap(box_1, box_2):
                combos = []
                for degree in range(3):
                    combos.append([])
                    combos[degree].append(box_1[degree*2 + 1])
                    if box_1[degree*2 + 1] < box_2[degree*2 + 1]:
                        combos[degree].append(box_2[degree*2 + 1])
                    if box_1[degree*2 + 2] > box_2[degree*2 + 2]:
                        combos[degree].append(box_2[degree*2 + 2])
                    combos[degree].append(box_1[degree*2 + 2])

                for i in range(len(combos[0])-1):
                    for j in range(len(combos[1])-1):
                        for k in range(len(combos[2])-1):
                            new_chopped_box.append([0, \
                                    combos[0][i], combos[0][i+1], \
                                    combos[1][j], combos[1][j+1], \
                                    combos[2][k], combos[2][k+1]])
                            if is_three_overlap(box_2, new_chopped_box[-1]):
                                new_chopped_box.pop()

            else:
                new_chopped_box.append(box_1)
        chopped_box = new_chopped_box

    ans = 0
    for box in chopped_box:
        ans += (box[2] - box[1]) * (box[4] - box[3]) * (box[6] - box[5])

                # Now I need to chop up the box...
            
    ##  We're going to take our box, and compare it to what we've seen thus far. Whatever is left is what we add to our running total.
    return ans

def part_2(inst):
    ans = 0
    for step in range(len(inst)-1, -1, -1):
        if inst[step][0] == 1:
            ans += three_filter(inst[step], inst[step+1:])
    return ans
 
def file_reader(file_name):
    input_file = open(file_name, 'r')
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace('\n', '')
        tmp = inputs_raw[i].split(' ')
        tmp_2 = tmp[1].split(',')
        tmp_2 = [x[2:] for x in tmp_2]
        x = tmp_2[0].split('..')
        y = tmp_2[1].split('..')
        z = tmp_2[2].split('..')
        trigger = 1 if tmp[0] == 'on' else 0
        inputs_raw[i] = [trigger,
                        int(x[0]), int(x[1])+1,
                        int(y[0]), int(y[1])+1,
                        int(z[0]), int(z[1])+1]
    return inputs_raw

print(part_1(file_reader('input_22.txt')))
print(part_2(file_reader('input_22.txt')))
