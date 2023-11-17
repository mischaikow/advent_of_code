def part1(str_val_arr):
  big_elf = 0
  temp = 0
  for val in str_val_arr:
    if val == '':
      if temp > big_elf:
        big_elf = temp
      temp = 0
    else:
      temp += int(val)
  print(f'Part 1: {max(big_elf, temp)}')

def part2(str_val_arr):
  big_elves = [0,0,0]
  smallest = 0
  temp = 0
  for val in str_val_arr:
    if val == '':
      if temp > big_elves[smallest]:
        big_elves[smallest] = temp
      if big_elves[0] <= big_elves[1] and big_elves[0] <= big_elves[2]:
        smallest = 0
      elif big_elves[1] <= big_elves[2] and big_elves[1] <= big_elves[2]:
        smallest = 1
      else:
        smallest = 2
      temp = 0
    else:
      temp += int(val)

  if temp > big_elves[smallest]:
    big_elves[smallest] = temp

  print(f'Part 2: {sum(big_elves)}')



def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw

part1(file_reader('day01input.txt'))
part2(file_reader('day01input.txt'))
