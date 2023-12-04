import numpy as np


def question_1():
    with open("./day_3_input.txt") as input:
        #read input into memory
        in_array = np.array([[symbol for symbol in line.strip()] for line in input])
        in_array = np.pad(in_array, 1, 'constant', constant_values=".")

    size = len(in_array)

    total = 0
    for i in range(size):
        j = 0
        while j < size:

            if np.char.isnumeric(in_array[i, j]):
                num = ""
                valid = False
                # while read number
                while in_array[i, j].isnumeric():
                    num += in_array[i][j]
                    if kernal_check(in_array[i-1:i+2, j-1:j+2]):
                        valid = True
                    j += 1
                print(num, valid)
                if valid:
                    total += int(num)
            else:
                j += 1

    print(total)


def kernal_check(in_array):
    print(in_array)
    for line in in_array:
        for symbol in line:
            if symbol not in ["0","1","2","3","4","5","6","7","8","9","."]:
                return True


def question_2():
    with open("./day_3_input.txt") as input:
        # read input into memory
        in_array = np.array([[symbol for symbol in line.strip()] for line in input])
        in_array = np.pad(in_array, 1, 'constant', constant_values=".")

    size = len(in_array)

    total = 0
    for i in range(size):
        for j in range(size):
            if in_array[i, j] == "*":
                adjacency = np.char.isnumeric(in_array[i-1:i+2, j-1:j+2])
                if vertical_adjacency_check(adjacency) or horizontal_adjacency_check(adjacency):
                    total += compute_gear(in_array, i,j)
    print(total)


def compute_gear(in_array, x , y):
    gear_nums = []
    for i in range(x-1, x+2):
        j = y - 1
        while j < y + 2:
            if np.char.isnumeric(in_array[i, j]):
                num = ""
                k = j

                # back up to start of number
                while in_array[i, k].isnumeric():
                    k -= 1
                k += 1

                #read number
                while in_array[i, k].isnumeric():
                    num += in_array[i, k]
                    k += 1

                j = k
                # print(num)
                gear_nums.append(int(num))

            else:
                 j += 1

    # if len(gear_nums) > 2: # edge case involving greater than 3 adjacency, wasn't a problem for my input
    return gear_nums[0] * gear_nums[1]


def vertical_adjacency_check(adjacency):
    adj = 0
    for line in adjacency:
        if True in line:
            adj += 1
    if adj == 2:
        return True

def horizontal_adjacency_check(adjacency):
    for line in adjacency:
        if line[0] == True and line[1] == False and line[2] == True:
            return True