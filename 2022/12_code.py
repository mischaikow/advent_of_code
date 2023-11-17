from collections import deque

def part1(topo):
  directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
  ]

  path = [[-1] * len(topo[0]) for _ in range(len(topo))]

  for i in range(len(topo)):
    for j in range(len(topo)):
      if topo[i][j] == 'S':
        toVisit = deque([(i, j)])
        path[i][j] = 0

  ans = 0
  while ans == 0:
    v = toVisit.popleft()
    for d in directions:
      vd = (v[0] + d[0], v[1] + d[1])
      if 0 <= vd[0] < len(topo) \
          and 0 <= vd[1] < len(topo[0]) \
          and path[vd[0]][vd[1]] == -1:

        if topo[vd[0]][vd[1]] == 'E' and \
            (topo[v[0]][v[1]] == 'z' or topo[v[0]][v[1]] == 'y'):
          ans = path[v[0]][v[1]] + 1

        elif topo[vd[0]][vd[1]] == 'E':
          continue

        else:
          v_val = ord(topo[v[0]][v[1]])
          n_val = ord(topo[vd[0]][vd[1]])

          if n_val <= v_val + 1 \
              or topo[v[0]][v[1]] == 'S':
            toVisit.append((vd[0], vd[1]))
            path[vd[0]][vd[1]] = path[v[0]][v[1]] + 1

  print(f'Part 1: {ans}')


def part2(topo):
  directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
  ]

  path = [[-1] * len(topo[0]) for _ in range(len(topo))]

  for i in range(len(topo)):
    for j in range(len(topo)):
      if topo[i][j] == 'E':
        toVisit = deque([(i, j)])
        path[i][j] = 0

  ans = 0
  while ans == 0:
    v = toVisit.popleft()
    for d in directions:
      vd = (v[0] + d[0], v[1] + d[1])
      if 0 <= vd[0] < len(topo) \
          and 0 <= vd[1] < len(topo[0]) \
          and path[vd[0]][vd[1]] == -1:

        if topo[vd[0]][vd[1]] == 'a' and topo[v[0]][v[1]] == 'b':
          ans = path[v[0]][v[1]] + 1

        else:
          if topo[v[0]][v[1]] == 'E':
            v_val = ord('z')
          else:
            v_val = ord(topo[v[0]][v[1]])
          n_val = ord(topo[vd[0]][vd[1]])

          if n_val >= v_val - 1:
            toVisit.append((vd[0], vd[1]))
            path[vd[0]][vd[1]] = path[v[0]][v[1]] + 1

  print(f'Part 2: {ans}')


def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw


part1(file_reader('day12input.txt'))
part2(file_reader('day12input.txt'))