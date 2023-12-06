def part1(input_list):
  times = [int(x) for x in input_list[0].split(':')[1].split()]
  distances = [int(x) for x in input_list[1].split(':')[1].split()]
  ans = 1
  
  for i in range(4):
    temp = 0
    for j in range(times[i]):
      if j * (times[i]-j) > distances[i]:
        temp += 1
    ans *= temp

  print(f'Part 1: {ans}')


def part2(input_list):
  times = [x for x in input_list[0].split(':')[1].split()]
  distances = [x for x in input_list[1].split(':')[1].split()]

  t = int(''.join(times))
  d = int(''.join(distances))

  small = 1
  big = t // 2
  while big > small:
    temp = small + ((big - small) // 2)

    if temp * (t-temp) > d:
      big = temp
    else:
      small = temp + 1

  print(f'Part 2: {t+1 - (2*small)}')


def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw

part1(file_reader('06_input.txt'))
part2(file_reader('06_input.txt'))
