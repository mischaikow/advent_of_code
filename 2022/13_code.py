def ordered(sig_one, sig_two):

  return True


def part1(inputs_raw):
  ans = 0

  index = 1
  row = 0

  while row < len(inputs_raw):
    sig_one = inputs_raw[row]
    sig_two = inputs_raw[row + 1]

    if ordered(sig_one, sig_two):
      ans += index

    row += 3
    index += 1

  print(f'Part 1: {ans}')


def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw


part1(file_reader('day13input.txt'))