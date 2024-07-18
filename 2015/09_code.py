from typing import List


def part1(input_dinstances: List[str]) -> int:
  locations = set()
  distances = dict()
  ans = 0

  for raw_distance in input_dinstances:
    distance = raw_distance.split()
    start = distance[0]
    end = distance[2]
    length = int(distance[4])
    ans += length

    locations.add(start)
    locations.add(end)

    if not start in distances:
      distances[start] = dict()
    if not end in distances:
      distances[end] = dict()
    
    distances[start][end] = length
    distances[end][start] = length

  locations_array = list(locations)

  # now to iterate through every possible order...
  visited = [0 for _ in range(len(locations_array))]
  def travel_sales(current: str, distance_covered: int, record_holder: int):
    for pointer in range(len(visited)):
      if visited[pointer] == 0:
        visited[pointer] = 1
        if current is None:
          record_holder = travel_sales(locations_array[pointer], 0, record_holder)
        else:
          ## for part 1, change max to min
          record_holder = max(travel_sales(locations_array[pointer], \
                                          distance_covered + distances[current][locations_array[pointer]], \
                                          record_holder), \
                              record_holder)
        visited[pointer] = 0

    if sum(visited) == len(visited):
      return distance_covered

    return record_holder

  ## for part 1, change the second 0 to ans
  return travel_sales(None, 0, 0)


def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw

## print(file_reader('09_input.txt'))
print(part1(file_reader('09_input.txt')))
## print(part2(file_reader('09_input.txt')))