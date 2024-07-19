from typing import List


def special_multiply(values: List[int]) -> int:
  ans = 1
  for v in values:
    if v > 0:
      ans *= v
    else:
      return 0
  return ans


def part1(input_impacts: List[str], total_volume: int) -> int:
  ans = 0
  calorie_restricted_ans = 0

  capacity = dict()
  durability = dict()
  flavor = dict()
  texture = dict()
  calories = dict()
  ingredients = []

  for ing_string in input_impacts:
    ing = ing_string.split()
    the_ingredient = ing[0][:-1]
    ingredients.append(the_ingredient)
    capacity[the_ingredient] = int(ing[2][:-1])
    durability[the_ingredient] = int(ing[4][:-1])
    flavor[the_ingredient] = int(ing[6][:-1])
    texture[the_ingredient] = int(ing[8][:-1])
    calories[the_ingredient] = int(ing[10])

  for i in range(total_volume):
    for j in range(i, total_volume):
      for k in range(j, total_volume):
        one_capacity = capacity[ingredients[0]] * i + capacity[ingredients[1]] * (j - i) + capacity[ingredients[2]] * (k - j) + capacity[ingredients[3]] * (100 - k)
        one_durability = durability[ingredients[0]] * i + durability[ingredients[1]] * (j - i) + durability[ingredients[2]] * (k - j) + durability[ingredients[3]] * (100 - k)
        one_flavor = flavor[ingredients[0]] * i + flavor[ingredients[1]] * (j - i) + flavor[ingredients[2]] * (k - j) + flavor[ingredients[3]] * (100 - k)
        one_texture = texture[ingredients[0]] * i + texture[ingredients[1]] * (j - i) + texture[ingredients[2]] * (k - j) + texture[ingredients[3]] * (100 - k)
        one_calorie = calories[ingredients[0]] * i + calories[ingredients[1]] * (j - i) + calories[ingredients[2]] * (k - j) + calories[ingredients[3]] * (100 - k)

        value = special_multiply([one_capacity, one_durability, one_flavor, one_texture])
        ans = max(ans, value)
        if one_calorie == 500:
          calorie_restricted_ans = max(calorie_restricted_ans, value)


  print(f'Part 1: {ans}')
  print(f'Part 2: {calorie_restricted_ans}')


def file_reader(file_name):
  input_file = open(file_name, 'r')
  inputs_raw = input_file.readlines()
  for i in range(len(inputs_raw)):
    inputs_raw[i] = inputs_raw[i].replace('\n','')
  return inputs_raw

## print(file_reader('15_input.txt'))
part1(file_reader('15_input.txt'), 100)