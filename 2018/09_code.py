from collections import defaultdict


class Node:
    def __init__(self, val, last=None, next=None):
        self.val = val
        self.last = last
        self.next = next


def part1(player_count: int, last_marble: int) -> int:
    pointer = Node(0, next=Node(2, next=Node(1)))
    pointer.next.next.next = pointer
    pointer.last = pointer.next.next
    pointer.last.last = pointer.next
    pointer.last.last.last = pointer
    player_scores = defaultdict(int)

    for i in range(3, last_marble + 1):
        if i % 23 == 0:
            player_scores[i % player_count] += i
            pointer = pointer.last.last.last.last.last.last.last
            player_scores[i % player_count] += pointer.next.val
            pointer.next = pointer.next.next
            pointer.next.last = pointer
        else:
            pointer.next.next.next = Node(i, pointer.next.next, pointer.next.next.next)
            pointer = pointer.next.next
            pointer.next.next.last = pointer.next

    ans = 0
    for val in player_scores.values():
        ans = max(ans, val)
    return ans


actual_players = 423
actual_marbles = 71_944

print(f"Part 1: {part1(actual_players, actual_marbles)}")
print(f"Part 2: {part1(actual_players, 100 * actual_marbles)}")
