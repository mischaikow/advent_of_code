from typing import List

def part1(legal_transforms: List[str]) -> None:
  transforms = dict()
  for a_t in legal_transforms:
    if '=>' in a_t:
      input_value, output_value = a_t.split(' => ')
      if not input_value in transforms:
        transforms[input_value] = [output_value]
      else:
        transforms[input_value].append(output_value)
    elif len(a_t) > 2:
      target_compound = a_t

  pointer = 0
  compounds = set()
  while pointer < len(target_compound):
    chem = target_compound[pointer]
    chem_length = 1
    if (not target_compound[pointer] == 'e') and pointer+1 < len(target_compound) and target_compound[pointer+1].islower():
      chem = target_compound[pointer:pointer+2]
      chem_length = 2

    if chem in transforms:
      for swap_chem in transforms[chem]:
        new_chem = target_compound[:pointer] + swap_chem + target_compound[pointer+chem_length:]
        compounds.add(new_chem)

    pointer += chem_length
  print(f'Part 1: {len(compounds)}')


def part2(legal_transforms: List[str]) -> None:
  transforms = dict()
  for a_t in legal_transforms:
    if '=>' in a_t:
      input_value, output_value = a_t.split(' => ')
      transforms[output_value] = input_value
    elif len(a_t) > 2:
      target_compound = a_t


  reductors = [a for a in transforms.keys()]
  reductors.sort(key=len)

  visited = set()
  stack = [(target_compound, 0)]

  while True:
    current_compound, depth = stack.pop()
    visited.add(current_compound)

    for mini_compound in reductors:
      a_compound = current_compound.replace(mini_compound, transforms[mini_compound], 1)
      if a_compound == 'e':
        print(f'Part 2: {depth+1}')
        return
        
      if not a_compound in visited:
        stack.append((a_compound, depth+1))



def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw

part1(file_reader('19_input.txt'))
part2(file_reader('19_input.txt'))