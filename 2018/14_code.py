def part1(target: int) -> str:
    baseline = [3, 7]
    elf_1 = 0
    elf_2 = 1

    target_char_length = len(str(target))

    while True:
        score_1 = baseline[elf_1]
        score_2 = baseline[elf_2]

        new_score = score_1 + score_2
        if new_score > 9:
            baseline.append(1)
        baseline.append(new_score % 10)

        elf_1 = (elf_1 + score_1 + 1) % len(baseline)
        elf_2 = (elf_2 + score_2 + 1) % len(baseline)

        if new_score > 9:
            last_7_minus_1 = "".join(
                [str(x) for x in baseline[-1 * target_char_length - 1 : -1]]
            )
            if int(last_7_minus_1) == target:
                print(f"Part 2: {len(baseline) - target_char_length - 1}")
                break

        last_6 = "".join([str(x) for x in baseline[-1 * target_char_length :]])
        if int(last_6) == target:
            print(f"Part 2: {len(baseline) - target_char_length}")
            break

    result = "".join([str(x) for x in baseline[target : target + 10]])
    print(f"Part 1: {result}")


part1(330_121)
