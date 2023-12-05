def part1(card_list):
  print(f'Part 1: {ans}')


def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw

part1(file_reader('05_input.txt'))
#part2(file_reader('05_input.txt'))
