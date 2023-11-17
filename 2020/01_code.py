"""Day 1 of the 2020 Advent of Code event

Wordy and brute force
"""

def fileReader(fileName):
    input_file = open(fileName, 'r')
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace('\n', '')
        inputs_raw[i] = int(inputs_raw[i])
    return inputs_raw
    

def findPairProd(fileName):
    arr = fileReader(fileName)
    #arr = [1721, 979, 366, 299, 675, 1456]
    
    for ind_a in range(len(arr)):
        if arr[ind_a] <= 2020:
            for ind_b in range(ind_a + 1, len(arr)):
                if arr[ind_a] + arr[ind_b] == 2020:
                    return arr[ind_a] * arr[ind_b]

                
def findTripleProd(fileName):
    arr = fileReader(fileName)
    #arr = [1721, 979, 366, 299, 675, 1456]

    for ind_a in range(len(arr)):
        if arr[ind_a] < 2020:
            for ind_b in range(ind_a + 1, len(arr)):
                if arr[ind_a] + arr[ind_b] < 2020:
                    for ind_c in range(ind_b + 1, len(arr)):
                        if arr[ind_a] + arr[ind_b] + arr[ind_c] == 2020:
                            return arr[ind_a] * arr[ind_b] * arr[ind_c]
    

def main():
    print("Pair product:", findPairProd("input_01_1.txt"))
    print("Triple product:", findTripleProd("input_01_1.txt"))


main()
