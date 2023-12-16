TEST = False
in_file = "./resources/day_16_test.txt" if TEST else "./resources/day_16_input.txt"

import numpy as np
from copy import deepcopy as copy


def file_lines():
    with open(in_file) as file:
        grid = []
        energized_grid = []
        for line in file:
            """Custom iteration logic goes here"""
            line = line.strip()
            grid.append([i for i in line])
            energized_grid.append([0 for _ in line])
        return np.array(grid), np.array(energized_grid)


def question_1():
    """Answer to the first question of the day"""
    mirrors, path = file_lines()
    shoot_beam((0, 0), (1, 0), mirrors, path, {})

    return find_answer(path)


def shoot_beam(pos, direction, mirrors, path, mem):
    while True:

        x, y = pos
        dx, dy = direction

        # energise current tile
        path[*pos] += 1

        # update pos
        x += dx
        y += dy

        if x < 0 or y < 0 or x >= len(path) or y >= len(path[0]):
            return

        pos = (x, y)

        # check and update stored locations
        if mem.get((pos, direction)):
            return
        mem[(pos, direction)] = True

        # update direction
        match mirrors[*pos]:
            case ".":
                pass
            case "|":
                if dy:
                    shoot_beam(pos, (1, 0), mirrors, path, mem)
                    shoot_beam(pos, (-1, 0), mirrors, path, mem)
                    return
            case "-":
                if dx:
                    shoot_beam(pos, (0, 1), mirrors, path, mem)
                    shoot_beam(pos, (0, -1), mirrors, path, mem)
                    return
            case "/":
                shoot_beam(pos, (-dy, -dx), mirrors, path, mem)
                return
            case "\\":
                shoot_beam(pos, (dy, dx), mirrors, path, mem)
                return


def find_answer(path):
    answer = 0
    for row in path:
        for col in row:
            if col > 0:
                answer += 1
    return answer

def question_2():
    """Answer to the second question of the day"""
    mirrors, path = file_lines()
    answers = []
    length = len(path)-1
    for i in range(length):

        local_path = copy(path)
        shoot_beam((i, 0), (0, 1), mirrors, local_path, {})
        answers.append(find_answer(local_path))

        local_path = copy(path)
        shoot_beam((i, length), (0, -1), mirrors, local_path, {})
        answers.append(find_answer(local_path))

        local_path = copy(path)
        shoot_beam((0, i), (1, 0), mirrors, local_path, {})
        answers.append(find_answer(local_path))

        local_path = copy(path)
        shoot_beam((length, i), (-1, 0), mirrors, local_path, {})
        answers.append(find_answer(local_path))

    answer = max(answers)
    return answer


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")
