from collections import deque

DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def travel(distance_grid: list[list[int]], visited_array, current_loc, distance_covered) -> int:
    ans = 1000000
    for i in range(len(visited_array)):
        if visited_array[i] == 0:
            nv_array = visited_array.copy()
            nv_array[i] = 1
            new_distance = distance_covered + distance_grid[current_loc][i]
            if sum(nv_array) == len(nv_array):
                ## For part 1, use the following line
                #return new_distance
                ## For part 2, use this line instead
                return new_distance + distance_grid[i][0]
            ans = min(ans, travel(distance_grid, nv_array, i, new_distance))
    return ans


def part1(maze: list[str]) -> int:
    ans = 0
    digit_collection = dict()
    distance_grid = [[-1] * 8 for _ in range(8)]
    for i in range(8):
        distance_grid[i][i] = 0

    height = len(maze)
    width = len(maze[0])

    for i in range(height):
        for j in range(width):
            if maze[i][j].isdigit():
                digit_collection[maze[i][j]] = (i, j)
    print(len(digit_collection))

    for item, location in digit_collection.items():
        distances = [[-1] * width for _ in range(height)]
        distances[location[0]][location[1]] = 0
        loc = (location[0], location[1], 0)
        to_visit = deque([loc])
        while len(to_visit) > 0:
            current_spot_x, current_spot_y, distance = to_visit.popleft()
            for dx, dy in DIRECTIONS:
                if maze[current_spot_x + dx][current_spot_y + dy] != '#' and distances[current_spot_x + dx][current_spot_y + dy] < 0:
                    distances[current_spot_x + dx][current_spot_y + dy] = distance + 1
                    if maze[current_spot_x + dx][current_spot_y + dy].isdigit():
                        distance_grid[int(item)][int(maze[current_spot_x + dx][current_spot_y + dy])] = distance + 1
                    to_visit.append(((current_spot_x + dx, current_spot_y + dy, distance + 1)))

    visited_array = [1, 0, 0, 0, 0, 0, 0, 0]
    current_loc = 0
    distance_covered = 0
    return travel(distance_grid, visited_array, current_loc, distance_covered)


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "")
    return inputs_raw


## print(file_reader("24_input.txt"))
print(f"Part 1: {part1(file_reader("24_input.txt"))}")
## part2(file_reader('24_input.txt'))
