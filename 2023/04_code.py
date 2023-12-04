def part1(card_list):
  ans = 0
  for val in card_list:
    simple_val = val[val.find(':')+2:]
    win_nums, my_nums = simple_val.split(' | ')
    win_list = pull_numbers(win_nums)
    my_list = pull_numbers(my_nums)
    temp = 0
    for a_num in my_list:
      if a_num in win_list:
        if temp == 0:
          temp = 1
        else:
          temp *= 2
    ans += temp

  print(ans)


def part2(card_list):
  counter = [1] * len(card_list)
  for i in range(len(card_list)):
    if counter[i] == 0:
      break
    simple_val = card_list[i][card_list[i].find(':')+2:]
    win_nums, my_nums = simple_val.split(' | ')
    win_list = pull_numbers(win_nums)
    my_list = pull_numbers(my_nums)
    temp = 0
    for a_num in my_list:
      if a_num in win_list:
        temp += 1
        counter[i + temp] += counter[i]
  print(sum(counter))



def pull_numbers(num_str):
  num_str = num_str.rstrip()
  i = 0
  ans = []
  for i in range(0, len(num_str), 3):
    n = 0
    if num_str[i].isdigit():
      n += 10*int(num_str[i])
    if num_str[i+1].isdigit():
      n += int(num_str[i+1])
    ans.append(n)

  return ans


def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw

part1(file_reader('04_input.txt'))
part2(file_reader('04_input.txt'))
