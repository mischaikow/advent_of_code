"""Day 4 of the 2020 Advent of Code event


"""
import re


def fileReader(fileName):
    with open(fileName) as f:
        inputs_raw = f.readlines()
    inputs_raw = [x.strip() for x in inputs_raw]
    output = [{}]

    for line in inputs_raw:
        if line.strip() == '':
            output.append({})
        else:
            fields = line.split()
            for field in fields:
                field = field.split(':')
                output[-1][field[0]] = field[1]
                
    return output


def fieldCheck(val, field):
    if field == 'byr':
        return val.isdigit() and 1920 <= int(val) <= 2002
            
    elif field == 'iyr':
        return val.isdigit() and 2010 <= int(val) <= 2020

    elif field == 'eyr':
        return val.isdigit() and 2020 <= int(val) <= 2030

    elif field == 'hgt':
        front = val[:-2]
        back = val[-2:]
        if front.isdigit():
            if back == 'cm' and 150 <= int(front) <= 193:
                return True
            elif back == 'in' and 59 <= int(front) <= 76:
                return True
            else:
                return False

    elif field == 'hcl':
        p = re.compile('^#[0-9a-f]{6}$')
        return re.search(p, val) is not None

    elif field == 'ecl':
        eyes = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        return val in eyes

    elif field == 'pid':
        p = re.compile('^[0-9]{9}$')
        return re.search(p, val) is not None

    return False


def docCheck(docs):
    simple_count, hard_count = 0, 0
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    
    for doc in docs:
        simple_check, hard_check = True, True
        for field in fields:
            if field in doc:
                hard_check *= fieldCheck(doc[field], field)
            elif field not in doc:
                simple_check, hard_check = False, False

        simple_count += simple_check
        hard_count += hard_check

    return simple_count, hard_count


def main():
    fileName = 'input_04_1.txt'
    organized = fileReader(fileName)
    basic, hard = docCheck(organized)
    print('Part 1:', basic)
    print('Part 2:', hard)
    return None


main()
