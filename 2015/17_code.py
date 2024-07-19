from typing import List, Dict
from collections import defaultdict


def merge_dicts(dict_one, dict_two):
  all_the_keys = set()
  for key_one in dict_one.keys():
    all_the_keys.add(key_one)
  for key_two in dict_two.keys():
    all_the_keys.add(key_two)

  new_dict = defaultdict(int)
  for a_key in all_the_keys:
    new_dict[a_key] = dict_one[a_key] + dict_two[a_key]
  return new_dict


def part1(input_containers: List[int], target: int) -> int:
  # now to iterate through every possible order...
  used = [0 for _ in range(len(input_containers))]
  def container_combos(current: int, total_volume: int) -> Dict[int, int]:
    recorded_combos = defaultdict(int)
    for pointer in range(current+1, len(used)):
      if used[pointer] == 0:
        used[pointer] = 1
        if total_volume + input_containers[pointer] == target:
          recorded_combos[sum(used)] += 1
        else:
          recorded_combos = merge_dicts(recorded_combos, container_combos(pointer, total_volume + input_containers[pointer]))
        used[pointer] = 0
    return recorded_combos 

  ## for part 1, change the second 0 to ans
  ans = 0
  low_ans = target
  low_count = target
  working_combos = container_combos(-1, 0)
  print(working_combos)
  for key, value in working_combos.items():
    ans += value
    if key < low_count:
      low_ans = value
      low_count = key

  print(f'Part 1: {ans}')
  print(f'Part 2: {low_ans}')


def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = int(inputs_raw[i].replace('\n',''))
  return inputs_raw

## print(file_reader('17_input.txt'))
part1(file_reader('17_input.txt'), 150)
## print(part2(file_reader('17_input.txt')))