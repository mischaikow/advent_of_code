def part1(first_value: str, depth: int):
  if depth == 0:
    return len(first_value)

  last_char = None
  count = 0
  ans = ''
  for char in first_value:
    if last_char is None:
      last_char = char
      count += 1
    elif char == last_char:
      count += 1
    else:
      ans += str(count) + str(last_char)
      last_char = char
      count = 1
  ans += str(count) + str(last_char)

  return part1(ans, depth-1)

puzzle_input = '1113222113'
rounds = 40
print(part1(puzzle_input, rounds))

rounds = 50
print(part1(puzzle_input, rounds))