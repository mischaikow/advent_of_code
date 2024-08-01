def part1(raw_connections: str) -> None:
    clusters = []

    for raw_conn in raw_connections:
        a, b = raw_conn.split(" <-> ")
        b_list = b.split(", ")
        bunch = [int(a)] + [int(x) for x in b_list]

        existing_pool = set()
        for conn in bunch:
            for pointer in range(len(clusters)):
                if conn in clusters[pointer]:
                    existing_pool.add(pointer)

        list_pool = list(existing_pool)
        list_pool.sort(reverse=True)

        new_set = set(bunch)
        if len(list_pool) != 0:
            for pointer in list_pool:
                new_set = new_set.union(clusters.pop(pointer))
        clusters.append(new_set)

    for a_cluster in clusters:
        if 0 in a_cluster:
            print(f"Part 1: {len(a_cluster)}")

    print(f"Part 2: {len(clusters)}")


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "")
    return inputs_raw


part1(file_reader("12_input.txt"))
