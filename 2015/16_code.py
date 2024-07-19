from typing import List, Dict


def special_multiply(values: List[int]) -> int:
  ans = 1
  for v in values:
    if v > 0:
      ans *= v
    else:
      return 0
  return ans


def part1(all_sues: List[str], sue_facts: Dict) -> int:
  for a_sue_str in all_sues:
    a_sue_raw = a_sue_str.split()
    a_sue = [a.replace(':', '').replace(',', '') for a in a_sue_raw]
    if sue_facts[a_sue[2]] == int(a_sue[3]) and sue_facts[a_sue[4]] == int(a_sue[5]) and sue_facts[a_sue[6]] == int(a_sue[7]):
      print(f'Part 1: {a_sue[1]}')
      break


def mfcsam_limits(facts: List[str], sue_facts: Dict) -> bool:
  for i in [0, 2, 4]:
    match facts[i]:
      case 'cats' | 'trees':
        if sue_facts[facts[i]] >= int(facts[i+1]):
          return False
      case 'pomeranians' | 'goldfish':
        if sue_facts[facts[i]] <= int(facts[i+1]):
          return False
      case other:
        if sue_facts[facts[i]] != int(facts[i+1]):
          return False

  return True


def part2(all_sues: List[str], sue_facts: Dict) -> int:
  for a_sue_str in all_sues:
    a_sue_raw = a_sue_str.split()
    a_sue = [a.replace(':', '').replace(',', '') for a in a_sue_raw]
    if mfcsam_limits(a_sue[2:], sue_facts):
      print(f'Part 1: {a_sue[1]}')
      break


def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw


sue_facts = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

## print(file_reader('15_input.txt'))
part1(file_reader('16_input.txt'), sue_facts)
part2(file_reader('16_input.txt'), sue_facts)