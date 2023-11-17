from intcode import packet
from intcode import interpreter

def part_1(data_raw):
    data_packet = interpreter.hex_interpreter(data_raw)
    return part_1_helper(data_packet)

def part_1_helper(data_packet):
    ans = data_packet.version_ID
    if data_packet.type_ID != 4:
        for p in data_packet.contents:
            ans += part_1_helper(p)
    return ans

def part_2(data_raw):
    data_packet = interpreter.hex_interpreter(data_raw)
    return data_packet.compute()

def file_reader(file_name):
    input_file = open(file_name, 'r')
    data_raw = input_file.readline().replace('\n', '')
    return data_raw

print(part_1(file_reader('input_16.txt')))
print(part_2(file_reader('input_16.txt')))