from typing import List


def part1(input_circuit: List[str]):
  circuit = dict()
  computed = dict()
  for connection in input_circuit:
    instruct, dest = connection.split(' -> ')
    circuit[dest] = instruct

  def operate(point):
    if point.isdigit():
      return int(point)
    if point in computed:
      return computed[point]

    instruct = circuit[point]
    
    if 'NOT' in instruct:
      _, val = instruct.split(' ')
      answer = operate(val) ^ 65535

    elif 'AND' in instruct:
      val_1, val_2 = instruct.split(' AND ')
      answer = operate(val_1) & operate(val_2)

    elif 'OR' in instruct:
      val_1, val_2 = instruct.split(' OR ')
      answer = operate(val_1) | operate(val_2)

    elif 'LSHIFT' in instruct:
      val_1, val_2 = instruct.split(' LSHIFT ')
      answer = operate(val_1) << int(val_2)
    
    elif 'RSHIFT' in instruct:
      val_1, val_2 = instruct.split(' RSHIFT ')
      answer = operate(val_1) >> int(val_2)

    else:
      answer = operate(instruct)

    computed[point] = answer
    return answer

  return operate('a')


def part2(input_circuit: List[str]):
  circuit = dict()
  computed = dict()
  computed['b'] = part1(file_reader('07_input.txt'))
  for connection in input_circuit:
    instruct, dest = connection.split(' -> ')
    circuit[dest] = instruct

  def operate(point):
    if point.isdigit():
      return int(point)
    if point in computed:
      return computed[point]

    instruct = circuit[point]
    
    if 'NOT' in instruct:
      _, val = instruct.split(' ')
      answer = operate(val) ^ 65535

    elif 'AND' in instruct:
      val_1, val_2 = instruct.split(' AND ')
      answer = operate(val_1) & operate(val_2)

    elif 'OR' in instruct:
      val_1, val_2 = instruct.split(' OR ')
      answer = operate(val_1) | operate(val_2)

    elif 'LSHIFT' in instruct:
      val_1, val_2 = instruct.split(' LSHIFT ')
      answer = operate(val_1) << int(val_2)
    
    elif 'RSHIFT' in instruct:
      val_1, val_2 = instruct.split(' RSHIFT ')
      answer = operate(val_1) >> int(val_2)

    else:
      answer = operate(instruct)

    computed[point] = answer
    return answer

  return operate('a')


def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw

## print(file_reader('07_input.txt'))
print(part1(file_reader('07_input.txt')))
print(part2(file_reader('07_input.txt')))