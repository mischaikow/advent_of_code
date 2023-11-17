def part1(inputs_raw):
  for i in range(4, len(inputs_raw)):
    if len(inputs_raw[i-4:i]) == len(set(inputs_raw[i-4:i])):
      break

  print(f'Part 1: {i}')

def part2(inputs_raw):
  for i in range(14, len(inputs_raw)):
    if len(inputs_raw[i-14:i]) == len(set(inputs_raw[i-14:i])):
      break

  print(f'Part 2: {i}')

def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw[0]

part1(file_reader('day06input.txt'))
part2(file_reader('day06input.txt'))
