# There was a much smarter way of doing this with dynamic programming which
# would have allowed for basically infinite iterations. I did not take that
# approach.


def chop(program: list[str], size: int) -> list[list[str]]:
    ans = []
    for i in range(0, len(program), size):
        ans.append([])
        for j in range(0, len(program), size):
            new_box = ""
            for ii in range(i, i + size):
                for jj in range(j, j + size):
                    new_box += program[ii][jj]
                new_box += "/"

            ans[-1].append(new_box[:-1])
    return ans


def recombine(program: list[list[str]], size: int) -> list[str]:
    size += 1
    ans = ["" for _ in range(size * len(program))]

    for i in range(len(program)):
        for box in program[i]:
            broken_box = box.split("/")
            for j in range(size):
                ans[(size * i) + j] += broken_box[j]

    return ans


def flip_2(box: str) -> str:
    return box[3:] + "/" + box[:2]


def rotate_2(box: str) -> str:
    return box[3] + box[0] + "/" + box[4] + box[1]


def flip_3(box: str) -> str:
    return box[8:] + box[3:8] + box[:3]


def rotate_3(box: str) -> str:
    return (
        box[8]
        + box[4]
        + box[0]
        + "/"
        + box[9]
        + box[5]
        + box[1]
        + "/"
        + box[10]
        + box[6]
        + box[2]
    )


def print_3(box: str) -> None:
    print(box[:3])
    print(box[4:7])
    print(box[8:])
    print()


def part1(enhancements_raw: list[str], iterations: int) -> int:
    enhancements_2 = dict()
    enhancements_3 = dict()

    for e in enhancements_raw:
        e_split_input, e_split_output = e.split(" => ")
        if len(e_split_input) == 5:
            enhancements_2[e_split_input] = e_split_output
        else:
            enhancements_3[e_split_input] = e_split_output

    program = [".#.", "..#", "###"]

    for _ in range(iterations):
        if len(program) % 2 == 0:
            start = chop(program=program, size=2)
            end = []
            for line in start:
                end.append([])
                for box in line:
                    for _ in range(3):
                        if box in enhancements_2:
                            break
                        box = rotate_2(box)
                    if not box in enhancements_2:
                        box = flip_2(box)
                    for _ in range(3):
                        if box in enhancements_2:
                            break
                        box = rotate_2(box)
                    while not box in enhancements_2:
                        box = rotate_2(box)
                    end[-1].append(enhancements_2[box])
            program = recombine(end, 2)

        else:
            start = chop(program=program, size=3)
            end = []
            for line in start:
                end.append([])
                for box in line:
                    for _ in range(3):
                        if box in enhancements_3:
                            break
                        box = rotate_3(box)
                    if not box in enhancements_3:
                        box = flip_3(box)
                    for _ in range(3):
                        if box in enhancements_3:
                            break
                        box = rotate_3(box)
                    end[-1].append(enhancements_3[box])
            program = recombine(end, 3)

    ans = 0
    for line in program:
        for light in line:
            if light == "#":
                ans += 1

    return ans


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "")
    return inputs_raw


print(f"Part 1: {part1(file_reader('21_input.txt'), 5)}")
print(f"Part 2: {part1(file_reader('21_input.txt'), 18)}")
