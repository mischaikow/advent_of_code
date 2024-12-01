from collections import defaultdict


def part1(feed: list[list[int]]):
    feed_one = []
    feed_two = []
    for pair in feed:
        feed_one.append(pair[0])
        feed_two.append(pair[1])

    feed_one.sort()
    feed_two.sort()

    ans = 0
    for i in range(len(feed_one)):
        ans += abs(feed_one[i] - feed_two[i])

    print(f"Part 1: {ans}")


def part2(feed: list[list[int]]):
    value_count = defaultdict(int)
    for _, value in feed:
        value_count[value] += 1

    ans = 0
    for value, _ in feed:
        if value in value_count:
            ans += value * value_count[value]

    print(f"Part 2: {ans}")


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].split()
        inputs_raw[i] = [int(x) for x in inputs_raw[i]]
    return inputs_raw


part1(file_reader("01_input.txt"))
part2(file_reader("01_input.txt"))
