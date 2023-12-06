from collections import deque

def part1(input_list):
  loc_list = []

  seeds = [int(x) for x in input_list[0][input_list[0].find(':')+2:].split()]
  for a_seed in seeds:
    loc_list += map_seed_1(a_seed, input_list[1:])

  print(f'Part 1: {min(loc_list)}')


def map_seed_1(x, map_list):
  i = 2
  p = 0
  while i < len(map_list):
    while i < len(map_list) and map_list[i] != '':
      values = [int(z) for z in map_list[i].split()]
      if values[1] <= x < values[1]+values[2]:
        x = (x - values[1]) + values[0]
        break
      i += 1

    while i < len(map_list) and map_list[i] != '':
      i += 1
    i += 2

  return [x]


def part2(input_list):
  seeds_raw = [int(x) for x in input_list[0][input_list[0].find(':')+2:].split()]
  i = 0
  locs = []
  while i < len(seeds_raw):
    locs.append((seeds_raw[i], seeds_raw[i]+seeds_raw[i+1]))
    i += 2

  locs_next = []
  for line in input_list[1:]:
    print(len(locs + locs_next))
    if line == '':
      locs += locs_next
      locs_next = []

    elif line[0].isdigit():
      temp = []
      values_raw = [int(x) for x in line.split()]
      for bloc in locs:
        if bloc[0] > values_raw[1] + values_raw[2] or bloc[1] < values_raw[1]:
          temp.append(bloc)
        else:
          if bloc[0] < values_raw[1]:
            temp.append((bloc[0], values_raw[1]-1))
          if bloc[1] > values_raw[1] + values_raw[2]:
            temp.append((values_raw[1] + values_raw[2], bloc[1]))
          convert = (
              max(0, bloc[0]-values_raw[1]) + values_raw[0],
              min(bloc[1]-values_raw[1], values_raw[2]) + values_raw[0]
              )
          locs_next.append(convert)
      locs = temp

  print(min(locs + locs_next))


def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw

part1(file_reader('05_input.txt'))
part2(file_reader('05_input.txt'))
