class Monkey:
  def __init__(self, operation, test, if_true, if_false, stuff, big_num):
    self.operation = operation
    self.test = test
    self.if_true = if_true
    self.if_false = if_false
    self.stuff = stuff
    self.inspections = 0
    self.big_num = big_num

  def inspects(self):
    self.inspections += len(self.stuff)
    outcome = []
    while len(self.stuff) > 0:
      item = self.stuff.pop()
      item = self.operation(item)
      if self.big_num:
        item %= 9699690
      else:
        item = item // 3
      if item % self.test == 0:
        outcome.append((self.if_true, item))
      else:
        outcome.append((self.if_false, item))

    return outcome

  def add(self, value):
    self.stuff.append(value)


def monkeys_def(big_num):
  monkeys = [Monkey(lambda a : a * 2, 11, 1, 4, [98, 70, 75, 80, 84, 89, 55, 98], big_num)]
  monkeys.append(Monkey(lambda a : a ** 2, 19, 7, 3, [59], big_num))
  monkeys.append(Monkey(lambda a : a + 6, 7, 0, 5, [77, 95, 54, 65, 89], big_num))
  monkeys.append(Monkey(lambda a : a + 2, 17, 6, 2, [71, 64, 75], big_num))
  monkeys.append(Monkey(lambda a : a * 11, 3, 1, 7, [74, 55, 87, 98], big_num))
  monkeys.append(Monkey(lambda a : a + 7, 5, 0, 4, [90, 98, 85, 52, 91, 60], big_num))
  monkeys.append(Monkey(lambda a : a + 1, 13, 5, 2, [99, 51], big_num))
  monkeys.append(Monkey(lambda a : a + 5, 2, 3, 6, [98, 94, 59, 76, 51, 65, 75], big_num))
  return monkeys


def part1():
  monkeys = monkeys_def(False)
  for _ in range(20):
    for mon in monkeys:
      result = mon.inspects()
      for toss in result:
        monkeys[toss[0]].add(toss[1])

  big = [0, 0]
  for mon in monkeys:
    if mon.inspections > big[0]:
      if big[1] < big[0]:
        big[1] = mon.inspections
      else:
        big[0] = mon.inspections
    elif mon.inspections > big[1]:
      big[1] = mon.inspections

  print(f'Part 1: {big[0] * big[1]}')


def part2():
  monkeys = monkeys_def(True)
  for _ in range(10000):
    for mon in monkeys:
      result = mon.inspects()
      for toss in result:
        monkeys[toss[0]].add(toss[1])

  big = [0, 0]
  for mon in monkeys:
    if mon.inspections > big[0]:
      if big[1] < big[0]:
        big[1] = mon.inspections
      else:
        big[0] = mon.inspections
    elif mon.inspections > big[1]:
      big[1] = mon.inspections

  print(f'Part 2: {big[0] * big[1]}')


part1()
part2()
