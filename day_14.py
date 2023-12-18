TEST = True
in_file = "./resources/day_14_test.txt" if TEST else "./resources/day_14_input.txt"

import numpy as np

def file_lines():
    with open(in_file) as file:
        grid = []
        for line in file:
            """Custom iteration logic goes here"""
            grid.append([i for i in line.strip()])
        return np.array(grid)

def question_1():
    """Answer to the first question of the day"""
    answer = 0
    grid = file_lines()
    grid = np.rot90(grid)
    grid = move_stones(grid)

    for row in grid:
        for pos, stone in enumerate(row):
            if stone == "O":
                answer += len(row) - pos

    return answer

def move_stones(grid):
    for row in grid:
        for pos, stone in enumerate(row):
            if stone == "O":
                row = move_stone(row, pos)
    return grid

def move_stone(row, place):
    while place > 0 and row[place-1] == ".":
        row[place] = "."
        place = place - 1
        row[place] = "O"
    return row

def find_answer(grid):
    answer = 0
    for row in grid:
        for pos, stone in enumerate(row):
            if stone == "O":
                answer += len(row) - pos
    return answer

def question_2():
    """Answer to the second question of the day"""
    answer = 0
    uniques = {}
    grid = file_lines()
    grid = np.rot90(grid)
    for i in range(1, 4 * 1000000001):
        grid = move_stones(grid)
        grid = np.rot90(grid, 3)
        # if i % 20 == 0:
        #     print(uniques)
        #     print(find_answer(grid))

    #     ans = find_answer(grid)
    #     flat_grid = grid.tolist()
    #     if flat_grid not in uniques:
    #         uniques[flat_grid] = ans
    #     else:
    #         break
    #
    # # print(uniques)
    #
    # print(uniques.values[[10000000%len(uniques)]])


    return answer



if __name__ == '__main__':
    # answer_1 = question_1()
    # print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")
