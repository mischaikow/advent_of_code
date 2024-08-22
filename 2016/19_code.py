class Node:
    def __init__(self, value, pointer=None):
        self.value = value
        self.pointer = pointer

    def kill_neighbor(self):
        self.pointer = self.pointer.pointer

    def is_self(self):
        return self.value == self.pointer.value


def part1(elf_count: int) -> int:
    root = Node(1)
    pointer = root

    for i in range(3, elf_count, 2):
        new_node = Node(i)
        pointer.pointer = new_node
        pointer = new_node
    pointer.pointer = root

    if elf_count % 2 == 0:
        pointer = pointer.pointer

    while not pointer.is_self():
        pointer.kill_neighbor()
        pointer = pointer.pointer

    return pointer.value


def part2(elf_count: int) -> int:
    root = Node(1)
    pointer = root

    for i in range(2, elf_count):
        new_node = Node(i)
        pointer.pointer = new_node
        pointer = new_node
    pointer.pointer = root

    pointer = root
    deletion = pointer
    for _ in range((elf_count - 1) // 2):
        deletion = deletion.pointer

    while elf_count > 0:
        if elf_count % 2 == 1:
            deletion = deletion.pointer
        deletion.kill_neighbor()
        elf_count -= 1
        pointer = pointer.pointer

    return pointer.value


TEST_INPUT = 5
ACTUAL_INPUT = 3005290

print(f"Part 1: {part1(ACTUAL_INPUT)}")
print(f"Part 2: {part2(ACTUAL_INPUT)}")
