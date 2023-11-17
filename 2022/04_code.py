def part1(inputs_raw):
  count1, count2 = 0, 0
  for row in inputs_raw:
    elfA = row[0].split('-')
    elfA[0] = int(elfA[0])
    elfA[1] = int(elfA[1])
    elfB = row[1].split('-')
    elfB[0] = int(elfB[0])
    elfB[1] = int(elfB[1])
    if (elfA[0] <= elfB[0] and elfA[1] >= elfB[1]) \
        or (elfA[0] >= elfB[0] and elfA[1] <= elfB[1]):
      count1 += 1
    if not (elfA[0] > elfB[1] or elfA[1] < elfB[0]):
      count2 += 1
  print(f'Part 1: {count1}')
  print(f'Part 2: {count2}')


def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','').split(',')
  return inputs_raw


part1(file_reader('day04input.txt'))
