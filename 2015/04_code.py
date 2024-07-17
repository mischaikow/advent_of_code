import hashlib

def part1(input_string: str):
  for numb in range(100000000000):
    dummy = hashlib.md5((input_string + str(numb)).encode('utf-8')).hexdigest()[:6]
    if numb / 10000000 == numb // 10000000:
      print(f'{numb}: {dummy}')
    if dummy == '000000':
      return str(numb)

## puzzle_input = 'abcdef'
## puzzle_input = 'pqrstuv'
puzzle_input = 'ckczppom'
print(part1(puzzle_input))
## print(part2(puzzle_input))