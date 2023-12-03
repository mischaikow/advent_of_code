"""
I didn't like how sloppy my code was last night, and for some reason my vim
had changed the formatting to 4 spaces instead of 2. In an effort to understand
some other potential approaches I'm just going to refine my code a bit.
"""

def part1(str_list):
  ans = 0

  for i in range(len(str_list)):
    j = 0
    while j < len(str_list[0]):
      if str_list[i][j].isdigit():
        # If we find a number, we should check if we include it
        is_hot = False
        number = 0
        while j < len(str_list[0]) and str_list[i][j].isdigit():
          number = number*10 + int(str_list[i][j])
          is_hot = is_hot or check_surroundings(str_list, i, j)
          j += 1
        if is_hot:
          ans += number
      j += 1

  print(ans)


def part2(str_list):
  ans = 0

  for i in range(len(str_list)):
    for j in range(len(str_list[0])):
      if str_list[i][j] == '*':
        values = []

        for di in [-1, 1]:
          if 0 <= i + di < len(str_list):
            if str_list[i + di][j].isdigit():
              values.append(pull_number(str_list, i+di, j))
            else:
              # If the char right above the * isn't a number, check the chars
              #  immediately before and after.
              for dj in [-1, 1]:
                if 0 <= j + dj < len(str_list[0]):
                  if str_list[i + di][j + dj].isdigit():
                    values.append(pull_number(str_list, i+di, j+dj))
        # Finally check the chars to the immediate left and right of the *
        for dj in [-1, 1]:
          if 0 <= j + dj < len(str_list[0]) and str_list[i][j+dj].isdigit():
            values.append(pull_number(str_list, i, j+dj))
        
        if len(values) == 2:
          ans += values[0] * values[1]

  print(ans)


def pull_number(str_list, i, j):
  while j > 0 and str_list[i][j-1].isdigit():
    j -= 1

  ans = 0
  while j < len(str_list[0]) and str_list[i][j].isdigit():
    ans = ans*10 + int(str_list[i][j])
    j += 1

  return ans


def check_is_symbol(a_char):
  if a_char.isdigit():
    return False
  if a_char == '.':
    return False
  return True


def check_surroundings(str_list, i, j):
  for di in [-1, 0, 1]:
    for dj in [-1, 0, 1]:
      if 0 <= i + di < len(str_list) and \
          0 <= j + dj < len(str_list[0]) and \
          check_is_symbol(str_list[i + di][j + dj]):
        return True
  return False
    

def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw

part1(file_reader('03_input.txt'))
part2(file_reader('03_input.txt'))
