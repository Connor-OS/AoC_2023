from queue import PriorityQueue, Queue

TEST = False
in_file = "./resources/day_23_test.txt" if TEST else "./resources/day_23_input.txt"

import numpy as np
from copy import deepcopy as copy

wrong_directions = {"<": [0, 1],
                    ">": [0, -1],
                    "v": [-1, 0],
                    "^": [1, 0]
                    }


def file_lines():
    with open(in_file) as file:
        graph = []
        for line in file:
            """Custom iteration logic goes here"""
            line = line.strip()
            graph.append([i for i in line])
        return np.array(graph)

def question_1():
    """Answer to the first question of the day"""
    answer = None
    graph = file_lines()

    frontier = PriorityQueue()
    start = (0, 1)
    goal = (len(graph) - 1, len(graph[0]) - 2)

    frontier.put((start, 0))
    came_from = dict()
    cost_so_far = dict()
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()
        pos, steps = current

        # where we've been up untill now
        position = pos
        path = [position]
        while position:
            position = came_from[position]
            if position:
                position = position[0]
                path.append(position)

        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            x, y = pos[0] + dx, pos[1] + dy
            if (0 <= x < len(graph) and 0 <= y < len(graph[0]) and graph[x, y] != "#"
                    and wrong_directions.get(graph[x, y]) != [dx, dy] and (x, y) not in path):

                new_cost = cost_so_far[pos] + 1
                next = (x, y)

                if next not in cost_so_far or new_cost > cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost
                    frontier.put((next, priority))
                    came_from[next] = current

    best = 10000000
    for i in cost_so_far:
        if i == goal and cost_so_far[i] < best:
            print(i, cost_so_far[i])
            best = cost_so_far[i]

    output(goal, came_from, graph)

    return best


def output(current, came_from, graph):
    path = [current]
    while current:
        current = came_from[current]
        if current:
            current = current[1]
            path.append(current)

    for i, row in enumerate(graph):
        for j, col in enumerate(row):
            if (i, j) in path and graph[i, j] not in ["<", ">", "v"]:
                print("O", end="")
            else:
                print(col, end="")

        print()


def prune(grid):
    current = (0, 1)
    graph = {current: set()}

    node, dist = follow_edge((0, 1), (1, 0), grid)
    graph[current].add((node, dist))
    if node not in graph:
        graph[node] = set()
    graph[node].add((current, dist))

    visited = [current]
    frontier = [(node, [-1, 0])]

    while frontier:
        current, wrong_direction = frontier.pop()
        x, y = current
        # if x == 22 and y == 21:
        #     continue
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            if (0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0])
                    and grid[x + dx, y + dy] != "#"
                    and [dx, dy] != wrong_direction):
                node, dist = follow_edge(current, (dx, dy), grid)


                graph[current].add((node, dist))
                if node not in graph:
                    graph[node] = set()
                graph[node].add((current, dist))

                if node not in visited:
                    frontier.append((node, [-dx, -dy]))

        visited.append(current)

    return graph


graph = prune(file_lines())

def question_2():
    """Answer to the second question of the day"""
    answer = None
    grid = file_lines()

    graph = prune(grid)

    for node in graph:
        print(node, graph[node])

    best = recursolve((0, 1), [], 0)
    # best = bfs(0,1, graph)

    return best


@cache
def recursolve(node, visited, dist):
    if node == (140, 139):
        print(dist, end="")
        for v in visited:
            print(f" -> {v}", end="")
        print()
        return dist

    neighbours = graph[node]

    dead_end = True
    for n in neighbours:
        if n[0] not in visited:
            dead_end = False
    if dead_end:
        return 0

    visited.append(node)

    return max([recursolve(neighbour[0], graph, copy(visited), dist+neighbour[1]) for neighbour in neighbours if neighbour[0] not in visited])


def follow_edge(pos, dir, grid):
    dx, dy = dir
    x, y = pos
    x += dx
    y += dy

    visited = [pos, (x, y)]
    while True:
        available = ([(x + dx, y + dy) for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]
                      if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0])
                      and grid[x + dx, y + dy] != "#"
                      and (x + dx, y + dy) not in visited])

        if len(available) > 1:
            return (x, y), len(visited)-1

        if len(available) == 0:
            return (x, y), len(visited)-1
        else:
            # print(available)
            x, y = available[0]
            visited.append((x, y))


if __name__ == '__main__':
    # answer_1 = question_1()
    # print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")
