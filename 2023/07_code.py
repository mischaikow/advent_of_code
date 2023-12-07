from functools import cmp_to_key

def part1(input_list):
  ans = 0

  a_list =[]
  for val in input_list:
    a_list.append((val[0:5], int(val[6:])))
  s_list = sorted(a_list, key=cmp_to_key(hand_compare))

  for i in range(len(s_list)):
    ans += (i+1) * s_list[i][1]

  print(f'Part 1: {ans}')


def hand_compare(hand_1, hand_2):
  hand_1_type = hand_type(hand_1[0])
  hand_2_type = hand_type(hand_2[0])
  if hand_1_type == hand_2_type:
    return hand_close_compare(hand_1[0], hand_2[0])
  return hand_1_type - hand_2_type


def hand_type(a_hand: str):
  ans = 0
  scoring = {
      5: 0, # high card
      7: 1, # one pair
      9: 2, # two pair
      11: 3, # three of a kind
      13: 4, # full house
      17: 5, # four of a kind
      25: 6, # five of a kind
    }

  for card in a_hand:
    ans += a_hand.count(card)

  return scoring[ans]


def hand_close_compare(hand_1: str, hand_2: str) -> bool:
  cards = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
  for i in range(5):
    if hand_1[i] != hand_2[i]:
      if hand_1[i].isdigit():
        h1 = int(hand_1[i])
      else:
        h1 = cards[hand_1[i]]
    
      if hand_2[i].isdigit():
        h2 = int(hand_2[i])
      else:
        h2 = cards[hand_2[i]]

      return h1 - h2


def part2(input_list):
  ans = 0

  a_list =[]
  for val in input_list:
    a_list.append((val[0:5], int(val[6:])))
  s_list = sorted(a_list, key=cmp_to_key(hand_compare_2))

  for i in range(len(s_list)):
    ans += (i+1) * s_list[i][1]

  print(f'Part 2: {ans}')


def hand_compare_2(hand_1, hand_2):
  hand_1_type = hand_type_2(hand_1[0])
  hand_2_type = hand_type_2(hand_2[0])
  if hand_1_type == hand_2_type:
    return hand_close_compare_2(hand_1[0], hand_2[0])
  return hand_1_type - hand_2_type


def hand_type_2(a_hand: str):
  ans = 0
  joker_count = a_hand.count('J')
  scoring = {
      5: 0, # high card
      7: 1, # one pair
      9: 2, # two pair
      11: 3, # three of a kind
      13: 4, # full house
      17: 5, # four of a kind
      25: 6, # five of a kind
    }

  for card in a_hand:
    ans += a_hand.count(card)

  if ans == 5 and joker_count == 1:
    return 1
  if ans == 7 and joker_count > 0:
    return 3
  if ans == 9 and joker_count == 1:
    return 4
  if ans == 9 and joker_count == 2:
    return 5
  if ans == 11 and joker_count > 0:
    return 5
  if ans == 13 and joker_count > 0:
    return 6
  if ans == 17 and joker_count > 0:
    return 6

  return scoring[ans]


def hand_close_compare_2(hand_1: str, hand_2: str) -> bool:
  cards = {'T': 10, 'J': -1, 'Q': 12, 'K': 13, 'A': 14}
  for i in range(5):
    if hand_1[i] != hand_2[i]:
      if hand_1[i].isdigit():
        h1 = int(hand_1[i])
      else:
        h1 = cards[hand_1[i]]
    
      if hand_2[i].isdigit():
        h2 = int(hand_2[i])
      else:
        h2 = cards[hand_2[i]]

      return h1 - h2


def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw

part1(file_reader('07_input.txt'))
part2(file_reader('07_input.txt'))
