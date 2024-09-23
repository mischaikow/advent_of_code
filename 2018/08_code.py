def part1(raw_license: list[int]) -> int:
    ans = 0

    the_stack = []
    the_stack.append([raw_license[0], raw_license[1]])
    pointer = 2

    while len(the_stack) > 0:
        whos_next = the_stack.pop()
        if whos_next[0] == 0:
            ans += raw_license[pointer]
            pointer += 1
            if whos_next[1] > 1:
                the_stack.append([whos_next[0], whos_next[1] - 1])
        else:
            the_stack.append([whos_next[0] - 1, whos_next[1]])
            the_stack.append([raw_license[pointer], raw_license[pointer + 1]])
            pointer += 2

    return ans


def part2(raw_license: list[int]) -> int:
    the_stack = []
    stack_children_count = []
    stack_meta_count = []

    pointer = 0
    while pointer < len(raw_license):
        children_count = raw_license[pointer]
        meta_count = raw_license[pointer + 1]
        pointer += 2

        if children_count == 0:
            temp_sum = 0
            for i in range(meta_count):
                temp_sum += raw_license[pointer]
                pointer += 1
            the_stack[-1].append(temp_sum)

        else:
            the_stack.append([])
            stack_children_count.append(children_count)
            stack_meta_count.append(meta_count)

        while stack_children_count[-1] == len(the_stack[-1]):
            temp_sum = 0
            children_sums = the_stack.pop()
            meta_count = stack_meta_count.pop()
            children_count = stack_children_count.pop()
            for i in range(meta_count):
                meta_reference = raw_license[pointer]
                if 0 < meta_reference < children_count + 1:
                    temp_sum += children_sums[meta_reference - 1]
                pointer += 1
            if len(the_stack) == 0:
                return temp_sum
            the_stack[-1].append(temp_sum)


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "").split()
    return [int(x) for x in inputs_raw[0]]


raw_license = file_reader("08_input.txt")
print(f"Part 1: {part1(raw_license)}")
print(f"Part 2: {part2(raw_license)}")
