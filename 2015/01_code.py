
def part1(input_str: str):
  ans = 0
  for c in input_str:
    if c == '(':
      ans += 1
    else:
      ans -= 1
  return ans

def part2(input_str: str):
  counter = 0
  ans = 0
  for c in input_str:
    if c == '(':
      ans += 1
    else:
      ans -= 1
    counter += 1
    
    if ans == -1:
      return counter

  return -1


def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw[0]

print(part1(file_reader('01_input.txt')))
print(part2(file_reader('01_input.txt')))