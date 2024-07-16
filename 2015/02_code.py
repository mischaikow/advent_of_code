from typing import List

def part1(input_boxes: List[int]):
  ans = 0
  for a_box in input_boxes:
    sides = [a_box[0] * a_box[1], a_box[1]*a_box[2], a_box[0]*a_box[2]]
    area = 2*sides[0] + 2*sides[1] + 2*sides[2] + min(sides)

    ans += area
  return ans


def part2(input_boxes: List[int]):
  ans = 0
  for a_box in input_boxes:
    side_perimeters = [a_box[0] + a_box[1], a_box[1]+a_box[2], a_box[0]+a_box[2]]
    ribbon_add = 2 * min(side_perimeters) + (a_box[0] * a_box[1] * a_box[2])

    ans += ribbon_add
  return ans


def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = [int(x) for x in inputs_raw[i].replace('\n','').split('x')]
  return inputs_raw

## print(file_reader('02_input.txt'))
print(part1(file_reader('02_input.txt')))
print(part2(file_reader('02_input.txt')))