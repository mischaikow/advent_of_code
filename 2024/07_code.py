def part1(equations: list[str]):

    ans = 0

    for e in equations:
        total, remainder = e.split(": ")
        values = remainder.split(" ")

        total = int(total)
        values = [int(x) for x in values]

        operators = 2 ** (len(values) - 1) - 1

        for i in range(operators, -1, -1):
            running_total = values[0]
            number = i
            for pointer in range(len(values) - 1):
                if number % 2 == 0:
                    running_total += values[pointer + 1]
                else:
                    running_total *= values[pointer + 1]
                number >>= 1
            if running_total == total:
                ans += total
                break

    print(f"Part 1: {ans}")


def part2(equations: list[str]):

    ans = 0

    for e in equations:
        total, remainder = e.split(": ")
        values = remainder.split(" ")
        total = int(total)
        values = [int(x) for x in values]

        operators = 3 ** (len(values) - 1) - 1

        for i in range(operators, -1, -1):
            running_total = values[0]
            number = i
            for pointer in range(len(values) - 1):
                if number % 3 == 0:
                    running_total += values[pointer + 1]
                elif number % 3 == 1:
                    running_total *= values[pointer + 1]
                else:
                    running_total = int(str(running_total) + str(values[pointer + 1]))
                number = number // 3
            if running_total == total:
                ans += total
                break

    print(f"Part 2: {ans}")


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].strip()
    return inputs_raw


part1(file_reader("07_input.txt"))
part2(file_reader("07_input.txt"))
