def part1():
    key_value = 1133

    ans_1 = [[0] * 300 for _ in range(300)]
    measures = [[0] * 300 for _ in range(300)]

    for x in range(1, 301):
        rack_id = x + 10
        for y in range(1, 301):
            power_level = rack_id * ((y * rack_id) + key_value)
            power_level = ((power_level % 1000) // 100) - 5

            measures[x - 1][y - 1] = power_level

            for dx in range(1, 4):
                for dy in range(1, 4):
                    if x - dx >= 0 and y - dy >= 0:
                        ans_1[x - dx][y - dy] += power_level

    maximum = 0
    final_1 = (1, 1)
    for x in range(len(ans_1) - 3):
        for y in range(len(ans_1) - 3):
            if ans_1[x][y] > maximum:
                final_1 = (x + 1, y + 1)
                maximum = ans_1[x][y]

    print(f"Part 1: {final_1}")

    maximum = 0
    final_2 = (1, 1, 1)
    for x in range(300):
        for y in range(300):
            total = 0
            for i in range(1, 300 - max(x, y)):
                dx = x + i
                for dy in range(y, y + i):
                    total += measures[dx][dy]
                dy = y + i
                for dx in range(x, x + i + 1):
                    total += measures[dx][dy]

                if total > maximum:
                    maximum = total
                    final_2 = (x + 1, y + 1, i + 1)

    print(f"Part 2: {final_2}")


part1()
