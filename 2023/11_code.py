

def part1(space_map):

  row_gaps = []
  for i in range(len(space_map)-1, -1, -1):
    is_empty = True
    for char in space_map[i]:
      if char != '.':
        is_empty = False
        break
    if is_empty:
      row_gaps.append(i)

  col_gaps = []
  for j in range(len(space_map[0])-1, -1, -1):
    is_empty = True
    for i in range(len(space_map)-1, -1, -1):
      if space_map[i][j] != '.':
        is_empty = False
        break
    if is_empty:
      col_gaps.append(j)

  for j in col_gaps:
    for i in range(len(space_map)):
      space_map[i].insert(j, '.')
  for i in row_gaps:
    space_map.insert(i, ['.']*len(space_map[0]))

  galaxies = []
  for i in range(len(space_map)):
    for j in range(len(space_map[i])):
      if space_map[i][j] == '#':
        galaxies.append((i, j))

  ans = 0
  for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
      ans += abs(galaxies[i][0] - galaxies[j][0])
      ans += abs(galaxies[i][1] - galaxies[j][1])

  print(f'Part 1: {ans}')


def part2(space_map):
  row_gaps = []
  for i in range(len(space_map)-1, -1, -1):
    is_empty = True
    for char in space_map[i]:
      if char != '.':
        is_empty = False
        break
    if is_empty:
      row_gaps.append(i)

  col_gaps = []
  for j in range(len(space_map[0])-1, -1, -1):
    is_empty = True
    for i in range(len(space_map)-1, -1, -1):
      if space_map[i][j] != '.':
        is_empty = False
        break
    if is_empty:
      col_gaps.append(j)

  galaxies = []
  for i in range(len(space_map)):
    for j in range(len(space_map[i])):
      if space_map[i][j] == '#':
        galaxies.append((i, j))

  ans = 0
  for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
      ans += abs(galaxies[i][0] - galaxies[j][0])
      ans += abs(galaxies[i][1] - galaxies[j][1])
      for x in row_gaps:
        row_1 = galaxies[i][0]
        row_2 = galaxies[j][0]
        if row_1 < x < row_2 or row_2 < x < row_1:
          ans += 999999
      for x in col_gaps:
        col_1 = galaxies[i][1]
        col_2 = galaxies[j][1]
        if col_1 < x < col_2 or col_2 < x < col_1:
          ans += 999999 

  print(f'Part 2: {ans}')


def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = list(inputs_raw[i].strip())
  return inputs_raw

part1(file_reader('11_input.txt'))
part2(file_reader('11_input.txt'))
