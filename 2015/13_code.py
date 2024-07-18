from typing import List


def part1(input_relationships: List[str]) -> int:
  people = set()
  feelings = dict()
  ans = 0

  for raw_feelings in input_relationships:
    feeling = raw_feelings.split()
    start = feeling[0]
    end = feeling[10][:-1]
    emotion = int(feeling[3])
    if feeling[2] == 'lose':
      emotion *= -1

    people.add(start)

    if not start in feelings:
      feelings[start] = dict()
    
    feelings[start][end] = emotion

  people_array = list(people)

  ## for part 1, just ignore the next 5 lines
  people_array.append('me')
  feelings['me'] = dict()
  for ak in feelings.keys():
    feelings['me'][ak] = 0
    feelings[ak]['me'] = 0


  # now to iterate through every possible order...
  visited = [0 for _ in range(len(people_array))]
  visited[0] = 1
  def seating_arrangement(current: str, emotions: int):
    ans = 0
    for pointer in range(1, len(visited)):
      if visited[pointer] == 0:
        visited[pointer] = 1
        ans = max(seating_arrangement(people_array[pointer], \
                                      emotions + feelings[current][people_array[pointer]] + feelings[people_array[pointer]][current]), \
                  ans)
        visited[pointer] = 0
    
    if sum(visited) == len(visited):
      return emotions + feelings[current][people_array[0]] + feelings[people_array[0]][current]

    return ans

  return seating_arrangement(people_array[0], 0)


def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw

## print(file_reader('13_input.txt'))
print(part1(file_reader('13_input.txt')))
## print(part2(file_reader('13_input.txt')))