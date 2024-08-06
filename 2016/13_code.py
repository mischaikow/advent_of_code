from collections import deque, defaultdict


def is_open_space(x: int, y: int, favorite: int) -> int:
  encoding = x*x + 3*x + 2*x*y + y + y*y + favorite
  ans = 0
  while encoding > 0:
    if encoding % 2 == 1:
      encoding -= 1
      ans += 1
    encoding >>= 1

  return ans % 2 == 0


def part1(designers_favorite_number: int, target: tuple[int, int]) -> int:
  locations = deque()
  locations.append(((1, 1, 0)))
  visited = set()

  compass = [(0, 1), (1, 0), (0, -1), (-1, 0)]

  while len(locations) > 0:
    point = deque.popleft(locations)
    if point[0] == target[0] and point[1] == target[1]:
      return point[2]

    if not (point[0], point[1]) in visited:
      visited.add(((point[0], point[1])))
      for direction in compass:
        if 0 <= point[0] + direction[0] and 0 <= point[1] + direction[1] and is_open_space(point[0] + direction[0], point[1] + direction[1], designers_favorite_number):
          locations.append(((point[0] + direction[0], point[1] + direction[1], point[2] + 1)))




def part2(designers_favorite_number: int) -> int:
  locations = deque()
  locations.append(((1, 1, 0)))
  visited = set()

  compass = [(0, 1), (1, 0), (0, -1), (-1, 0)]

  while len(locations) > 0:
    point = deque.popleft(locations)
    if not (point[0], point[1]) in visited and point[2] < 51:
      visited.add(((point[0], point[1])))
      for direction in compass:
        if 0 <= point[0] + direction[0] and 0 <= point[1] + direction[1] and is_open_space(point[0] + direction[0], point[1] + direction[1], designers_favorite_number):
          locations.append(((point[0] + direction[0], point[1] + direction[1], point[2] + 1)))
  
  return len(visited)


TEST_INPUT = 10
TEST_TARGET = (7, 4)
ACTUAL_INPUT = 1350
ACTUAL_TARGET = (31, 39)
ans_part1 = part1(ACTUAL_INPUT, ACTUAL_TARGET)
print(f'Part 1: {ans_part1}')
ans_part2 = part2(ACTUAL_INPUT)
print(f'Part 2: {ans_part2}')

