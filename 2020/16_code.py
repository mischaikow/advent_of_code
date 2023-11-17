"""Day 16 of the 2020 Advent of Code


"""

def readFile(fileName):
    with open(fileName) as f:
        t1, t2, t3 = f.read().split('\n\n')

    rules = {}
    t1 = t1.strip().split('\n')
    for a_rule in t1:
        index, content = a_rule.split(': ')
        content = content.split(' or ')
        new_content = content[0].split('-') + content[1].split('-')
        rules[index] = [int(i) for i in new_content]

    discard, str_ticket = t2.strip().split('\n')
    list_ticket = str_ticket.strip().split(',')
    my_ticket = [int(i) for i in list_ticket]

    nearby_tickets = []
    temp_tickets = t3.strip().split('\n')[1:]
    for a_ticket in temp_tickets:
        temp = a_ticket.strip().split(',')
        nearby_tickets.append([int(i) for i in temp])

    return rules, my_ticket, nearby_tickets


def isBadMatch(conditionals, value):
    return conditionals[0] > value \
        or (conditionals[1] < value < conditionals[2]) \
        or conditionals[3] < value


def badTicket(ticket, rules):
    for a_val in ticket:
        if all([isBadMatch(rules[a_rule], a_val) for a_rule in rules]):
            return a_val
    return 0


def invalidRatio(rules, tickets):
    rejects = 0
    for a_ticket in tickets:
        rejects += badTicket(a_ticket, rules)
    return rejects


def determineFields(rules, my_ticket, tickets):
    result = {}
    answer = {}
    for a_rule in rules:
        result[a_rule] = [True] * len(my_ticket)
        answer[a_rule] = -1

    for a_ticket in tickets:
        if badTicket(a_ticket, rules) == 0:
            for i in range(len(a_ticket)):
                for a_rule in rules:
                    if result[a_rule][i] \
                       and isBadMatch(rules[a_rule], a_ticket[i]):
                        result[a_rule][i] = False
        
    cycle = True
    while cycle:
        cycle = False
        for a_rule in rules:
            if sum(result[a_rule]) <= 1:
                if answer[a_rule] < 0:
                    for i in range(len(a_ticket)):
                        if result[a_rule][i]:
                            answer[a_rule] = i
                            break
                        
                    for a_rule_2 in rules:
                        if answer[a_rule_2] < 0 and a_rule != a_rule_2:
                            result[a_rule_2][answer[a_rule]] = False

            else:
                cycle = True
                        
    return my_ticket[answer['departure location']] \
        * my_ticket[answer['departure station']] \
        * my_ticket[answer['departure platform']] \
        * my_ticket[answer['departure track']] \
        * my_ticket[answer['departure date']] \
        * my_ticket[answer['departure time']]


def main():
    rules, my_ticket, nearby_tickets = readFile('input_16_1.txt')
    print('Part 1:', invalidRatio(rules, nearby_tickets))
    print('Part 2:', determineFields(rules, my_ticket, nearby_tickets))
    return None


main()
