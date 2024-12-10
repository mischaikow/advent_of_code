def part1(memory_original: str):

    memory_int = [int(x) for x in memory_original]

    checksum = 0

    lower = 0
    higher = len(memory_original) - 1
    higher_progress = 0

    counter = 0
    while higher > lower:
        if lower % 2 == 0:
            for i in range(memory_int[lower]):
                checksum += counter * (lower // 2)
                counter += 1
            lower += 1
        else:
            for i in range(memory_int[lower]):
                checksum += counter * (higher // 2)
                counter += 1
                higher_progress += 1
                if higher_progress == memory_int[higher]:
                    higher -= 2
                    if higher <= lower:
                        break
                    higher_progress = 0
            lower += 1

    while higher_progress < memory_int[higher]:
        checksum += counter * (higher // 2)
        counter += 1
        higher_progress += 1

    print(f"Part 1: {checksum}")


def part2(memory_original: str):

    memory_int = [int(x) for x in memory_original]
    weights = [weight_distribution(x) for x in range(len(memory_original))]

    max_move = max(weights) + 1
    i = len(weights) - 1
    while i > 0:
        if 0 < weights[i] < max_move:
            max_move = min(max_move, weights[i])
            j = 1
            while j < i:
                if weights[j] == 0:
                    if memory_int[j] == memory_int[i]:
                        weights[j] = weights[i]
                        weights[i] = 0
                        break

                    elif memory_int[j] > memory_int[i]:
                        memory_int[j] = memory_int[j] - memory_int[i]
                        memory_int.insert(j, memory_int[i])
                        weights.insert(j, weights[i])
                        weights[i + 1] = 0
                        break

                j += 1

            k = 1
            while k < len(memory_int) - 1:
                if weights[k] == weights[k + 1] == 0:
                    memory_int[k] += memory_int[k + 1]
                    memory_int.pop(k + 1)
                    weights.pop(k + 1)
                else:
                    k += 1

        i -= 1

    checksum = 0
    counter = 0
    for i in range(len(weights)):
        for j in range(memory_int[i]):
            checksum += counter * weights[i]
            counter += 1

    print(f"Part 2: {checksum}")


def weight_distribution(x):
    if x % 2 == 0:
        return x // 2
    return 0


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    return inputs_raw[0].strip()


part1(file_reader("09_input.txt"))
part2(file_reader("09_input.txt"))
