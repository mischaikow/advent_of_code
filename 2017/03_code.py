def part1(search_value: int) -> int:
    k = 1
    while k**2 < search_value:
        k += 2
    if k**2 - (k - 1) <= search_value:
        # the answer is along the bottom
        return k // 2 + abs(k**2 - search_value - k // 2)
    elif k**2 - (2 * k - 2) <= search_value:
        print(k)
        # the answer is along the left
        return k // 2 + abs(k**2 - (k - 1) - search_value - k // 2)
    elif k**2 - (3 * k - 3) <= search_value:
        # the answer is along the top
        return k // 2 + abs(k**2 - (2 * k - 2) - search_value - k // 2)
    else:
        # the answer is along the right
        return k // 2 + abs(k**2 - (3 * k - 3) - search_value - k // 2)


def part2(search_value: int) -> int:
    the_grid = [[0] * 20 for _ in range(20)]
    x = 10
    y = 10
    the_grid[x][y] = 1
    direction = 0
    direction_table = {"R": (1, 0), "U": (0, 1), "L": (-1, 0), "D": (0, -1)}
    full_neighbors = [
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
    ]
    direction_order = ["R", "U", "L", "D"]
    while True:
        x += direction_table[direction_order[direction]][0]
        y += direction_table[direction_order[direction]][1]
        count = 0
        for ords in full_neighbors:
            if the_grid[x + ords[0]][y + ords[1]] > 0:
                count += 1
                the_grid[x][y] += the_grid[x + ords[0]][y + ords[1]]

        if search_value <= the_grid[x][y]:
            return the_grid[x][y]

        if count < 3:
            direction = (direction + 1) % 4


INPUT_VALUE = 368078
print(f"Part 1: {part1(INPUT_VALUE)}")
print(f"Part 2: {part2(INPUT_VALUE)}")
