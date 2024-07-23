from typing import List

def part1(input_str: List[str]) -> None:
  ans = 0
  for a_line in input_str:
    values = [int(a) for a in a_line if len(a) > 0]
    if values[0] + values[1] > values[2] and values[0] + values[2] > values[1] and values[1] + values[2] > values[0]:
      ans += 1

  print(f'Part 1: {ans}')


def part2(input_str: List[str]) -> None:
  ans = 0
  counter = 0
  while counter < len(input_str):
    line_1 = [int(a) for a in input_str[counter] if len(a) > 0]
    line_2 = [int(a) for a in input_str[counter+1] if len(a) > 0]
    line_3 = [int(a) for a in input_str[counter+2] if len(a) > 0]

    col = []
    for x in range(3):
      col.append([line_1[x], line_2[x], line_3[x]])
    
    for i in range(3):
      if col[i][0] + col[i][1] > col[i][2] and col[i][0] + col[i][2] > col[i][1] and col[i][1] + col[i][2] > col[i][0]:
        ans += 1
    
    counter += 3

  print(f'Part 2: {ans}')


def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','').split(' ')
  return inputs_raw

#print(file_reader('03_input.txt'))
part1(file_reader('03_input.txt'))
part2(file_reader('03_input.txt'))