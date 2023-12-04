"""
Some fun bunching this together, so I thought I'd refactor and fix some of my
sillier decisions in the process
"""

def both_parts(card_list):
  ans_1 = 0
  counter = [1] * len(card_list)
  for i in range(len(card_list)):
    simple_card = card_list[i][card_list[i].find(':')+1:]
    winners, mine = simple_card.split('|')
    win_list = [int(x) for x in winners.split()]
    my_list = [int(x) for x in mine.split()]
    temp = 0
    for a_num in my_list:
      if a_num in win_list:
        temp += 1
        counter[i + temp] += counter[i]
    if temp > 0:
      ans_1 += 2**(temp-1)

  print(f'Part 1: {ans_1}\nPart 2: {sum(counter)}')


def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw

both_parts(file_reader('04_input.txt'))
