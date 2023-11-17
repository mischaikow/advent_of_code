"""The interpreter

Belatedly moved this into a class in its own file. I made an effort
to comply with PEP8 standards, but will keep revisiting.

The interpreter is powered by an Intcode which is represented here as
a list. The two other important properties of the Interpreter, the
relative base and the pointer, are also recorded. Otherwise there is
an initialization method, the interpreter cycle itself, and a suite of
helper funcitons.

"""


class Interpreter:
    def __init__(self, intcode):
        self.intcode = intcode
        self.relative_base = 0
        self.pointer = 0

    def instruction(self, number):
        # Convert the instruction int into a 5-element list broken
        # into component digits.
        answer = [0] * 5
        for i in range(5):
            answer[i] = number % 10
            number = number // 10
        return answer

    def pull_value(self, address):
        # Read a value from the Intcode.
        # Even if the index is from outside the list's bounds, this
        # will return a 0.
        if address >= len(self.intcode):
            return 0
        elif address < 0:
            raise Exception("Out of bounds memory call")
        else:
            return self.intcode[address]

    def read_param(self, mode, address):
        # This performs a read from the Intcode taking potential modes
        # into account.
        if mode == 0:
            return self.pull_value(self.pull_value(address))
        elif mode == 1:
            return self.pull_value(address)
        elif mode == 2:
            return self.pull_value(self.relative_base \
                                   + self.pull_value(address))
        else:
            raise Exception("Incorrect mode selected")

    def write_param(self, mode, address, value):
        # This writes to the Intcode. It should be the only method that
        # writes directly to the Intcode. It can take potential modes
        # into account.
        address = self.pull_value(address)
        
        if mode == 2:
            address += self.relative_base
        elif mode != 0:
            raise Exception("Incorrect mode selected")

        if address >= len(self.intcode):
            self.intcode.extend([0] * (address + 1 - len(self.intcode)))
        elif address < 0:
            raise Exception("Out of bounds memory call")
        self.intcode[address] = value

    def run_interpreter(self, signal = 0):
        # The heart of the Interpreter class, this will loop until
        # it produces an output (opcode 4), halts (opcode 99), or
        # encounters an error.
        a_set = {1, 2, 4, 5, 6, 7, 8, 9}
        b_set = {1, 2, 5, 6, 7, 8}
        
        while True:
            # Halt command
            if self.intcode[self.pointer] == 99:
                return None
            
            instruction = self.instruction(self.intcode[self.pointer])
            opcode = (10 * instruction[1]) + instruction[0]

            if opcode in a_set:
                a = self.read_param(instruction[2], self.pointer + 1)
            if opcode in b_set:
                b = self.read_param(instruction[3], self.pointer + 2)

            # Addition
            if opcode == 1:
                self.write_param(instruction[4], self.pointer + 3, a + b)
                self.pointer += 4

            # Multiplication
            elif opcode == 2:
                self.write_param(instruction[4], self.pointer + 3, a * b)
                self.pointer += 4
                
            # Input
            elif opcode == 3:
                self.write_param(instruction[2], self.pointer + 1, signal)
                self.pointer += 2
                return -1

            # Output
            elif opcode == 4:
                self.pointer += 2
                return a

            # Not equal to zero
            elif opcode == 5:
                if a != 0:
                    self.pointer = b
                else:
                    self.pointer += 3

            # Equal to zero
            elif opcode == 6:
                if a == 0:
                    self.pointer = b
                else:
                    self.pointer += 3

            # Less than comparison
            elif opcode == 7:
                if a < b:
                    c = 1
                else:
                    c = 0
                self.write_param(instruction[4], self.pointer + 3, c)
                self.pointer += 4
                
            # Equality comparison
            elif opcode == 8:
                if a == b:
                    c = 1
                else:
                    c = 0
                self.write_param(instruction[4], self.pointer + 3, c)
                self.pointer += 4

            # Adjust the relative base
            elif opcode == 9:
                self.relative_base += a
                self.pointer += 2

            # Break if a bad opcode
            else:
                raise Exception("Bad opCode call")
