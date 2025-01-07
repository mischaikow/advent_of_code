from collections import defaultdict


def part1(computer_connections: list[list[str]]) -> None:

    connections = defaultdict(set)
    for c in computer_connections:
        connections[c[0]].add(c[1])
        connections[c[1]].add(c[0])

    ans = 0
    for c in computer_connections:
        for cross in connections[c[0]]:
            if cross in connections[c[1]]:
                if c[0][0] == "t" or c[1][0] == "t" or cross[0] == "t":
                    ans += 1

    print(f"Part 1: {ans // 3}")


def part2(computer_connections: list[list[str]]) -> None:

    all_connections = set()
    all_computers = defaultdict(set)
    for conn in computer_connections:
        all_connections.add(tuple(sorted(conn)))
        all_computers[conn[0]].add(conn[1])
        all_computers[conn[1]].add(conn[0])

    for i in range(len(all_computers)):
        new_connections = set()

        while len(all_connections) > 0:
            connection_group = all_connections.pop()
            for val, neighbors in all_computers.items():
                if val not in connection_group:
                    if set(connection_group).issubset(neighbors):
                        new_group = connection_group + (val,)
                        new_group = tuple(sorted(list(new_group)))
                        new_connections.add(new_group)

        if len(new_connections) == 1:
            answer = ",".join(sorted(list(new_connections.pop())))
            print(f"Part 2: {answer}")
            break
        all_connections = new_connections


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].strip().split("-")
    return inputs_raw


part1(file_reader("23_input.txt"))
part2(file_reader("23_input.txt"))
