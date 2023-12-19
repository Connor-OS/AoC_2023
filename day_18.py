TEST = False
in_file = "./resources/day_18_test.txt" if TEST else "./resources/day_18_input.txt"

directions = {"R": (0, 1), "L": (0, -1), "D": (1, 0), "U": (-1, 0)}
dirs = ["R", "D", "L", "U"]

import numpy as np
from queue import Queue


def file_lines():
    with open(in_file) as file:
        for line in file:
            """Custom iteration logic goes here"""
            line = line.strip()
            line = line.split()
            direction, steps, colour = line
            yield direction, int(steps)


def file_lines_2():
    with open(in_file) as file:
        for line in file:
            """Custom iteration logic goes here"""
            line = line.strip()
            line = line.split()
            direction, steps, colour = line
            steps = colour[2:7]
            direction = dirs[int(colour[7])]

            yield direction, int(steps, 16)


def question_1():
    """Answer to the first question of the day"""

    count, start, grid = construct_grid(file_lines)
    start = (start[0] + 1, start[1] + 1)
    count += flood_fill(start, grid)

    return count


def construct_grid(read_file):
    x, y = 0, 0
    x_max, y_max = 0, 0
    x_min, y_min = 0, 0
    for direction, steps in read_file():

        dy, dx = directions[direction]
        dx *= steps
        dy *= steps

        x += dx
        y += dy

        if x > x_max:
            x_max = x
        if y > y_max:
            y_max = y

        if x < x_min:
            x_min = x
        if y < y_min:
            y_min = y

    grid = np.empty([y_max - y_min + 1, x_max - x_min + 1], str)
    grid[:] = " "
    x, y = -x_min, -y_min
    start = (y, x)
    count = 1
    for direction, steps in file_lines():
        dy, dx = directions[direction]
        for step in range(steps):
            grid[y, x] = direction
            x += dx
            y += dy
            count += 1

    return count, start, grid


def flood_fill(start, grid):
    count = 0
    frontier = Queue()
    frontier.put(start)
    reached = set()
    reached.add(start)

    while not frontier.empty():
        current = frontier.get()
        for d in ["R", "L", "D", "U"]:
            next = tuple(map(sum, zip(current, directions[d])))
            if next not in reached and grid[*next] == " ":
                count += 1
                frontier.put(next)
                reached.add(next)
    return count


def construct_grid_lines(read_file):
    x, y = 0, 0
    lines = []
    perimiter_area = 0
    for direction, steps in read_file():
        perimiter_area += steps
        if direction == "U":
            y -= steps
        if direction == "D":
            y += steps
        if direction == "R":
            lines.append((x, x + steps, y, "R"))
            x += steps
        if direction == "L":
            lines.append((x, x - steps, y, "L"))
            x -= steps
    return lines, perimiter_area


def question_2():
    """Answer to the second question of the day"""
    lines, perimiter_area = construct_grid_lines(file_lines_2)
    shoe_lace_area = 0
    for x_1, x_2, y, direction in lines:
        shoe_lace_area += (x_2 - x_1) * y

    # Picks theorem
    area = abs(shoe_lace_area) + perimiter_area / 2 + 1

    return int(area)


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")
