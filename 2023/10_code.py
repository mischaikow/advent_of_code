

def part1(pipe_map):
  i, j = find_s(pipe_map)
  
  if pipe_map[i-1][j] in ['|', '7', 'F']:
    current = [i-1, j, 'S']
  elif pipe_map[i+1][j] in ['|', 'L', 'J']:
    current = [i+1, j, 'N']
  elif pipe_map[i][j-1] in ['-', 'L', 'F']:
    current = [i, j-1, 'E']
  elif pipe_map[i][j+1] in ['-', '7', 'J']:
    current = [i, j+1, 'W']

  ans = 1
  while pipe_map[current[0]][current[1]] != 'S':
    c = pipe_map[current[0]][current[1]]
    current[2] = path_dict[current[2] + c]
    current[0] += delta_dict[current[2]][0]
    current[1] += delta_dict[current[2]][1]
    ans += 1

  print(f'Part 1: {ans//2}')


def part2(pipe_map):
  i, j = find_s(pipe_map)

  connectors = ''
  if pipe_map[i-1][j] in ['|', '7', 'F']:
    current = [i-1, j, 'S']
    connectors += 'S'
  if pipe_map[i+1][j] in ['|', 'L', 'J']:
    current = [i+1, j, 'N']
    connectors += 'N'
  if pipe_map[i][j-1] in ['-', 'L', 'F']:
    current = [i, j-1, 'E']
    connectors += 'E'
  if pipe_map[i][j+1] in ['-', '7', 'J']:
    current = [i, j+1, 'W']
    connectors += 'W'
  pipe_map[i][j] = s_val[connectors]

  last = pipe_map[current[0]][current[1]]
  while not pipe_map[current[0]][current[1]] in ['*', '&', 'U', 'D']:
    c = pipe_map[current[0]][current[1]]
    if c == '|':
      pipe_map[current[0]][current[1]] = '&'
    elif c == 'L' or c == 'J':
      pipe_map[current[0]][current[1]] = 'U'
    elif c == '7' or c == 'F':
      pipe_map[current[0]][current[1]] = 'D'
    else:
      pipe_map[current[0]][current[1]] = '*'
    current[2] = path_dict[current[2] + c]
    current[0] += delta_dict[current[2]][0]
    current[1] += delta_dict[current[2]][1]

  ans = 0

  for line in pipe_map:
    hot = False
    path = 'O'
    for char in line:
      if char == '*':
        pass
      elif char == '&':
        hot = not hot
      elif char == 'U':
        if path == 'D':
          hot = not hot
          path = 'O'
        elif path == 'U':
          path = 'O'
        else:
          path = 'U'
      elif char == 'D':
        if path == 'D':
          path = 'O'
        elif path == 'U':
          hot = not hot
          path = 'O'
        else:
          path = 'D'
      elif hot:
        ans += 1

  print(f'Part 2: {ans}')



def find_s(pipe_map):
  for i in range(len(pipe_map)):
    for j in range(len(pipe_map[i])):
      if pipe_map[i][j] == 'S':
        return (i, j)


path_dict = {
    'S|': 'S',
    'S7': 'E',
    'SF': 'W',
    'N|': 'N',
    'NJ': 'E',
    'NL': 'W',
    'E-': 'E',
    'EF': 'N',
    'EL': 'S',
    'W-': 'W',
    'W7': 'N',
    'WJ': 'S'
  }


delta_dict = {
    'S': [-1, 0],
    'N': [1, 0],
    'E': [0, -1],
    'W': [0, 1]
  }


s_val = {
    'SN': '|',
    'SE': 'J',
    'SW': 'L',
    'NE': '7',
    'NW': 'F',
    'EW': '-'
  }


def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = list(inputs_raw[i].strip())
  return inputs_raw

part1(file_reader('10_input.txt'))
part2(file_reader('10_input.txt'))
