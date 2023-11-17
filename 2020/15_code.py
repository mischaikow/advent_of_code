"""Day 15 of the 2020 Advent of Code

Catching up - helps that I got the algorithm from Part 1 to work for Part 2 :)
"""

def findStep(start, final_step):
    reference = {}
    step = 0
    for value in start:
        step += 1
        reference[value] = step

    next_value = 0
    while step <= final_step + 10:
        if step % 1000000 == 0:
            print(step)
        step += 1
        if next_value in reference:
            next_next_value = step - reference[next_value]
        else:
            next_next_value = 0
        reference[next_value] = step
        next_value = next_next_value
        if step == final_step-1:
            return next_value


def main(start):
    print('Part 1:', findStep(start, 2020))
    print('Part 2:', findStep(start, 30000000))
    return None


main([16,12,1,0,15,7,11])
