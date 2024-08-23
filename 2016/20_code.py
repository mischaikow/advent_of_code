def part1(ip_ranges_raw: list[list[int]]) -> int:
    ip_ranges_raw.sort(key=lambda ip: ip[0])
    minimum = 0
    for block in ip_ranges_raw:
        if block[0] <= minimum:
            minimum = max(minimum, block[1] + 1)
        else:
            return minimum
    
    return -1


def part2(ip_ranges_raw: list[list[int]]) -> int:
    ip_ranges_raw.sort(key=lambda ip: ip[0])
    minimum = 0
    ans = 0
    for block in ip_ranges_raw:
        if block[0] <= minimum:
            minimum = max(minimum, block[1] + 1)
        else:
            ans += block[0] - minimum
            minimum = block[1] + 1
    
    return ans



def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "").split('-')
        inputs_raw[i] = [int(inputs_raw[i][0]), int(inputs_raw[i][1])]
    return inputs_raw


## print(file_reader("20_input.txt"))
print(f"Part 1: {part1(file_reader('20_input.txt'))}")
print(f"Part 2: {part2(file_reader('20_input.txt'))}")
