"""Day 8 of the 2020 Advent of Code

Polished since we will likely be revisiting this boot code
"""

class BootCode:
    def __init__(self, instructions):
        self.accumulator = 0
        self.pointer = 0
        self.instructions = instructions

    # The commands that this computer can execute
    def acc(self, val, *discard):
        self.accumulator += val
        self.pointer += 1

    def jmp(self, val, *discard):
        self.pointer += val

    def nop(self, *discard):
        self.pointer += 1

    # The command that takes an arbitrary operation and executes it
    def operation(self, instruction):
        getattr(self, instruction[0])(instruction[1])

    # The commands that prints values
    def printAccumulator(self):
        print("Accumulator:", self.accumulator)


class Handheld(BootCode):
    def __init__(self, instructions):
        super().__init__(instructions)
        
    def findLoop(self):
        visited = set()
        while self.pointer not in visited:
            if self.pointer >= len(self.instructions):
                return False
            visited.add(self.pointer)
            self.operation(self.instructions[self.pointer])
        return True


# Brute force this solution
def breakLoop(instructions):
    for i in range(len(instructions)):
        if instructions[i][0] == 'jmp':
            instructions[i][0] = 'nop'
            game_console = Handheld(instructions)
            if not game_console.findLoop():
                game_console.printAccumulator()
                return True
            instructions[i][0] = 'jmp'
            
        elif instructions[i][0] == 'nop':
            instructions[i][0] = 'jmp'
            game_console = Handheld(instructions)
            if not game_console.findLoop():
                game_console.printAccumulator()
                return True
            instructions[i][0] = 'nop'


def readFile(fileName):
    instructions_raw = open(fileName).read().strip().split('\n')
    instruction_set = []
    for line in instructions_raw:
        temp = line.split(' ')
        instruction_set.append([temp[0], int(temp[1])])
    return instruction_set


def main():
    instructions = readFile('input_08_1.txt')
    game_console = Handheld(instructions)
    game_console.findLoop()
    print('Part 1:')
    game_console.printAccumulator()
    print('Part 2:')
    breakLoop(instructions)


main()
