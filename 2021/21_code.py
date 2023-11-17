from collections import deque

class Trie:
    def __init__(self, val, children = []):
        self.val = val
        self.children = []


def part_1(location):
    die_roll = 0
    roll_count = 0
    scores = [0, 0]
    player_turn = 0
    while all(s < 1000 for s in scores):
        turn = 0
        for _ in range(3):
            die_roll = (die_roll % 100) + 1
            roll_count += 1
            turn += die_roll
        location[player_turn] += turn
        location[player_turn] %= 10
        scores[player_turn] += location[player_turn]
        if location[player_turn] == 10: scores[player_turn] += 10
        player_turn = (player_turn+1) % 2
    return min(scores) * roll_count



def part_2(location):
    one_turn_distribution = { 3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1 }
    scores_0 = deque()
    scores_1 = deque()
    #          position    score    scenarios  turn
    scores_0.append(((location[0], 0, 1, 0)))
    scores_1.append(((location[1], 0, 1, 0)))
    turn = 0
    scenarios = [1, 1]
    wins = [0, 0]

    while scores_0 and scores_1:
        turn += 1
        # Player 1
        while scores_0 and scores_0[0][3] < turn:
            start = scores_0.popleft()
            scenarios[0] -= start[2]
            for i in range(3, 10):
                position = (start[0] + i) % 10
                if position == 0: position = 10

                if start[1] + position >= 21:
                    wins[0] += (scenarios[1] * one_turn_distribution[i] * start[2])
                else:
                    branch = (position, start[1] + position, start[2] * one_turn_distribution[i], turn)
                    scenarios[0] += branch[2]
                    scores_0.append(branch)

        # Player 2
        while scores_0 and scores_1 and scores_1[0][3] < turn:
            start = scores_1.popleft()
            scenarios[1] -= start[2]
            for i in range(3, 10):
                position = (start[0] + i) % 10
                if position == 0: position = 10

                if start[1] + position >= 21:
                    wins[1] += (scenarios[0] * one_turn_distribution[i] * start[2])
                else:
                    branch = (position, start[1] + position, start[2] * one_turn_distribution[i], turn)
                    scenarios[1] += branch[2]
                    scores_1.append(branch)

    return max(wins)
 
print(part_1([9, 3]))
print(part_2([9, 3]))
