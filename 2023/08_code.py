import math

def part1(input_list):
  ans = 0
  
  lr = input_list[0]

  inst = {}
  for line in input_list[2:]:
    key = line[:3]
    left = line[7:10]
    right = line[12:15]
    inst[key] = (left, right)

  val = 'AAA'
  i = 0
  while val != 'ZZZ':
    if lr[i] == 'L':
      val = inst[val][0]
    else:
      val = inst[val][1]
    i += 1
    i %= len(lr)
    ans += 1

  print(f'Part 1: {ans}')



def part2(input_list):
  lr = input_list[0]

  inst = {}
  for line in input_list[2:]:
    key = line[:3]
    left = line[7:10]
    right = line[12:15]
    inst[key] = (left, right)
    if key[2] == 'A':
      print(key)

  vals = ['AAA', 'GCA', 'CMA', 'QNA', 'FTA', 'CBA']
  timings = []
  for v in vals:
    i = 0
    ans = 0
    while v[2] != 'Z':
      if lr[i] == 'L':
        v = inst[v][0]
      else:
        v = inst[v][1]
      i += 1
      i %= len(lr)
      ans += 1
    timings.append(ans)

  def lcm(a, b):
    return a * b // math.gcd(a, b)

  one = lcm(timings[0], timings[1])
  two = lcm(timings[2], timings[3])
  three = lcm(timings[4], timings[5])
  four = lcm(one, two)
  final = lcm(three, four)


  print(f'Part 2: {final}')



def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw

part1(file_reader('08_input.txt'))
part2(file_reader('08_input.txt'))
