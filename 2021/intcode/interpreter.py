from .packet import Packet

def hex_interpreter(hex_feed):
    binary = { 
            '0': '0000', 
            '1': '0001',
            '2': '0010',
            '3': '0011',
            '4': '0100',
            '5': '0101',
            '6': '0110',
            '7': '0111',
            '8': '1000',
            '9': '1001',
            'A': '1010',
            'B': '1011',
            'C': '1100',
            'D': '1101',
            'E': '1110',
            'F': '1111'
            }

    result = []
    for val in hex_feed:
        result.append(binary[val])
    binary_feed = ''.join(result)

    return binary_interpreter(0, binary_feed)[1]


def binary_interpreter(index, binary_feed):
    version_ID = int(binary_feed[index+0:index+3], 2)
    type_ID = int(binary_feed[index+3:index+6], 2)
    #print(binary_feed[index:index+11], version_ID, type_ID, int(binary_feed[index+6]))
    if type_ID == 4:
        # Literal Value
        index += 6
        content_str = ''
        while True:
            content_str += binary_feed[index+1:index+5]
            if binary_feed[index] == '0':
                index += 5
                break
            index += 5
        content = int(content_str, 2)
    else:
        index += 6
        if binary_feed[index] == '0':
            content_distance = int(binary_feed[index+1:index+1+15], 2)
            index, content = serial_binary_interpreter(index+16, index+16+content_distance, binary_feed)
        elif binary_feed[index] == '1':
            count_loops = int(binary_feed[index+1:index+1+11], 2)
            index += 12
            content = []
            for _ in range(count_loops):
                index, temp = binary_interpreter(index, binary_feed)
                content.append(temp)
        else:
            content = 'ERROR'

    packet = Packet(version_ID, type_ID, content)

    return index, packet


def serial_binary_interpreter(index, end_point, binary_feed):
    content = []
    while index < end_point-1:
        index, temp = binary_interpreter(index, binary_feed)
        content.append(temp)

    return index, content