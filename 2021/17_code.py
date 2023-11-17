import math

def y_target_check(speed, y_target):
    start_speed = speed
    y, steps, peak = 0, 0, 0
    step_ans = []
    while y >= y_target[0]:
        if speed == 0:
            peak = y
        if y <= y_target[1]:
            step_ans.append(steps)
        steps += 1
        y += speed
        speed -= 1
    return (start_speed, step_ans, peak)

def x_hits_in_steps(steps, x_target):
    ans = 0
    for start_speed in range(x_target[1]+1):
        x = 0
        speed = start_speed
        for _ in range(steps):
            x += speed
            speed = max(speed-1, 0)
        if x_target[0] <= x <= x_target[1]:
            ans += 1
    return ans

def part_1(x_target, y_target):
    y_valid = []
    for n in range(-y_target[0]-1, -1, -1):
        hit = y_target_check(n, y_target)
        if hit[1] != -1:
            y_valid.append(hit)

    sequence_of_triangle_numbers = [0, 1]
    while sequence_of_triangle_numbers[-1] <= x_target[1]:
        sequence_of_triangle_numbers.append(sequence_of_triangle_numbers[-1] + len(sequence_of_triangle_numbers))
        if sequence_of_triangle_numbers[-1] >= x_target[0]:
            return y_valid[0][2]

    for target in y_valid:
        _, steps, peak = target
        for s in steps:
            if s >= len(sequence_of_triangle_numbers):
                pass
            elif x_hits_in_steps(s, x_target) > 0:
                return peak

def part_2(x_target, y_target):
    ans = 0
    for x_start in range(x_target[1]+1):
        for y_start in range(y_target[0], -y_target[0]+1):
            x, x_speed = 0, x_start
            y, y_speed = 0, y_start
            while x <= x_target[1] and y >= y_target[0]:
                if x >= x_target[0] and y <= y_target[1]:
                    ans += 1
                    break
                x += x_speed
                y += y_speed
                x_speed = max(x_speed-1, 0)
                y_speed -= 1
    return ans

print(part_1([201, 230], [-99, -65]))
print(part_2([201, 230], [-99, -65]))