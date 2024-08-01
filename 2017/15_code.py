THE_DIVISOR = 2147483647
A_FACTOR = 16807
B_FACTOR = 48271


def part1(a_start: int, b_start: int) -> None:
    loops = 40 * 1000 * 1000

    ans = 0
    for _ in range(loops):
        a_start = (a_start * A_FACTOR) % THE_DIVISOR
        b_start = (b_start * B_FACTOR) % THE_DIVISOR

        if a_start % (2**16) == b_start % (2**16):
            ans += 1

    print(f"Part 1: {ans}")


def part2(a_start: int, b_start: int) -> None:
    loops = 5 * 1000 * 1000

    ans = 0
    for _ in range(loops):
        a_start = (a_start * A_FACTOR) % THE_DIVISOR
        b_start = (b_start * B_FACTOR) % THE_DIVISOR

        while not a_start % 4 == 0:
            a_start = (a_start * A_FACTOR) % THE_DIVISOR
        while not b_start % 8 == 0:
            b_start = (b_start * B_FACTOR) % THE_DIVISOR

        if a_start % (2**16) == b_start % (2**16):
            ans += 1

    print(f"Part 2: {ans}")


TEST_A = 65
TEST_B = 8921
ACTUAL_A = 591
ACTUAL_B = 393
part1(ACTUAL_A, ACTUAL_B)
# part2(TEST_A, TEST_B)
part2(ACTUAL_A, ACTUAL_B)
