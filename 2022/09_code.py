def move_tail(tail, head):
  ans_0 = tail[0]
  ans_1 = tail[1]

  if tail[0] < head[0]:
    ans_0 = tail[0] + 1
  if tail[0] > head[0]:
    ans_0 = tail[0] - 1
  if tail[1] < head[1]:
    ans_1 = tail[1] + 1
  if tail[1] > head[1]:
    ans_1 = tail[1] - 1

  if (ans_0, ans_1) == head:
    return tail
  return (ans_0, ans_1)


def part1(inputs_raw):
  d = {
      'L': (-1, 0),
      'U': (0, 1),
      'R': (1, 0),
      'D': (0, -1)
      }
  
  head = (0, 0)
  tail = (0, 0)

  ans = set()
  for line in inputs_raw:
    for _ in range(line[1]):
      head = (head[0] + d[line[0]][0], \
              head[1] + d[line[0]][1])
      tail = move_tail(tail, head)
      ans.add(tail)

  print(f'Part 1: {len(ans)}')

  rope = [(0, 0) for _ in range(10)]

  ans = set()
  for line in inputs_raw:
    for _ in range(line[1]):
      rope[0] = (rope[0][0] + d[line[0]][0], \
          rope[0][1] + d[line[0]][1])
      for i in range(1, len(rope)):
        rope[i] = move_tail(rope[i], rope[i-1])
      ans.add(rope[9])

  print(f'Part 2: {len(ans)}')


def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','').split()
    inputs_raw[i][1] = int(inputs_raw[i][1])
  return inputs_raw

part1(file_reader('day09input.txt'))
