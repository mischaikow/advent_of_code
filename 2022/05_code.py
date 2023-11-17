### I'm not proud of it, but it worked on the first try...

def part1(inputs_raw):
  ship = [[] for _ in range(9)]
  for i in range(7, -1, -1):
    for j in range(1, 37, 4):
      if inputs_raw[i][j] != ' ':
        ship[(j-1)//4].append(inputs_raw[i][j])

  for i in range(10, len(inputs_raw)):
    count = int(inputs_raw[i][5:7])
    if count < 10:
      start = inputs_raw[i][12]
      end = inputs_raw[i][17]
    else:
      start = inputs_raw[i][13]
      end = inputs_raw[i][18]

    for j in range(int(count)):
      ship[int(end)-1].append(ship[int(start)-1].pop())

  result = ''
  for i in range(len(ship)):
    result += ship[i].pop()
    
  print(f'Part 1: {result}')

def part2(inputs_raw):
  ship = [[] for _ in range(9)]
  for i in range(7, -1, -1):
    for j in range(1, 37, 4):
      if inputs_raw[i][j] != ' ':
        ship[(j-1)//4].append(inputs_raw[i][j])

  for i in range(10, len(inputs_raw)):
    count = int(inputs_raw[i][5:7])
    if count < 10:
      start = inputs_raw[i][12]
      end = inputs_raw[i][17]
    else:
      start = inputs_raw[i][13]
      end = inputs_raw[i][18]

    temp = []
    for j in range(int(count)):
      temp.append(ship[int(start)-1].pop())
    for j in range(int(count)):
      ship[int(end)-1].append(temp.pop())

  result = ''
  for i in range(len(ship)):
    result += ship[i].pop()
    
  print(f'Part 2: {result}')


def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw


part1(file_reader('day05input.txt'))
part2(file_reader('day05input.txt'))
