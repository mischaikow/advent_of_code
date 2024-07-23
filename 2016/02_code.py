from typing import List

def part1(input_str: List[str]) -> None:
  instruction_map = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
  current_loc = [1, 1]
  location_map = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

  ans = ''
  
  for line in input_str:
    for instruction in line:
      current_loc[0] += instruction_map[instruction][0]
      current_loc[0] = max(0, current_loc[0])
      current_loc[0] = min(2, current_loc[0])
      current_loc[1] += instruction_map[instruction][1]
      current_loc[1] = max(0, current_loc[1])
      current_loc[1] = min(2, current_loc[1])
    ans += location_map[current_loc[0]][current_loc[1]]

  print(f'Part 1: {ans}')


def part2(input_str: List[str]) -> None:
  instruction_map = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
  current_loc = [2, 0]
  location_map = [['NA', 'NA', '1', 'NA', 'NA'], ['NA', '2', '3', '4', 'NA'], ['5', '6', '7', '8', '9'], ['NA', 'A', 'B', 'C', 'NA'], ['NA', 'NA', 'D', 'NA', 'NA']]

  ans = ''

  for line in input_str:
    for instruction in line:
      if 0 <= current_loc[0] + instruction_map[instruction][0] <= 4:
        current_loc[0] += instruction_map[instruction][0]
      if 0 <= current_loc[1] + instruction_map[instruction][1] <= 4:
        current_loc[1] += instruction_map[instruction][1]
      if location_map[current_loc[0]][current_loc[1]] == 'NA':
        if 0 <= current_loc[0] - instruction_map[instruction][0] <= 4:
          current_loc[0] -= instruction_map[instruction][0]
        if 0 <= current_loc[1] - instruction_map[instruction][1] <= 4:
          current_loc[1] -= instruction_map[instruction][1]
    ans += location_map[current_loc[0]][current_loc[1]]

  print(f'Part 2: {ans}')


def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw

#print(file_reader('01_input.txt'))
part1(file_reader('02_input.txt'))
part2(file_reader('02_input.txt'))