from collections import defaultdict

def explore_1(seen, current, conn):
    if current == 'end':
        return 1
    
    ans = 0
    for n in conn[current]:
        if not(n in seen) or n.isupper():
            dummy = seen.copy()
            dummy.add(n)
            ans += explore_1(dummy, n, conn)

    return ans


def part_1(raw_data):
    conn = defaultdict(list)
    for pair in raw_data:
        a, b = pair.split('-')
        conn[a].append(b)
        conn[b].append(a)

    dummy = set()
    dummy.add('start')
    return explore_1(dummy, 'start', conn)


def explore_2(seen, current, double, conn):
    if current == 'end':
        return 1
    
    ans = 0
    for n in conn[current]:
        if n.isupper() or not(n in seen):
            dummy = seen.copy()
            dummy.add(n)
            ans += explore_2(dummy, n, double, conn)
        elif n in seen and not double and n != 'start':
            ans += explore_2(seen, n, True, conn)

    return ans


def part_2(raw_data):
    conn = defaultdict(list)
    for pair in raw_data:
        a, b = pair.split('-')
        conn[a].append(b)
        conn[b].append(a)

    dummy = set()
    dummy.add('start')
    return explore_2(dummy, 'start', False, conn)

 
def file_reader(file_name):
    input_file = open(file_name, 'r')
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace('\n', '')
    return inputs_raw

print(part_1(file_reader('input_12.txt')))
print(part_2(file_reader('input_12.txt')))
