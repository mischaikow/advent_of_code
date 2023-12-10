import math

def part1(input_list):
  ans = 0

  for line in input_list:
    dive = [line]
    while sum(dive[-1]) != 0:
      new_line = []
      for i in range(len(dive[-1])-1):
        new_line.append(dive[-1][i+1] - dive[-1][i])
      dive.append(new_line)

    dive[-1].append(0)
    for i in range(len(dive)-2, -1, -1):
      dive[i].append(dive[i+1][-1] + dive[i][-1])

    ans += dive[0][-1]
  print(dive)

  print(f'Part 1: {ans}')



def part2(input_list):
  ans = 0
  print(f'Part 2: {ans}')



def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
    inputs_raw[i] = [int(x) for x in inputs_raw[i].split()]
  return inputs_raw

example = [
    [0, 3, 6, 9, 12, 15],
    [1, 3, 6, 10, 15, 21],
    [10, 13, 16, 21, 30, 45]]

part1(file_reader('09_input.txt'))
part1(example)
#part2(file_reader('09_input.txt'))
