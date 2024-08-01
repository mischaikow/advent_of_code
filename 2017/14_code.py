def list_flip(a_list, start, length) -> None:
    for loc in range(length // 2):
        (
            a_list[(start + loc) % len(a_list)],
            a_list[(start + length - 1 - loc) % len(a_list)],
        ) = (
            a_list[(start + length - 1 - loc) % len(a_list)],
            a_list[(start + loc) % len(a_list)],
        )


def knot_hash(raw_string: str) -> str:
    input_lengths = []
    for character in raw_string:
        input_lengths.append(ord(character))
    input_lengths += [17, 31, 73, 47, 23]

    circle = [x for x in range(256)]
    counter = 0
    pointer = 0

    for _ in range(64):
        for length in input_lengths:
            list_flip(circle, pointer, length)
            pointer = (pointer + length + counter) % len(circle)
            counter += 1

    # shrink the circle
    hex_string = ""
    for i in range(16):
        n = 0
        for j in range(16):
            n ^= circle[16 * i + j]
        n_hex = hex(n)[2:]
        if len(n_hex) == 1:
            n_hex = "0" + n_hex
        hex_string += n_hex

    return hex_string


def hex_to_binary(hex_string: str) -> str:
    ans = ""
    for a_char in hex_string:
        ans += format(a_char, "b")[-4:]
    return ans


def part1(key: str) -> None:
    grid = []
    ans_one = 0
    for x in range(128):
        grid.append([])
        start = key + "-" + str(x)
        hex_hash = int(knot_hash(start), 16)
        binary_hash = f"{hex_hash:0>128b}"
        for a_char in binary_hash:
            ans_one += int(a_char)
            grid[-1].append(int(a_char))

    ordinals = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[0] * 128 for _ in range(128)]
    ans_two = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if visited[i][j] == 0 and grid[i][j] == 1:
                ans_two += 1
                to_visit = [(i, j)]
                while len(to_visit) > 0:
                    current = to_visit.pop()
                    for direction in ordinals:
                        new_i = current[0] + direction[0]
                        new_j = current[1] + direction[1]
                        if (
                            0 <= new_i < len(grid)
                            and 0 <= new_j < len(grid)
                            and visited[new_i][new_j] == 0
                            and grid[new_i][new_j] == 1
                        ):
                            visited[new_i][new_j] = 1
                            to_visit.append((new_i, new_j))

    print(f"Part 1: {ans_one}")
    print(f"Part 2: {ans_two}")


TEST_KEY = "flqrgnkx"
ACTUAL_KEY = "wenycdww"
part1(ACTUAL_KEY)
