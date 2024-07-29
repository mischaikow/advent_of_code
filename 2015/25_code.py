def part1():
    FIRST_CODE = 20151125

    step_count = 0
    for i in range(3075):
        step_count += i
    for j in range(2981):
        step_count += i + j

    code = FIRST_CODE
    for _ in range(step_count):
        code = (code * 252533) % 33554393

    print(code)

part1()

