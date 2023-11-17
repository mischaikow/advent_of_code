"""Day 6 of Advent of Code 2020


"""

import re

def readFile(fileName):
    return open(fileName).read().strip().split('\n\n')


def answerCounter(forms):
    count = 0
    for answers in forms:
        letters = set()
        for an_answer in answers:
            if an_answer.islower():
                letters.add(an_answer)
        count += len(letters)
    return count


def answerCounterTwo(forms):
    count = 0
    for answers in forms:
        per_person = re.split('\s', answers)
        common_answers = set(per_person[0])
        if len(per_person) == 1:
            count += len(common_answers)
        else:
            for a_person in per_person[1:]:
                common_answers = common_answers.intersection(a_person)
            count += len(common_answers)
    return count


def main():
    forms = readFile('input_06_1.txt')
    print('Part 1:', answerCounter(forms))
    print('Part 2:', answerCounterTwo(forms))


main()
