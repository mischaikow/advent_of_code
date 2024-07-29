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
  print(data)
  

def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw[0]

## print(file_reader('12_input.txt'))
print(part1(file_reader('12_input.txt')))
print(part2(file_reader('12_input.txt')))