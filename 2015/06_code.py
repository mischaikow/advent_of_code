from typing import List

def part1(input_instructions: List[str]) -> int:
  lit = []

  for instruct in input_instructions:
    # categorize
    if instruct[0] == 'toggle':
      pass
    elif instruct[1] == 'on':
      x1, y1 = instruct[2].split(',')
      x2, y2 = instruct[4].split(',')
      x1 = int(x1)
      x2 = int(x2)
      y1 = int(y1)
      y2 = int(y2)
      for spot in lit:



    elif instruct[2] == 'off':
      pass



  return 0



def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','').split(' ')
  return inputs_raw

## print(file_reader('06_input.txt'))
print(part1(file_reader('06_input.txt')))
## print(part2(file_reader('06_input.txt')))