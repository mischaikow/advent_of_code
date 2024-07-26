from typing import List, Dict


class Bots:
    def __init__(self, downstream_high=None, downstream_low=None, is_high_output=False, is_low_output=False, slot_a=None, slot_b=None):
        self.downstream_high = downstream_high
        self.downstream_low = downstream_low
        self.is_high_output = is_high_output
        self.is_low_output = is_low_output
        self.slot_a = slot_a
        self.slot_b = slot_b

    def add_value(self, value):
        if self.slot_a is None:
            self.slot_a = value
        elif self.slot_b is None:
            self.slot_b = value
        else:
            print('Uh oh')

    def distribution(self, downstream_high=None, downstream_low=None, is_high_output=False, is_low_output=False):
        self.downstream_high = downstream_high
        self.downstream_low = downstream_low
        self.is_high_output = is_high_output
        self.is_low_output = is_low_output

    def process(self, bots: Dict, outputs: Dict):
        if self.slot_a is not None and self.slot_b is not None:
            if self.is_low_output:
                outputs[self.downstream_low] = min(self.slot_a, self.slot_b)
            else:
                bots[self.downstream_low].add_value(min(self.slot_a, self.slot_b))
            if self.is_high_output:
                outputs[self.downstream_high] = max(self.slot_a, self.slot_b)
            else:
                bots[self.downstream_high].add_value(max(self.slot_a, self.slot_b))
            self.slot_a = None
            self.slot_b = None

    def check_answer(self) -> bool:
        if (self.slot_a == 61 and self.slot_b == 17) or (self.slot_a == 17 and self.slot_b == 61):
            return True
        return False



def part1(bot_instructions: List[str]) -> None:
    bots = dict()
    outputs = dict()

    for a_line in bot_instructions:
        if a_line[0] == 'value':
            value = int(a_line[1])
            bot = int(a_line[5])
            if bot in bots:
                bots[bot].add_value(value)
            else:
                bots[bot] = Bots(slot_a=value)
        elif a_line[0] == 'bot':
            source = int(a_line[1])
            dest_low = int(a_line[6])
            dest_high = int(a_line[11])
            is_low_output = False
            is_high_output = False
            if a_line[5] == 'output':
                is_low_output = True
                if not dest_low in outputs:
                    outputs[dest_low] = -1
            if a_line[10] == 'output':
                is_high_output = True
                if not dest_high in outputs:
                    outputs[dest_high] = -1
            if source in bots:
                bots[source].distribution(downstream_high=dest_high, downstream_low=dest_low, is_high_output=is_high_output, is_low_output=is_low_output)
            else:
                bots[source] = Bots(downstream_high=dest_high, downstream_low=dest_low, is_high_output=is_high_output, is_low_output=is_low_output)
    
    answer_a = False
    answer_b = False
    while True:
        for bot_number, the_bot in bots.items():
            if the_bot.check_answer() and not answer_a:
                print(f'Part 1: {bot_number}')
                answer_a = True
            if outputs[0] >= 0 and outputs[1] >= 0 and outputs[2] >= 0:
                print(f'Part 2: {outputs[0] * outputs[1] * outputs[2]}')
                answer_b = True

            if answer_a and answer_b:
                return
            the_bot.process(bots, outputs)



def file_reader(file_name):
    input_file = open(file_name, "r")
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace("\n", "").split(' ')
    return inputs_raw


## print(file_reader("10_input.txt"))
part1(file_reader('10_input.txt'))
#print(f"Part 2: {part2(file_reader('10_input.txt'))}")
