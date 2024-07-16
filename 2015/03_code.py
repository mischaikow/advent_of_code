from collections import defaultdict

def part1(input_instructions: str):
  loc = (0, 0)
  visited = defaultdict(int)
  visited[loc] += 1
  for val in input_instructions:
    if val == '^':
      loc = (loc[0], loc[1]+1)
    elif val == 'v':
      loc = (loc[0], loc[1]-1)
    elif val == '<':
      loc = (loc[0]-1, loc[1])
    elif val == '>':
      loc = (loc[0]+1, loc[1])
    visited[loc] += 1

  return len(visited) 

def part2(input_instructions: str):
  santa_loc = (0,0)
  robo_loc = (0,0)
  visited = set()
  visited.add(santa_loc)

  is_santa = True
  for val in input_instructions:
    if is_santa:
      loc = santa_loc
    else:
      loc = robo_loc

    if val == '^':
      loc = (loc[0], loc[1]+1)
    elif val == 'v':
      loc = (loc[0], loc[1]-1)
    elif val == '<':
      loc = (loc[0]-1, loc[1])
    elif val == '>':
      loc = (loc[0]+1, loc[1])

    visited.add(loc)

    if is_santa:
      santa_loc = loc
    else:
      robo_loc = loc

    is_santa = not is_santa
    

  return len(visited)



def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw[0]

## print(file_reader('03_input.txt'))
print(part1(file_reader('03_input.txt')))
print(part2(file_reader('03_input.txt')))