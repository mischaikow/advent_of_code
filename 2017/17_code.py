CYCLE_COUNT = 2018
CYCLE_COUNT_LONG = 50 * 1000 * 1000


def part1(step_count: int) -> None:
    the_list = [0]
    pointer = 0
    for x in range(1, CYCLE_COUNT):
        pointer = (step_count + pointer) % len(the_list)
        the_list = the_list[: pointer + 1] + [x] + the_list[pointer + 1 :]
        pointer += 1 % len(the_list)

    print(f"Part 1: {the_list[the_list.index(CYCLE_COUNT-1) + 1]}")


def part2(step_count: int) -> None:
    pointer = 0
    ans = 0
    for x in range(1, CYCLE_COUNT_LONG):
        pointer = (step_count + pointer) % x
        if pointer == 0:
            ans = x
        pointer += 1 % (x + 1)

    print(f"Part 2: {ans}")


TEST_VALUE = 3
ACTUAL_VALUE = 367
part1(ACTUAL_VALUE)
part2(ACTUAL_VALUE)
