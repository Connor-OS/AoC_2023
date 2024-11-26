TEST = False
in_file = "./resources/day_21_test.txt" if TEST else "./resources/day_21_input.txt"

import numpy as np

steps = 26501365


def file_lines():
    with open(in_file) as file:
        graph = []
        for line in file:
            """Custom iteration logic goes here"""
            line = line.strip()
            graph.append([i for i in line])
        graph = np.array(graph)
        #
        # big_graph = np.concatenate((graph, graph), axis=0)
        # big_graph = np.concatenate((big_graph, graph), axis=0)
        # even_bigger_graph = np.concatenate((big_graph, big_graph), axis=1)
        # even_bigger_graph = np.concatenate((even_bigger_graph, big_graph), axis=1)
        #
        # graph = even_bigger_graph

    return graph


def question_1():
    """Answer to the first question of the day"""

    grid = file_lines()
    grid = np.array([["."] * 30] * 30)
    mid = {(int(len(grid) / 2), int(len(grid[0]) / 2))}
    positions = grid_solver(steps, grid, mid)
    # output(positions, grid)
    answer = positions
    return answer


def output(positions, grid):
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if (i, j) in positions and grid[i, j] != "#":
                print("O", end="")
            else:
                print(grid[i, j], end="")
        print()


def question_2():
    """Answer to the second question of the day"""

    # grid = file_lines()
    g = 131

    grid = np.array([["."] * g] * g)
    grid = file_lines()

    #initialisation positions
    mid = {(int(g / 2), int(g / 2))}

    top_mid = {(-1, int(g / 2))}
    bot_mid = {(g, int(g / 2))}
    left_mid = {(int(g / 2), -1)}
    right_mid = {(int(g / 2), g)}

    top_left = {(-1, 0)}
    top_right = {(-1, g-1)}
    bot_left = {(g, 0)}
    bot_right = {(g, g-1)}

    positions = 0

    # A
    schema_A = grid_solver(g+10+((steps+1) % 2), grid, mid)
    schema_B = grid_solver(g+10+(steps % 2), grid, mid)

    if int(steps/g) % 2 == 0:
        positions += schema_A * (int(steps/g) - 1)**2
        # print((int(steps/g) - 1)**2, "A")
    else:
        positions += schema_A * int(steps / g) ** 2
        # print(int(steps / g) ** 2, "A")

    # B
    if int(steps / g) % 2 == 0:
        positions += schema_B * (int(steps / g)) ** 2
        # print(int(steps / g) ** 2, "B")
    else:
        positions += schema_B * int((steps / g) - 1) ** 2
        # print(int((steps / g) - 1) ** 2, "B")


    corners = [top_left, top_right, bot_left, bot_right]
    for corner in corners:
        # C
        schema_C = grid_solver(((g + steps) % (2*g)), grid, corner)
        schema_D = grid_solver((steps % (2*g)), grid, corner)

        if int(steps/g) % 2 == 0:
            positions += schema_C * (int(steps/g) - 1)
            # print(int(steps/g - 1), "C")
        else:
            positions += schema_C * int(steps / g)
            # print(int(steps / g), "C")

        # D
        if int(steps / g) % 2 == 0:
            positions += schema_D * (int(steps / g))
            # print(int(steps / g), "D")
        else:
            positions += schema_D * int((steps / g) - 1)
            # print(int((steps / g) - 1), "D")

    mids = [top_mid, left_mid, bot_mid, right_mid]
    for middle in mids:
        # E
        if ((int((g+1)/2) + steps) % (2*g)) < 2 * g - int(g/2):
            schema_E = grid_solver(((int((g+1)/2) + steps) % (2*g)), grid, middle)
        else:
            schema_E = 0

        if ((int((g+1)/2) + steps - g) % (2*g)) < 2 * g - int(g/2):
            schema_F = grid_solver(((int((g+1)/2) + steps - g) % (2*g)), grid, middle)
        else:
            schema_F = 0
        # F
        positions += schema_E
        positions += schema_F

    print((steps+1) ** 2)
    return positions


def grid_solver(steps, grid, positions):
    for step in range(steps):
        temp = set()
        for x, y in positions:
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x + dx, y + dy] != "#":
                    temp.add((x + dx, y + dy))
        positions = temp

    positions = [(x,y) for x,y in positions if 0 <= x < len(grid) and 0 <= y < len(grid[0])]
    # output(positions, grid)
    # print(len(positions))
    return len(positions)


if __name__ == '__main__':
    # answer_1 = question_1()
    # print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")
