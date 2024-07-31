from typing import List
import json

def part1(accounting_blob: str) -> int:
  ans = 0

  temp = ''
  for letter in accounting_blob:
    if letter.isdigit() or (letter == '-' and temp == ''):
      temp += letter
    else:
      if temp != '':
        ans += int(temp)
        temp = ''

  return ans


def part2(accounting_blob: str):
  data = json.loads(accounting_blob)
  stack = [data]

  ans = 0

  while len(stack) > 0:
    pointer = stack.pop()
    if isinstance(pointer, list):
      stack += pointer
    elif isinstance(pointer, int):
      ans += pointer
    elif isinstance(pointer, dict):
      temp = 0
      temp_stack = []
      for v in pointer.values():
        if v == 'red':
          temp = 0
          temp_stack = []
          break
        if isinstance(v, int):
          temp += v
        elif isinstance(v, list) or isinstance(v, dict):
          temp_stack.append(v)
      stack += temp_stack
      ans += temp

  return ans
  

def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw[0]

## print(file_reader('12_input.txt'))
print(f"Part 1: {part1(file_reader('12_input.txt'))}")
print(f"Part 2: {part2(file_reader('12_input.txt'))}")