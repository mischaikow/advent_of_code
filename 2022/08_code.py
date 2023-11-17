def part1(inputs_raw):
  visible = [[0] * len(inputs_raw[0]) for _ in inputs_raw]
  visible[0] = [1] * len(inputs_raw[0])
  visible[-1] = [1] * len(inputs_raw[0])
  for i in range(len(inputs_raw)):
    visible[i][0] = 1
    visible[i][-1] = 1

  for i in range(1, len(inputs_raw)-1):
    max = inputs_raw[i][0]
    for j in range(1, len(inputs_raw[0])-1):
      if inputs_raw[i][j] > max:
        visible[i][j] = 1
        max = inputs_raw[i][j]

  for i in range(1, len(inputs_raw)-1):
    max = inputs_raw[i][-1]
    for j in range(len(inputs_raw[0])-1, 0, -1):
      if inputs_raw[i][j] > max:
        visible[i][j] = 1
        max = inputs_raw[i][j]

  for j in range(1, len(inputs_raw[0])-1):
    max = inputs_raw[0][j]
    for i in range(1, len(inputs_raw)-1):
      if inputs_raw[i][j] > max:
        visible[i][j] = 1
        max = inputs_raw[i][j]

  for j in range(1, len(inputs_raw[0])-1):
    max = inputs_raw[-1][j]
    for i in range(len(inputs_raw)-1, 0, -1):
      if inputs_raw[i][j] > max:
        visible[i][j] = 1
        max = inputs_raw[i][j]

  ans = 0
  for row in visible:
    ans += sum(row)

  print(f'Part 1: {ans}')


def part2(inputs_raw):
  directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

  ans = 0
  for i in range(1, len(inputs_raw)-1):
    for j in range(1, len(inputs_raw[0])-1):
      house = 1
      for step in directions:
        k = i
        l = j
        count = 0
        while 0 < k < len(inputs_raw)-1 and 0 < l < len(inputs_raw)-1:
          k += step[0]
          l += step[1]
          count += 1
          if inputs_raw[i][j] <= inputs_raw[k][l]:
            break
        house *= count
      if house > ans:
        ans = house

  print(f'Part 2: {ans}')


def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
    inputs_raw[i] = [int(_) for _ in inputs_raw[i]]
  return inputs_raw

part1(file_reader('day08input.txt'))
part2(file_reader('day08input.txt'))
