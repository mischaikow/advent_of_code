def part1(inputs_raw):
  ans = 0
  game_swap = {
    "X": "A",
    "Y": "B",
    "Z": "C"
  }

  for game in inputs_raw:
    g = game[:1] + game_swap[game[2]]
    ans += score(g)

  print(f'Part 1: {ans}')


def score(game):
  ans = 0
  if game[1] == 'A':
    ans += 1
  elif game[1] == 'B':
    ans += 2
  elif game[1] == 'C':
    ans += 3

  if game in {'AA', 'BB', 'CC'}:
    ans += 3
  elif game in {'AB', 'BC', 'CA'}:
    ans += 6

  return ans


def part2(inputs_raw):
  ans = 0
  game_ans = {
    'A X': 3,
    'A Y': 4,
    'A Z': 8,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 2,
    'C Y': 6,
    'C Z': 7,
  }

  for game in inputs_raw:
    ans += game_ans[game]

  print(f'Part 2: {ans}')
  

def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw

part1(file_reader('day02input.txt'))
part2(file_reader('day02input.txt'))
