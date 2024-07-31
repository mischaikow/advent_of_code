from typing import List

def part1(input_instructions: List[str]) -> None:
  lit = [[0] * 1000 for _ in range(1000)]
  brightness = [[0] * 1000 for _ in range(1000)]
  for instruct in input_instructions:
    # decode -
    k = 2
    if instruct[0] == 'toggle':
      k = 1
    x1, y1 = instruct[k].split(',')
    x2, y2 = instruct[k+2].split(',')
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
      
    # categorize
    if instruct[0] == 'toggle':
      for i in range(x1, x2+1):
        for j in range(y1, y2+1):
          lit[i][j] = (lit[i][j] + 1) % 2
          brightness[i][j] += 2
    elif instruct[1] == 'on':
      for i in range(x1, x2+1):
        for j in range(y1, y2+1):
          lit[i][j] = 1
          brightness[i][j] += 1
    else:
      for i in range(x1, x2+1):
        for j in range(y1, y2+1):
          lit[i][j] = 0
          brightness[i][j] = max(0, brightness[i][j] - 1)

  ans = 0
  for line in lit:
    ans += sum(line)
  print(f'Part 1: {ans}')

  ans = 0
  for line in brightness:
    ans += sum(line)
  print(f'Part 2: {ans}')



def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','').split(' ')
  return inputs_raw

## print(file_reader('06_input.txt'))
part1(file_reader('06_input.txt'))
## print(part2(file_reader('06_input.txt')))