from typing import List


def part1(input_circuit: List[str]):
  total_string_code = 0
  memory_string = 0
  expanded_string = 0
  for a_line in input_circuit:
    total_string_code += len(a_line)
    expanded_string += 2
    is_escaped = 0
    for a_char in a_line:
      match a_char:
        case "\\":
          expanded_string += 2
          if is_escaped == 0:
            is_escaped = 1 
          elif is_escaped == 1:
            is_escaped = 0
            memory_string += 1
        case '"':
          expanded_string += 2
          if is_escaped == 1:
            is_escaped = 0
            memory_string += 1
        case 'x':
          expanded_string += 1
          if is_escaped == 1:
            is_escaped += 1
          elif is_escaped == 2:
            is_escaped += 1
          elif is_escaped == 3:
            is_escaped = 0
            memory_string += 1
          else:
            memory_string += 1
        case _:
          expanded_string += 1
          if is_escaped == 1:
            is_escaped = 0
            memory_string += 2
          elif is_escaped == 2:
            is_escaped += 1
          elif is_escaped == 3:
            is_escaped = 0
            memory_string += 1
          else:
            memory_string += 1

  print(f'Part 1: {total_string_code - memory_string}')
  print(f'Part 2: {expanded_string - total_string_code}')


def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw

## print(file_reader('08_input.txt'))
part1(file_reader('08_input.txt'))