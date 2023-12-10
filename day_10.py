TEST = False
in_file = "./resources/day_10_test.txt" if TEST else "./resources/day_10_input.txt"

import numpy as np

vert = "|"
horiz = "-"
down_right = "L"
down_left = "J"
up_right = "F"
up_left = "7"

direct_dict = {(1, 0): "D",
               (-1, 0): "U",
               (0, 1): "R",
               (0, -1): "?"}

collision_dict = {("R", "D"): "R",
                  ("R", "U"): "L",
                  ("?", "D"): "L",
                  ("?", "U"): "R",
                  ("U", "R"): "R",
                  ("U", "?"): "L",
                  ("D", "R"): "L",
                  ("D", "?"): "R",
                  }

invert_dict = {"R": "L", "L": "R"}

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
    tunnel_grid = file_lines()
    # find the start
    position = find_start(tunnel_grid)

    # Pick U, R, D, L
    direction = pick_direction(tunnel_grid, position)

    # move square: update position and direction
    direction, position = move_square(tunnel_grid, direction, position)
    count = 1
    while (tunnel_grid[position] != "S"):

        direction, position = move_square(tunnel_grid, direction, position)
        count += 1

    return int(count / 2)


def find_start(tunnel_grid):
    for j, row in enumerate(tunnel_grid):
        for i, col in enumerate(row):
            if col == "S":
                return j, i


def pick_direction(tunnel_grid, position):
    j, i = position
    if tunnel_grid[j - 1, i] in [vert, up_right, up_left]:
        return -1, 0
    if tunnel_grid[j, i + 1] in [horiz, down_left, up_right]:
        return 0, 1
    if tunnel_grid[j + 1, i] in [vert, down_right, down_left]:
        return 1, 0
    if tunnel_grid[j, i - 1] in [horiz, down_right, up_left]:
        return -1, 0


def change_direction(direction, pipe):
    j, i = direction
    if pipe in [vert, horiz]:
        return direction

    if j != 0 and pipe in [down_right, up_right]:
        return 0, 1
    if j != 0 and pipe in [down_left, up_left]:
        return 0, -1

    if i != 0 and pipe in [up_right, up_left]:
        return 1, 0
    if i != 0 and pipe in [down_right, down_left]:
        return -1, 0


def move_square(tunnel_grid, direction, position):
    j, i = position
    dj, di = direction
    position = (j + dj, i + di)
    direction = change_direction(direction, tunnel_grid[position])

    return direction, position


def question_2():
    """Answer to the second question of the day"""
    tunnel_grid = file_lines()
    # find the start
    position = find_start(tunnel_grid)
    start = position

    # Pick U, R, D, L
    direction = pick_direction(tunnel_grid, position)
    tunnel_grid[position] = direct_dict[direction]
    # move square: update position and direction
    direction, position = move_square(tunnel_grid, direction, position)

    # traverse path and convert symbols to directional
    while position != start:
        tunnel_grid[position] = direct_dict.get(direction)
        direction, position = move_square(tunnel_grid, direction, position)

    # for each empty space fid if on left or right of active path
    right = 0
    left = 0
    for j, row in enumerate(tunnel_grid):
        for i, col in enumerate(row):
            if col not in direct_dict.values():
                rl = right_left(tunnel_grid, (j, i))
                if rl == "R":
                    right += 1
                else:
                    left += 1


    return right, left


def right_left(tunnel_grid, position):
    # fire rays in each direction looking for the path
    for dj, di in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        ray_direction = direct_dict[(dj, di)]
        j, i = position
        j += dj
        i += di
        while len(tunnel_grid) > j >= 0 and len(tunnel_grid[0]) > i >= 0 and tunnel_grid[position]:
            if tunnel_grid[j, i] in direct_dict.values():
                # collide in direction of pipe
                if ray_direction == tunnel_grid[j, i]:
                    # back track one to find out
                    if ray_direction in ["U", "D"]:
                        other_directs = ["?", "R"]
                    else:
                        other_directs = ["U", "D"]

                    if j + di < len(tunnel_grid) and i + dj < len(tunnel_grid[0]) and tunnel_grid[j + di, i + dj] in other_directs:
                        return collision_dict[(ray_direction, tunnel_grid[j + di, i + dj])]
                    else:
                        return collision_dict[(ray_direction, tunnel_grid[j - di, i - dj])]

                # colide with path
                else:
                    return collision_dict[(ray_direction, tunnel_grid[j, i])]

            j += dj
            i += di


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is either: {answer_2[0]} or {answer_2[1]} lol")
