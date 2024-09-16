def part1(ports_raw: list[str]) -> int:
    ports = []
    for p in ports_raw:
        p1, p2 = p.split("/")
        ports.append(((int(p1), int(p2))))

    current_port = 0
    used_ports = [0] * len(ports)

    def dive(current_port):
        strength = 0
        for i in range(len(ports)):
            if used_ports[i] == 0:
                if ports[i][0] == current_port:
                    used_ports[i] = 1
                    strength = max(strength, current_port + dive(ports[i][1]))
                    used_ports[i] = 0

                elif ports[i][1] == current_port:
                    used_ports[i] = 1
                    strength = max(strength, current_port + dive(ports[i][0]))
                    used_ports[i] = 0

        return strength + current_port

    return dive(current_port=current_port)


def part2(ports_raw: list[str]) -> int:
    ports = []
    for p in ports_raw:
        p1, p2 = p.split("/")
        ports.append(((int(p1), int(p2))))

    current_port = 0
    used_ports = [0] * len(ports)

    def dive(current_port):
        strength = 0
        depth = 0
        for i in range(len(ports)):
            if used_ports[i] == 0:
                if ports[i][0] == current_port:
                    used_ports[i] = 1
                    temp_strength, temp_depth = dive(ports[i][1])
                    if temp_depth > depth:
                        strength = current_port + temp_strength
                        depth = temp_depth
                    if temp_depth == depth:
                        strength = max(strength, current_port + temp_strength)
                    used_ports[i] = 0

                elif ports[i][1] == current_port:
                    used_ports[i] = 1
                    temp_strength, temp_depth = dive(ports[i][0])
                    if temp_depth > depth:
                        strength = current_port + temp_strength
                        depth = temp_depth
                    if temp_depth == depth:
                        strength = max(strength, current_port + temp_strength)
                    used_ports[i] = 0

        return strength + current_port, depth + 1

    return dive(current_port=current_port)[0]


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "")
    return inputs_raw


print(f"Part 1: {part1(file_reader('24_input.txt'))}")
print(f"Part 2: {part2(file_reader('24_input.txt'))}")
