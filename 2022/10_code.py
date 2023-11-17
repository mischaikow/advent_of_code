class Computer:
  def __init__(self, instructions = None):
    self.step = 0
    self.instructions = instructions
    self.pointer = 0
    self.register = 1
    self.state = None

  def cycle(self):
    if self.state is not None:
      if self.state[0] == 'addx':
        self.register += self.state[1]
        self.state = None

    elif self.pointer == len(self.instructions):
      print('End of Instructions...')

    elif self.instructions[self.pointer][0] == 'addx':
      self.state = ('addx', self.instructions[self.pointer][1])
      self.pointer += 1

    else: # noop
      self.pointer += 1

    self.step += 1


class Screen:
  def __init__(self):
    self.screen = [['.'] * 40 for _ in range(6)]

  def draw(self, register, step):
    loc = step % 40
    if loc == register or loc == register+1 or loc == register-1:
      self.screen[step // 40][step % 40] = '#'

  def display(self):
    for i in self.screen:
      print(''.join(i))


def part1(inputs_raw):
  run_1 = Computer(inputs_raw)
  image = Screen()
  ans = 0

  while run_1.step < 241:
    run_1.cycle()

    if (run_1.step + 21) % 40 == 0:
      ans += (run_1.step + 1) * run_1.register

    image.draw(run_1.register, run_1.step)

  print(f'Part 1: {ans}')
  print('Part 2:')
  image.display()


def file_reader(file_name):
  input_file = open(file_name,  'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n', '').split()
    if len(inputs_raw[i]) > 1:
      inputs_raw[i][1] = int(inputs_raw[i][1])
  return inputs_raw

part1(file_reader('day10input.txt'))
