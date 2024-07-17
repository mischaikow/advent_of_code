from typing import List

def has_double(a_string: str) -> bool:
  for pointer in range(1, len(a_string)):
    if a_string[pointer-1] == a_string[pointer]:
      return True
  return False


def vowel_counter(a_string: str, count: int) -> bool:
  ans = 0
  vowels = {'a', 'e', 'i', 'o', 'u'}
  for char in a_string:
    if char in vowels:
      ans += 1
      if ans >= count:
        return True
  return False


def special_strings(a_string: str) -> bool:
  if 'ab' in a_string:
    return True
  if 'cd' in a_string:
    return True
  if 'pq' in a_string:
    return True
  if 'xy' in a_string:
    return True
  return False
    

def part1(input_instructions: List[str]):
  ans = 0
  for name in input_instructions:
    if has_double(name) and vowel_counter(name, 3) and not special_strings(name):
      ans += 1
    
  return ans


def double_pair(a_string: str) -> bool:
  for pointer in range(3, len(a_string)):
    if a_string[pointer-3:pointer-1] in a_string[pointer-1:]:
      print(f'{a_string[pointer-3:pointer-1]} from {a_string}')
      return True
  return False


def aba_check(a_string: str) -> bool:
  for pointer in range(2, len(a_string)):
    if a_string[pointer] == a_string[pointer - 2]:
      return True
  return False


def part2(input_instructions: List[str]):
  ans = 0
  for name in input_instructions:
    if double_pair(name) and aba_check(name):
      ans += 1

  return ans


def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw

## print(file_reader('05_input.txt'))
print(part1(file_reader('05_input.txt')))
print(part2(file_reader('05_input.txt')))