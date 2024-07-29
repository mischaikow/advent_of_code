def is_anagram(word_one: str, word_two: str) -> bool:
    if len(word_one) != len(word_two):
        return False

    list_one = sorted(list(word_one))
    list_two = sorted(list(word_two))
    for i in range(len(list_one)):
        if list_one[i] != list_two[i]:
            return False

    return True


def no_anagrams(phrase: str) -> bool:
    for i in range(len(phrase)):
        for j in range(i + 1, len(phrase)):
            if is_anagram(phrase[i], phrase[j]):
                return False

    return True


def part1(passphrases: list[list[str]]) -> None:
    ans_one = 0
    ans_two = 0
    for phrase in passphrases:
        if len(phrase) == len(set(phrase)):
            ans_one += 1
            if no_anagrams(phrase):
                ans_two += 1
    print(f"Part 1: {ans_one}")
    print(f"Part 2: {ans_two}")


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "").split()
    return inputs_raw


# print(file_reader('04_input.txt'))
part1(file_reader("04_input.txt"))
# part2(file_reader("04_input.txt"))
