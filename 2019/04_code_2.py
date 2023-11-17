##  Part one is a math problem
## Two adjacent digits are the same
## Digits are monotonically increasing
## Range is 134799 to 669999 inclusive
## How many 6-digit combos are there?

##  We could build this using a tree of some sort where each node has
## a few rules:
##   - Nodes can be "on" or "off". A node is "on" if repeated digits appear
##         anywhere above. Otherwise the node is "off". If the leaf if "off"
##         the node is not counted
##   - Nodes that match the above node are immediately marked as "on"
##   - Nodes that do not match the above node keep whatever marking the
##         above node has
##   - Each leaf must be within the range to be counted

import math

def digit_count(number):
    return int(math.log10(number)) + 1

def digit(number, n):
    return number // 10**n % 10

def node(number, isOn, defOn):
    if digit_count(number) == 6:
        if not isOn and not defOn:
            print "miss", number
            return 0
        elif number < 134799 or number > 669999:
            return 0
        else:
            print "hit", number
            return 1
    else:
        count = 0
        for i in range(digit(number, 0), 10):
            if i == digit(number, 0):
                if i == digit(number, 1):
                    count += node(number*10 + i, False, defOn)
                else:
                    count += node(number*10 + i, True, defOn)
            else:
                if isOn:
                    count += node(number*10 + i, isOn, True)
                else:
                    count += node(number*10 + i, isOn, defOn)
        return count


count = 0
for i in range(1, 7):
    count += node(i, False, False)
    
print count
