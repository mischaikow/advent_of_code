def part1(parts: list[str]) -> int:
    ans = -1
    ans_distance = 1_000_000_000
    for index in range(len(parts)):
        pos, vel, acc = parts[index].split(", ")
        pos = [int(x) for x in pos[3:-1].split(",")]
        vel = [int(x) for x in vel[3:-1].split(",")]
        acc = [int(x) for x in acc[3:-1].split(",")]

        distance = 0
        for _ in range(1_000):
            for i in range(3):
                vel[i] += acc[i]
                pos[i] += vel[i]

        for i in range(3):
            distance += abs(pos[i])

        if distance < ans_distance:
            ans_distance = distance
            ans = index

    return ans


def part2(parts: list[str]) -> int:
    particles = []
    for index in range(len(parts)):
        pos, vel, acc = parts[index].split(", ")
        pos = tuple([int(x) for x in pos[3:-1].split(",")])
        vel = [int(x) for x in vel[3:-1].split(",")]
        acc = tuple([int(x) for x in acc[3:-1].split(",")])

        particles.append({"pos": pos, "vel": vel, "acc": acc})

    for _ in range(1_000):
        for a_part in particles:
            pos = list(a_part["pos"])
            vel = a_part["vel"]
            acc = a_part["acc"]

            for i in range(3):
                vel[i] += acc[i]
                pos[i] += vel[i]

            a_part["pos"] = tuple(pos)
            a_part["vel"] = vel

        to_delete = set()
        for i in range(len(particles)):
            for j in range(i + 1, len(particles)):
                if particles[i]["pos"] == particles[j]["pos"]:
                    to_delete.add(i)
                    to_delete.add(j)
        to_delete = list(to_delete)
        to_delete.sort(reverse=True)
        for i in to_delete:
            particles.pop(i)

    return len(particles)


def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "")
    return inputs_raw


print(f"Part 1: {part1(file_reader('20_input.txt'))}")
print(f"Part 2: {part2(file_reader('20_input.txt'))}")
