import math

def part1(target_gift_count: int) -> None:
  counter = 1
  while True:
    present_count = 0
    for elf in range(1, math.floor(math.sqrt(counter)) + 1):
      if counter % elf == 0:
        present_count += elf * 10
        if counter // elf != elf:
          present_count += (counter // elf) * 10
      
    if counter % 100000 == 0 or counter < 10:
      print(f'Progress: {counter} has {present_count}')

    if present_count >= target_gift_count:
      print(f'Part 1: {counter}')
      break
    counter += 1


def part2(target_gift_count: int) -> None:
  counter = 1
  while True:
    present_count = 0
    for elf in range(1, math.floor(math.sqrt(counter)) + 1):
      if counter % elf == 0:
        if counter // elf <= 50:
          present_count += elf * 11
        if counter // elf != elf and elf <= 50:
          present_count += (counter // elf) * 11
      
    if counter % 100000 == 0 or counter < 10:
      print(f'Progress: {counter} has {present_count}')

    if present_count >= target_gift_count:
      print(f'Part 2: {counter}')
      break
    counter += 1

target_gift_count = 36000000

part1(target_gift_count)
part2(target_gift_count)