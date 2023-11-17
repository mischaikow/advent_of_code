"""Day 5 of the Advent of Code event

I wrote this code as quickly as possible rather than
going for something even remotely polished.
"""

def fileReader(fileName):
    with open(fileName, 'r') as f:
        inputs_raw = f.readlines()
    return inputs_raw


def maxSeat(tickets):
    max = 0
    for seatID in tickets:
        row = 0
        col = 0
        for val in seatID:
            if val == 'F':
                row *= 2
            elif val == 'B':
                row *= 2
                row += 1
            elif val == 'L':
                col *= 2
            elif val == 'R':
                col *= 2
                col += 1
        if (row * 8) + col > max:
            max = (row * 8) + col
    return max


def allSeat(tickets):
    output = []
    for seatID in tickets:
        row = 0
        col = 0
        for val in seatID:
            if val == 'F':
                row *= 2
            elif val == 'B':
                row *= 2
                row += 1
            elif val == 'L':
                col *= 2
            elif val == 'R':
                col *= 2
                col += 1
        output.append(row*8 + col)
    return output


def mySeat(taken_seats):
    fullList = [0]*(127*8 + 7)
    for seat in taken_seats:
        fullList[seat] = 1
    for check in range(127*1+7, 127*7+7):
        if fullList[check-1] == 1 and\
           fullList[check] == 0 and\
           fullList[check+1] == 1:
            return check
    

def main(fileName):
    tickets = fileReader(fileName)
    print('Part 1:', maxSeat(tickets))
    taken_seats = allSeat(tickets)
    print('Part 2:', mySeat(taken_seats))

main('input_05_1.txt')
