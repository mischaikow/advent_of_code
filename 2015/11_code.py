def straight_increase(pw: str) -> bool:
  history = [-1, -1]
  for char in pw:
    if ord(char) == history[1]+1 and ord(char) == history[0]+2:
      return True
    history[0] = history[1]
    history[1] = ord(char)

  return False

def contains_forbidden(pw: str) -> bool:
  if 'i' in pw:
    return True
  if 'o' in pw:
    return True
  if 'l' in pw:
    return True
  return False

def two_pairs(pw: str) -> bool:
  counter = 0
  pointer = 1
  while pointer < len(pw):
    if pw[pointer-1] == pw[pointer]:
      counter += 1
      pointer += 1
    pointer += 1
    
  return counter > 1


def increment_string(pw: str) -> str:
  temp = list(pw)
  pointer = len(temp) - 1
  while True:
    if temp[pointer] == 'z':
      temp[pointer] = 'a'
      pointer -= 1
    else:
      temp[pointer] = chr(ord(temp[pointer]) + 1)
      return ''.join(temp)


def part1(first_value: str) -> str:

  while True:
    first_value = increment_string(first_value)
    if straight_increase(first_value) and not contains_forbidden(first_value) and two_pairs(first_value):
      return first_value



puzzle_input = 'abcdefgh'
puzzle_input = 'ghijklmn'
puzzle_input = 'hxbxwxba'
ans = part1(puzzle_input)
print(ans)
print(part1(ans))
