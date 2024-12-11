from collections import defaultdict


def part2(stones_str: list[str]):
    stones = defaultdict(int)
    for a_stone in stones_str:
        stones[int(a_stone)] += 1

    for k in range(75):
        new_stones = defaultdict(int)
        for a_stone, count in stones.items():
            if a_stone == 0:
                new_stones[1] += count
            elif len(str(a_stone)) % 2 == 0:
                front = int(str(a_stone)[: len(str(a_stone)) // 2])
                back = int(str(a_stone)[len(str(a_stone)) // 2 :])
                new_stones[front] += count
                new_stones[back] += count
            else:
                new_stones[2024 * a_stone] += count
        stones = new_stones

        if k == 24:
            ans = 0
            for count in stones.values():
                ans += count
            print(f"Part 1: {ans}")

    ans = 0
    for count in stones.values():
        ans += count
    print(f"Part 2: {ans}")


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    return inputs_raw[0].split()


part2(file_reader("11_input.txt"))
