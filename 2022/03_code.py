def part1(inputs_raw):
  ans = 0
  for row in inputs_raw:
    row = [ \
        row[:len(row)//2], \
        row[len(row)//2:]]
    cut = False
    for i in row[0]:
      if cut:
        break
      for j in row[1]:
        if i == j:
          if ord(i) < 97:
            ans += ord(i)-38
          else:
            ans += ord(i)-96
          cut = True
          break
  print(f'Part 1: {ans}')

def part2(inputs_raw):
  ans = 0
  for index in range(0, len(inputs_raw), 3):
    first_two = []
    cut = False
    for i in inputs_raw[index]:
      for j in inputs_raw[index+1]:
        if i == j:
          first_two.append(i)
    
    for i in first_two:
      if cut:
        break
      for j in inputs_raw[index+2]:
        if i == j:
          if ord(i) < 97:
            ans += ord(i)-38
          else:
            ans += ord(i)-96
          cut = True
          break
  print(f'Part 2: {ans}')


def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw

part1(file_reader('day03input.txt'))
part2(file_reader('day03input.txt'))
