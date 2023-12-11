TEST = False
in_file = "./resources/day_11_test.txt" if TEST else "./resources/day_11_input.txt"

import numpy as np


def file_lines():
    with open(in_file) as file:
        grid = []
        for line in file:
            """Custom iteration logic goes here"""
            line = line.strip()
            grid.append([i for i in line])
        grid = np.array(grid)
        return grid


def question_1():
    """Answer to the first question of the day"""
    grid = file_lines()
    grid = expand_grid(grid)

    stars = []
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if grid[i, j] == "#":
                stars.append((i, j))

    return star_dists(stars)


def expand_grid(grid):
    i = 0
    while i < len(grid):
        if len(set(grid[i])) == 1:
            grid = np.insert(grid, i, ".", axis=0)
            i += 1
        i += 1

    i = 0
    while i < len(grid.transpose()):
        if len(set(grid[:, i])) == 1:
            grid = np.insert(grid, i, ".", axis=1)
            i += 1
        i += 1

    return grid


def expand_stars(stars, grid, param=2):
    row_expansions = []
    col_expansions = []

    for i, row in enumerate(grid):
        if len(set(row)) == 1:
            row_expansions.append(i)

    for i, col in enumerate(grid.transpose()):
        if len(set(col)) == 1:
            col_expansions.append(i)

    # expand star locations
    new_stars = []
    for star in stars:
        x, y = star
        for i in row_expansions:
            if star[0] > i:
                x += param - 1

        for j in col_expansions:
            if star[1] > j:
                y += param - 1

        new_stars.append([x, y])
    return new_stars


def star_dists(stars):
    total = 0
    for i, star_1 in enumerate(stars):
        for j, star_2 in enumerate(stars[i + 1:]):
            total += abs(star_1[0] - star_2[0]) + abs(star_1[1] - star_2[1])
    return total


def question_2():
    """Answer to the second question of the day"""
    expansion_parameter = 1000000
    grid = file_lines()

    stars = []
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if grid[i, j] == "#":
                stars.append([i, j])

    stars = expand_stars(stars, grid, expansion_parameter)

    return star_dists(stars)


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")
