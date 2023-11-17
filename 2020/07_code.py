"""Day 7 of the Advent of Code 2020



"""    

def readFile(fileName):
    rules_raw = open(fileName).read().strip().split('\n')
    rule_color = {}
    rule_amount = {}
    for r in rules_raw:
        a_rule = r.rstrip().split(' contain ')
        o_temp = a_rule[0].split(' ')
        outside = o_temp[0] + ' ' + o_temp[1]
        inside = a_rule[1].split(', ')

        rule_amount[outside] = []
        rule_color[outside] = []

        if inside[0] != 'no other bags.':
            for bag in inside:
                items = bag.split(' ')
                amount = int(items[0])
                color = items[1] + ' ' + items[2]
            
                rule_amount[outside].append(amount)
                rule_color[outside].append(color)
                
    return rule_amount, rule_color


def isContained(rule_color, start, color):
    if len(rule_color[start]) == 0:
        return False
    else:
        result = False
        for a_bag in rule_color[start]:
            if a_bag == color:
                return True
            else:
                result = \
                    result or isContained(rule_color, a_bag, color)
        return result

    
def containers(rule_color, my_color):
    count = 0
    for a_bag in rule_color:
        count += isContained(rule_color, a_bag, my_color)
    return count


def bag_contains(rule_amount, rule_color, my_color):
    if len(rule_color[my_color]) == 0:
        return 1

    else:
        count = 1
        for i in range(len(rule_color[my_color])):
            count += \
                rule_amount[my_color][i] * \
                bag_contains(rule_amount, rule_color, \
                             rule_color[my_color][i])
            
        return count


def main():
    input_amount, input_color = readFile('input_07_1.txt')
    print('Part 1:', containers(input_color, 'shiny gold'))
    print('Part 2:', bag_contains(input_amount, input_color, 'shiny gold')-1)
    

main()
