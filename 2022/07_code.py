class File:
  def __init__(self, name = None, parent = None, storage = -1):
    self.name = name
    self.parent = parent
    self.storage = storage

  def size(self):
    return self.storage


class Directory:
  def __init__(self, name = None, parent = None):
    self.name = name
    self.parent = parent
    self.storage = -1
    self.sub_f = dict()

  def sum_storage(self):
    self.storage = 0
    for f in self.sub_f:
      self.storage += self.sub_f[f].size()

  def size(self):
    return self.storage

  # new_file = [name, size]
  def add_file(self, new_file):
    self.sub_f[new_file[1]] = File(new_file[1], self, int(new_file[0]))

  def add_folder(self, new_folder_name):
    self.sub_f[new_folder_name] = Directory(new_folder_name, self)


def part2(pointer, gap):
  answer = pointer
  for key, folder in pointer.sub_f.items():
    if isinstance(folder, Directory) and folder.size() >= gap:
      temp = part2(folder, gap)
      if temp.size() < answer.size() and temp.size() >= gap:
        answer = temp
  return answer


def part1(inputs_raw):
  ans = 0
  pointer = Directory('/')
  for line in inputs_raw[1:]:
    # cd
    if line[0:4] == '$ cd':
      if line[5:7] == '..':
        pointer.sum_storage()
        if isinstance(pointer, Directory) and pointer.size() <= 100000:
          ans += pointer.size()
        pointer = pointer.parent

      else:
        instruction = line.split()
        pointer = pointer.sub_f[instruction[2]]
    
    # ls outputs
    elif line[0:3] == 'dir':
      instruction = line.split()
      pointer.add_folder(instruction[1])

    elif line[0].isnumeric():
      pointer.add_file(line.split())

  print(f'Part 1: {ans}')

  while pointer.name != '/':
    pointer = pointer.parent
    pointer.sum_storage()

  TOTAL_SPACE = 70000000
  NEEDED_SPACE = 30000000
  
  gap = pointer.size() - (TOTAL_SPACE - NEEDED_SPACE)

  result = part2(pointer, gap)
  print(f'Part 2: {result.size()}')

def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw

part1(file_reader('day07input.txt'))
