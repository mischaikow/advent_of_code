from collections import deque

import hashlib

OPEN_CODES = {'b', 'c', 'd', 'e', 'f'}
DIRECTIONS = [(-1,0), (1,0), (0,-1), (0,1)]
DIRECTION_NAMES = ['U', 'D', 'L', 'R']

def part1(passcode: str) -> str:
    coordinates = (0, 0, passcode)
    to_visit = deque()
    to_visit.append(coordinates)
    while len(to_visit) > 0:
        coord_vertical, coord_horizontal, code = to_visit.popleft()
        md5hash = hashlib.md5(code.encode("utf-8")).hexdigest()[:4]
        for i in range(4):
            if md5hash[i] in OPEN_CODES:
                new_vertical = coord_vertical + DIRECTIONS[i][0]
                new_horizontal = coord_horizontal + DIRECTIONS[i][1]
                if new_vertical == 3 and new_horizontal == 3:
                    return (code + DIRECTION_NAMES[i])[len(passcode):]
                elif 0 <= new_vertical < 4 and 0 <= new_horizontal < 4:
                    to_visit.append((new_vertical, new_horizontal, code + DIRECTION_NAMES[i]))


    return "ERROR"


def part2(passcode: str) -> str:
    coordinates = (0, 0, passcode)
    to_visit = deque()
    to_visit.append(coordinates)
    ans = 0
    while len(to_visit) > 0:
        coord_vertical, coord_horizontal, code = to_visit.popleft()
        md5hash = hashlib.md5(code.encode("utf-8")).hexdigest()[:4]
        for i in range(4):
            if md5hash[i] in OPEN_CODES:
                new_vertical = coord_vertical + DIRECTIONS[i][0]
                new_horizontal = coord_horizontal + DIRECTIONS[i][1]
                if new_vertical == 3 and new_horizontal == 3:
                    ans = max(ans, len(code) + 1 - len(passcode))
                elif 0 <= new_vertical < 4 and 0 <= new_horizontal < 4:
                    to_visit.append((new_vertical, new_horizontal, code + DIRECTION_NAMES[i]))
    
    return ans



TEST_INPUT_1 = "hijkl"
TEST_INPUT_2 = "ihgpwlah"
TEST_INPUT_3 = "kglvqrro"
TEST_INPUT_4 = "ulqzkmiv"

ACTUAL_INPUT = "njfxhljp"
## print(file_reader("15_input.txt"))
print(f"Part 1: {part1(ACTUAL_INPUT)}")
print(f"Part 2: {part2(ACTUAL_INPUT)}")
## print(f"Part 2: {part2(file_reader('15_input.txt'))}")
