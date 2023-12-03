def part1(game_list):
  maximum = {
      'red': 12,
      'green': 13,
      'blue': 14
      }

  ans = 0
  for i in range(len(game_list)):
    is_possible = True
    short_string = game_list[i][game_list[i].find(':') + 2:]
    draw_list = short_string.split(';')
    for a_draw in draw_list:
      balls = a_draw.split(',')
      for a_ball in balls:
        a_ball = a_ball.strip()
        a_count, a_color = sep(a_ball)
        if a_count > maximum[a_color]:
          is_possible = False

    if is_possible:
      ans += i+1
   
  print(ans)


def part2(game_list):
  ans = 0
  for i in range(len(game_list)):
    short_string = game_list[i][game_list[i].find(':') + 2:]
    draw_list = short_string.split(';')
    count = {
        'red': 0,
        'green': 0,
        'blue': 0
        }

    for a_draw in draw_list:
      balls = a_draw.split(',')
      for a_ball in balls:
        a_ball = a_ball.strip()
        a_count, a_color = sep(a_ball)
        if a_count > count[a_color]:
          count[a_color] = a_count

    temp = 1
    for _, val in count.items():
      temp *= val
    ans += temp

  print(ans)


def sep(a_ball: str):
  i = 0
  count = 0
  while a_ball[i].isdigit():
    count = count*10 + int(a_ball[i])
    i += 1
  return count, a_ball[i+1:]



def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw

part1(file_reader('02_input.txt'))
part2(file_reader('02_input.txt'))
