import hashlib
from math import prod


def part1(input_string: str) -> None:
    pt1_ans = ""
    pt2_check = [0, 0, 0, 0, 0, 0, 0, 0]
    pt2_ans = ["_", "_", "_", "_", "_", "_", "_", "_"]
    for numb in range(100000000000):
        dummy = hashlib.md5((input_string + str(numb)).encode("utf-8")).hexdigest()
        if dummy[:5] == "00000":
            if len(pt1_ans) < 8:
                pt1_ans += dummy[5]
            if (
                dummy[5].isdigit()
                and int(dummy[5]) < 8
                and pt2_check[int(dummy[5])] == 0
            ):
                pt2_ans[int(dummy[5])] = dummy[6]
                pt2_check[int(dummy[5])] = 1
                print(f"Progress: {''.join(pt2_ans)}")
                if prod(pt2_check) == 1:
                    break

    print(f"Part 1: {pt1_ans}")
    print(f"Part 2: {''.join(pt2_ans)}")


puzzle_input = "abc"
puzzle_input = "ojvtpuvg"
part1(puzzle_input)
## print(part2(puzzle_input))
