"""Day 13 of the Advent of Code


"""

def readFile(fileName):
    with open(fileName) as f:
        raw = f.readlines()
    time = int(raw[0].strip())
    bus_list = raw[1].strip().split(',')
    return time, bus_list


def nextBus(time, raw_list):
    wait = (-1, 0)
    for bus in raw_list:
        if bus != 'x':
            temp = time % int(bus)
            temp = int(bus) - temp
            if wait[0] == -1:
                wait = (int(bus), temp)
            elif temp < wait[1]:
                wait = (int(bus), temp)
    return wait[0]*wait[1]


def perfectSpacing(bus_list):
    start = 0
    step = 1
    for i in range(len(bus_list)):
        if bus_list[i] != 'x':
            while (start + i) % int(bus_list[i]) != 0:
                start += step

            step *= int(bus_list[i])
    return start


def main():
    time, bus_list = readFile('input_13_1.txt')
    print('Part 1:', nextBus(time, bus_list))
    print('Part 2:', perfectSpacing(bus_list))
    return True


main()
