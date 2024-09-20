def generate_dictionary(raw_instructions) -> dict[str, list[str]]:
    pointing_at_me = dict()
    all_letters = set()
    for instruct in raw_instructions:
        if instruct[1] in pointing_at_me:
            pointing_at_me[instruct[1]].append(instruct[0])
        else:
            pointing_at_me[instruct[1]] = [instruct[0]]
        
        all_letters.add(instruct[0])
        all_letters.add(instruct[1])

    for key in pointing_at_me.keys():
        all_letters.discard(key)
    for key in all_letters:
        pointing_at_me[key] = []

    return pointing_at_me


def part1(raw_instructions) -> str:
    pointing_at_me = generate_dictionary(raw_instructions=raw_instructions)
    
    ans = []
    visited = set()
    
    while len(visited) < len(pointing_at_me):
        next_visited = set()
        for key, value in pointing_at_me.items():
            if (key not in visited) and all(v in visited for v in value):
                next_visited.add(key)
        ans_temp = list(next_visited)
        ans_temp.sort()
        ans.append(ans_temp[0])
        visited.add(ans_temp[0])

    return "".join(ans)


def part2(raw_instructions) -> str:
    pointing_at_me = generate_dictionary(raw_instructions=raw_instructions)

    counter = 0 

    ans = []
    done = set()
    working = set()

    elves = [[0, '-'], [0, '-'], [0, '-'], [0, '-'], [0, '-']]

    while len(done) < len(pointing_at_me):
        counter += 1
        unemployed_elves = []
        for index, e in enumerate(elves):
            e[0] += 1
            if e[1] == '-':
                unemployed_elves.append(index)
            elif e[0] == ord(e[1]) - 4:
                unemployed_elves.append(index)
                done.add(e[1])
                ans.append(e[1])
                working.discard(e[1])
                elves[index] = [0, '-']

        if len(unemployed_elves) > 0:
            next_visited = set()
            for key, value in pointing_at_me.items():
                if (key not in working) and (key not in done) and all(v in done for v in value):
                    next_visited.add(key)
            ans_temp = list(next_visited)
            ans_temp.sort()
            for job, elf in enumerate(unemployed_elves):
                if job < len(ans_temp):
                    elves[elf] = [0, ans_temp[job]]
                    working.add(ans_temp[job])
    
    return counter-1


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "").split()
        inputs_raw[i] = (inputs_raw[i][1], inputs_raw[i][7])
    return inputs_raw


raw_instructions = file_reader("07_input.txt")
print(f"Part 1: {part1(raw_instructions=raw_instructions)}")
print(f"Part 2: {part2(raw_instructions=raw_instructions)}")
