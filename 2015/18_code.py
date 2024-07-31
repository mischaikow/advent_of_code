def part1(starting_state: list[str]) -> int:
  lightboard = []
  for a_line in starting_state:
    lightboard.append([])
    for char in a_line:
      if char == '#':
        lightboard[-1].append(1)
      else:
        lightboard[-1].append(0)

  STEP_COUNT = 100
  CYCLE = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
  for _ in range(STEP_COUNT):
    new_lightboard = []
    for i in range(len(lightboard)):
      new_lightboard.append([])
      for j in range(len(lightboard[0])):
        # for part 1, switch out the if statement:
        # if False:
        if (i == 0 or i == len(lightboard)-1) and (j == 0 or j == len(lightboard)-1):
          new_lightboard[-1].append(1)
        else:
          counter = 0
          for direction in CYCLE:
            if -1 < i + direction[0] < len(lightboard) and -1 < j + direction[1] < len(lightboard[0]):
              counter += lightboard[i+direction[0]][j+direction[1]]
          if lightboard[i][j] == 1 and (counter == 2 or counter == 3):
            new_lightboard[-1].append(1)
          elif lightboard[i][j] == 0 and counter == 3:
            new_lightboard[-1].append(1)
          else:
            new_lightboard[-1].append(0)
    lightboard = new_lightboard
    

  ans = 0
  for line in lightboard:
    ans += sum(line)
  print(f'Part 1: {ans}')


def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw

## print(file_reader('18_input.txt'))
part1(file_reader('18_input.txt'))
## print(part2(file_reader('18_input.txt')))