class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def part_1(val):
    counter = [0] * 12
    for num in val:
        for i, char in enumerate(num):
            counter[i] += int(char)
    target = len(val) / 2
    gamma, epsilon = 0, 0
    for digit in counter:
        gamma *= 2
        epsilon *= 2
        gamma += int(digit > target)
        epsilon += int(digit <= target)
    return gamma * epsilon

def part_2(feed):
    tree = TreeNode([2])
    for num in feed:
        branch = tree
        for char in num:
            if char == '0':
                if branch.left == None:
                    branch.left = TreeNode([1, num])
                else:
                    branch.left.val[0] += 1
                branch = branch.left
            else:
                if branch.right == None:
                    branch.right = TreeNode([1, num])
                else:
                    branch.right.val[0] += 1
                branch = branch.right

    branch = tree
    while branch.val[0] > 1:
        if branch.right == None or branch.left != None and branch.left.val[0] > branch.right.val[0]:
            branch = branch.left
        else:
            branch = branch.right
    oxygen = branch.val[1]

    branch = tree
    while branch.val[0] > 1:
        if branch.right == None or branch.left != None and branch.left.val[0] <= branch.right.val[0]:
            branch = branch.left
        else:
            branch = branch.right
    co2 = branch.val[1]

    return int(oxygen, 2) * int(co2, 2)
 

def file_reader(file_name):
    input_file = open(file_name, 'r')
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace('\n', '')
    return inputs_raw

print(part_1(file_reader('input_03.txt')))
print(part_2(file_reader('input_03.txt')))
