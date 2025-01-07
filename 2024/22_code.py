from collections import deque, defaultdict


def part1(secret_starts: list[int]) -> None:

    ans = 0
    for number in secret_starts:
        for _ in range(2000):
            number = number_evolution(number)
        ans += number

    print(f"Part 1: {ans}")


def part2(secret_starts: list[int]) -> None:
    price_sequences = defaultdict(int)

    for number in secret_starts:
        new_price_sequences = dict()
        last_five_levels = deque([number % 10])

        for _ in range(2000):
            number = number_evolution(number)
            last_five_levels.append(number % 10)
            if len(last_five_levels) == 5:
                last_four = last_five_levels_deltas(last_five_levels)
                if last_four not in new_price_sequences:
                    new_price_sequences[last_four] = last_five_levels[-1]
                last_five_levels.popleft()

        for key, val in new_price_sequences.items():
            price_sequences[key] += val

    ans = 0
    for val in price_sequences.values():
        ans = max(ans, val)

    print(f"Part 2: {ans}")


def number_evolution(number: int) -> int:
    number = ((number * 64) ^ number) % 16777216
    number = ((number // 32) ^ number) % 16777216
    number = ((number * 2048) ^ number) % 16777216
    return number


def last_five_levels_deltas(levels: deque[int]) -> tuple[int]:
    one = levels[1] - levels[0]
    two = levels[2] - levels[1]
    three = levels[3] - levels[2]
    four = levels[4] - levels[3]
    return (one, two, three, four)


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = int(inputs_raw[i].strip())
    return inputs_raw


part1(file_reader("22_input.txt"))
part2(file_reader("22_input.txt"))
