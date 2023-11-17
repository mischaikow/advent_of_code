"""Day 18 - 2020 Advent of Code

Interpreting arithmetic expressions
"""

import re


def readFile(fileName):
    with open(fileName) as f:
        formulas = f.read().strip().split('\n')
    return formulas


def calculation(formula, step):
    started = False
    result = 0
    operation = 'z'
    while step < len(formula):
        char = formula[step]

        if char == '+':
            operation = '+'
        elif char == '*':
            operation = '*'
        elif char == '(':
            new = calculation(formula, step+1)
            started = True
            step = new[1]
            if operation == '+':
                result += new[0]
            elif operation == '*':
                result *= new[0]
            else:
                result = new[0]
                
        elif char == ')':
            return result, step
        elif started == False:
            result = char
            started = True
        else:
            if operation == '+':
                result += char
            elif operation == '*':
                result *= char

        step += 1

    return result
    

def calculation_2(formula):
    no_plus = False
    while len(formula) > 1:
        i = 0
        new_formula = []
        operation = ''
        while i < len(formula):
            char = formula[i]

            if char == '+':
                operation = '+'
            elif char == '*':
                operation = '*'
                if not no_plus:
                    new_formula.append('*')
            elif char == '(':
                answer = calculation_2(formula[i+1:])
                depth = 1
                if operation == '+':
                    new_formula[-1] += answer
                elif operation == '*':
                    if no_plus:
                        new_formula[-1] *= answer
                    if not no_plus:
                        new_formula.append(answer)
                else:
                    new_formula.append(answer)
                while depth > 0:
                    i += 1
                    if formula[i] == '(':
                        depth += 1
                    elif formula[i] == ')':
                        depth -= 1
            elif char == ')':
                if i == 1:
                    return formula[0]
                else:
                    break
            elif i == 0:
                new_formula.append(char)
            else:
                if operation == '+':
                    new_formula[-1] += char
                elif operation == '*' and no_plus:
                    new_formula[-1] *= char
                else:
                    new_formula.append(char)

            i += 1
        formula = new_formula
        no_plus = True

    return formula[0]

def sum_results(formulas):
    answer1 = answer2 = 0
    for formula in formulas:
        p = re.compile("\(|\)|\d+|\+|\*")
        chopped = p.findall(formula)
        for i, val in enumerate(chopped):
            if val.isdigit():
                chopped[i] = int(val)
        answer1 += calculation(chopped, 0)
        answer2 += calculation_2(chopped)
    return answer1, answer2


def main():
    formulas = readFile('input_18_1.txt')
    results = sum_results(formulas)
    print('Part 1:', results[0])
    print('Part 2:', results[1])
    return None


main()
