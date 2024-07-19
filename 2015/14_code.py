from typing import List


def part1(input_paces: List[str], time: int) -> int:
  speeds = dict()
  speed_times = dict()
  rest_times = dict()
  big_distance = dict()
  incremental_distance = dict()
  scores = dict()
  ans_part1 = 0

  for paces in input_paces:
    pace = paces.split()
    reindeer = pace[0]
    speeds[reindeer] = int(pace[3])
    speed_times[reindeer] = int(pace[6])
    rest_times[reindeer] = int(pace[13])
    scores[reindeer] = 0

    complete_cycles = (time // (speed_times[reindeer] + rest_times[reindeer]))
    running_time = min((time % (speed_times[reindeer] + rest_times[reindeer])), speed_times[reindeer])
    big_distance[reindeer] = complete_cycles * speeds[reindeer] * speed_times[reindeer] + running_time * speeds[reindeer]

    ans_part1 = max(ans_part1, big_distance[reindeer])

  print(f'Part 1: {ans_part1}')

  for step in range(1, time+1):
    for deer in scores.keys():
      complete_cycles = (step // (speed_times[deer] + rest_times[deer]))
      running_time = min((step % (speed_times[deer] + rest_times[deer])), speed_times[deer])
      incremental_distance[deer] = complete_cycles * speeds[deer] * speed_times[deer] + running_time * speeds[deer]

    winner = []
    winning_distance = 0
    for deer, coverage in incremental_distance.items():
      if coverage > winning_distance:
        winner = [deer]
        winning_distance = coverage
      elif coverage == winning_distance:
        winner.append(deer)

    for deer in winner:
      scores[deer] += 1

  winning_score = 0
  for points in scores.values():
    winning_score = max(points, winning_score)

  print(f'Part 2: {winning_score}')


def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw

## print(file_reader('14_input.txt'))
part1(file_reader('14_input.txt'), 2503)