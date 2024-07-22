from typing import List

def part1(input_str: List[str]) -> None:
  direction = 0
  direction_map = [(1, 0), (0, 1), (-1, 0), (0, -1)]
  current_loc = [0, 0]
  visited = set()
  overlapped = False

  for instruction in input_str:
    if instruction[0] == 'R':
      direction = (direction + 1) % 4
    elif instruction[0] == 'L':
      direction = (direction - 1) % 4
    else:
      print('error?')

    for _ in range(int(instruction[1:])):
      current_loc[0] += direction_map[direction][0]
      current_loc[1] += direction_map[direction][1]

      if (current_loc[0], current_loc[1]) in visited and not overlapped:
        print(f'Part 2: {abs(current_loc[0]) + abs(current_loc[1])}')
        overlapped = True
      else:
        visited.add((current_loc[0], current_loc[1]))


  print(f'Part 1: {abs(current_loc[0]) + abs(current_loc[1])}')
  return


def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','').split(', ')
  return inputs_raw[0]

#print(file_reader('01_input.txt'))
part1(file_reader('01_input.txt'))
#print(part2(file_reader('01_input.txt')))