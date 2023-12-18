from functools import cache

TEST = True
in_file = "./resources/day_17_test.txt" if TEST else "./resources/day_17_input.txt"

mem = {}
directions = {"R": (0, 1), "L": (0, -1), "D": (1, 0), "U": (-1, 0)}

import numpy as np
from copy import deepcopy as dcopy

with open(in_file) as file:
    grid = []
    for line in file:
        """Custom iteration logic goes here"""
        line = line.strip()
        grid.append([int(i) for i in line])
    grid = np.array(grid)


def question_1():
    """Answer to the first question of the day"""
    answer = None
    # print(grid)
    # simple bfs

    # add neighbours to queue. add crruent square to visited add
    answer = bfs()

    return answer


class node():

    def __init__(self, tile):
        if len(tile) == 2:
            self.cost = grid[*tile]
        else:
            x,y,_ = tile
            self.cost = grid[x, y]
        self.dist = 10000000
        self.direction = (0, 0)
        self.steps = 0
        self.prev = None

    def __str__(self):
        return f"{self.cost} {self.dist} {self.direction} {self.steps} {self.prev}"

    def set_dist(self, distance, direction, steps, prev):
        self.dist = distance
        self.direction = direction
        self.steps = steps
        self.prev = prev




def shortest_dist(routes, visited):
    return_tile = None
    dist = 10000000
    for tile in routes:
        if routes[tile].dist <= dist and tile not in visited:
            dist = routes[tile].dist
            return_tile = tile
    return return_tile


def bfs():
    start = (0, 0)

    routes = {(0, 0): node((0, 0))}
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            # routes[(i, j)] = node((i, j))
            for d in ["R", "L", "D", "U"]:
                routes[(i, j, d)] = node((i, j))

    routes[(0, 0)].set_dist(0, (0, 0), 1, None)

    visited = {}
    while len(visited) < len(routes):
        # pop current shortest node
        tile = shortest_dist(routes, visited)
        # print(tile)
        # for new_tile in routes[tile].neighbours():
        current_direction = routes[tile].direction
        for d in ["R", "L", "D", "U"]:
            new_tile = tuple(map(sum, zip(tile[:2], directions[d])))
            if routes[tile].steps == 3 and d == current_direction:
                continue

            new_tile = new_tile + (d,)

            if new_tile not in routes:
                continue

            new_dist = routes[tile].dist + routes[new_tile].cost
            if new_dist < routes[new_tile].dist:
                routes[new_tile].set_dist(new_dist, d,
                                          routes[tile].steps + 1 if current_direction == d else 1, tile)
        visited[(tile] = routes[tile]
        # print(routes[tile])
        # routes.pop(tile)

    for i in routes:
        print(i, routes[i].dist)

    #     visited[tile] = tile_dist
    print(visited[(1, 4, "D")])

    output(visited, (1,4,"D"))
    # print(visited[(140, 140, "R")])
    # print(visited[(140, 140, "L")])
    # print(visited[(140, 140, "U")])
    # print(visited[(140, 140, "D")])

    # for i in visited:
    #     print(i, visited[i])

def output(visited, end_node):
    path = [end_node]
    while end_node:
        # print(end_node)
        end_node = visited[end_node].prev
        if end_node:
            path.append(end_node[:2])
    # print(path)

    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if (i,j) in path:
                print("#",end="")
            else:
                print(col, end="")

        print()



def question_2():
    """Answer to the second question of the day"""
    answer = None

    return answer


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    # answer_2 = question_2()
    # print(f"Question 2 answer is: {answer_2}")
