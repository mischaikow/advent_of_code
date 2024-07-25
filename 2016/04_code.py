from typing import List, Dict
from collections import defaultdict

def compare_checksum(checksum: str, counted_char: Dict[int, List[str]], count_list: List[int]) -> bool:
  pointer = 0
  for value in count_list:
    counted_char[value].sort()
    for elem in counted_char[value]:
      if checksum[pointer] == elem:
        pointer += 1
        if pointer == 5:
          return True
      else:
        return False
  return False


def decrypt_bunny(sector_id: int, front_list: List[str]) -> str:
  rotate = sector_id % 26
  ans = ''
  
  for batch in front_list:
    for character in batch:
      projected_ord = ord(character) + rotate
      if projected_ord > ord('z'):
        projected_ord -= 26
      ans += chr(projected_ord)
    ans += ' '
  return ans[:-1]
  


def part1(input_str: List[str]) -> None:
  ans = 0
  for line in input_str:
    front, checksum = line[:-1].split('[')
    front_list = front.split('-')
    sector_id = int(front_list.pop())
    e_name = ''.join(front_list)

    char_count = defaultdict(int)
    for char in e_name:
      char_count[char] += 1

    counted_char = dict()
    for key, value in char_count.items():
      if value in counted_char:
        counted_char[value].append(key)
      else:
        counted_char[value] = [key]

    count_list = list(counted_char.keys())
    count_list.sort(reverse=True)

    if compare_checksum(checksum, counted_char, sorted(count_list, reverse=True)):
      ans += sector_id
      if decrypt_bunny(sector_id, front_list) == 'northpole object storage':
        print(f'Part 2: {sector_id}')

  print(f'Part 1: {ans}')
  return



def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw

test_input = ['aaaaa-bbb-z-y-x-123[abxyz]', 'a-b-c-d-e-f-g-h-987[abcde]', 'not-a-real-room-404[oarel]', 'totally-real-room-200[decoy]']

#print(file_reader('04_input.txt'))
#part1(test_input)
part1(file_reader('04_input.txt'))
#part2(file_reader('04_input.txt'))