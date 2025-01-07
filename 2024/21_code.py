### Normally I delete extra print statements and debugging,
# but this was such a mess I decided to keep it all


from collections import deque
from functools import cache

TIME = 100
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

MOVES = {
    "A": {
        "^": "<A",
        ">": "vA",
        "v": "<vA",
        "<": "v<<A",
    },
    "^": {
        "A": ">A",
        ">": "v>A",
        "v": "vA",
        "<": "v<A",
    },
    ">": {
        "^": "<^A",
        "A": "^A",
        "v": "<A",
        "<": "<<A",
    },
    "v": {
        "^": "^A",
        ">": ">A",
        "A": "^>A",
        "<": "<A",
    },
    "<": {
        "^": ">^A",
        ">": ">>A",
        "v": ">A",
        "A": ">>^A",
    },
}

# (start, end, layers) -> int
depth_chart = dict()


def part1(codes: list[str], brute_count) -> None:

    ans = 0
    ans_pt2 = 0
    precompute = keyboard_extension(brute_count=brute_count)
    for code in codes:
        new_string = keyboard_computataion(code, precompute)

        ans += len(new_string) * int(code[:3])
        # print(f"{code}: ({len(new_string)})  {new_string}")
        ans_pt2 += depth_size(new_string, 21) * int(code[:3])

    print(f"Part 1: {ans}")
    print(f"Part 2: {ans_pt2}")


def keyboard_extension(brute_count: int) -> dict[str, str]:
    table = {
        (1, 3): "9",
        (1, 2): "8",
        (1, 1): "7",
        (2, 3): "6",
        (2, 2): "5",
        (2, 1): "4",
        (3, 3): "3",
        (3, 2): "2",
        (3, 1): "1",
        (4, 2): "0",
        (4, 3): "A",
        (4, 1): "XX",
    }

    table_2 = {
        "9": (1, 3),
        "8": (1, 2),
        "7": (1, 1),
        "6": (2, 3),
        "5": (2, 2),
        "4": (2, 1),
        "3": (3, 3),
        "2": (3, 2),
        "1": (3, 1),
        "0": (4, 2),
        "A": (4, 3),
    }

    precompute = dict()

    for i, start_coord in table_2.items():
        for j, end_coord in table_2.items():
            if i == j:
                precompute[(i, j)] = "A"
            else:
                up_count = max(0, start_coord[0] - end_coord[0])
                down_count = max(0, end_coord[0] - start_coord[0])
                left_count = max(0, start_coord[1] - end_coord[1])
                right_count = max(0, end_coord[1] - start_coord[1])

                def make_paths(uc, dc, lc, rc, current, loc) -> list[str]:
                    if uc + dc + lc + rc == 0:
                        return current

                    ans = []
                    if uc > 0:
                        ans += make_paths(
                            uc - 1,
                            dc,
                            lc,
                            rc,
                            [x + "^" for x in current],
                            (loc[0] - 1, loc[1]),
                        )
                    if dc > 0 and not table[(loc[0] + 1, loc[1])] == "XX":
                        ans += make_paths(
                            uc,
                            dc - 1,
                            lc,
                            rc,
                            [x + "v" for x in current],
                            (loc[0] + 1, loc[1]),
                        )
                    if lc > 0 and not table[(loc[0], loc[1] - 1)] == "XX":
                        ans += make_paths(
                            uc,
                            dc,
                            lc - 1,
                            rc,
                            [x + "<" for x in current],
                            (loc[0], loc[1] - 1),
                        )
                    if rc > 0:
                        ans += make_paths(
                            uc,
                            dc,
                            lc,
                            rc - 1,
                            [x + ">" for x in current],
                            (loc[0], loc[1] + 1),
                        )

                    return ans

                paths = make_paths(
                    up_count, down_count, left_count, right_count, [""], start_coord
                )
                full_paths = [arrowboard_repeat(x + "A", brute_count) for x in paths]

                best = ""
                best_length = 500000000
                for p in full_paths:
                    if len(p) < best_length:
                        best = p
                        best_length = len(p)

                precompute[(i, j)] = best

    return precompute


def keyboard_computataion(code: str, precompute: dict[tuple[str, str], str]):
    pointer = 0
    ans = ""
    code = "A" + code
    while pointer < len(code) - 1:
        ans += precompute[(code[pointer], code[pointer + 1])]
        pointer += 1
    return ans


def arrowboard_extension(code: str) -> str:
    location = "A"
    output = ""

    for val in code:
        if location == val:
            output += "A"
        else:
            output += MOVES[location][val]
        location = val

    return output


def arrowboard_repeat(code: str, count: int) -> str:
    for _ in range(count):
        code = arrowboard_extension(code)
    return code


def depth_size(code, depth) -> int:
    if depth == 0:
        return len(code)

    if code == "A":
        return 1

    if (code, depth) not in depth_chart:
        ans = 0
        pointer = 0
        expansion = arrowboard_extension(code).split("A")

        while pointer < len(expansion) - 1:
            ans += depth_size(expansion[pointer] + "A", depth - 1)
            pointer += 1
        depth_chart[(code, depth)] = ans

    return depth_chart[(code, depth)]


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].strip()
    return inputs_raw


test = ["029A", "980A", "179A", "456A", "379A"]

# part1(file_reader("21_input.txt"), brute_count=2)
part1(file_reader("21_input.txt"), brute_count=4)
# part1(file_reader("21_input.txt"), brute_count=6)
# part1(file_reader("21_input.txt"), brute_count=8)
# part1(test)
# part2(file_reader("21_input.txt"))
# print(keyboard_extension("456A"))
# print(arrowboard_extension(keyboard_extension("456A")))
# print(arrowboard_extension(arrowboard_extension(keyboard_extension("456A"))))
