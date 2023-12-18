TEST = False
in_file = "./resources/day_17_test.txt" if TEST else "./resources/day_17_input.txt"

import numpy as np
from queue import PriorityQueue

directions = {"R": (0, 1), "L": (0, -1), "D": (1, 0), "U": (-1, 0)}


with open(in_file) as file:
    graph = []
    for line in file:
        """Custom iteration logic goes here"""
        line = line.strip()
        graph.append([int(i) for i in line])
    graph = np.array(graph)


def question_1():
    """Answer to the first question of the day"""
    answer = None

    frontier = PriorityQueue()
    start = (0, 0)
    goal = (len(graph)-1, len(graph[0])-1)

    frontier.put((start, "", 1), 0)
    came_from = dict()
    cost_so_far = dict()
    came_from[(start, "", 1)] = None
    cost_so_far[(start, "", 1)] = 0

    while not frontier.empty():
        current = frontier.get()
        pos, direc, steps = current

        for d in ["R", "L", "D", "U"]:
            if direc and directions[direc] == tuple(-i for i in directions[d]):
                continue

            if steps == 3 and direc == d:
                continue

            next = tuple(map(sum, zip(pos, directions[d])))
            x,y = next
            if x < 0 or y < 0 or x >= len(graph) or y >= len(graph[0]):
                continue

            new_cost = cost_so_far[current] + graph[*next]

            if direc == d:
                next_steps = steps + 1
            else:
                next_steps = 1
            next = (next, d, next_steps)

            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next,  priority)
                came_from[next] = current

    best = 10000000
    for i in cost_so_far:
        if i[0] == goal and cost_so_far[i] < best:
            print(i, cost_so_far[i])
            best = cost_so_far[i]
            best_route = i

    # output(best_route, came_from)

    return best


def output(current, came_form):
    path = [current]
    while current:
        # print(current)
        current = came_form[current]
        if current:
            path.append(current[0])
    # print(path)

    for i, row in enumerate(graph):
        for j, col in enumerate(row):
            if (i, j) in path:
                print("#", end="")
            else:
                print(col, end="")

        print()




def question_2():
    """Answer to the second question of the day"""
    answer = None

    frontier = PriorityQueue()
    start = (0, 0)
    goal = (len(graph)-1, len(graph[0])-1)

    frontier.put((start, "", 1), 0)
    came_from = dict()
    cost_so_far = dict()
    came_from[(start, "", 1)] = None
    cost_so_far[(start, "", 1)] = 0

    while not frontier.empty():
        current = frontier.get()
        pos, direc, steps = current

        for d in ["R", "L", "D", "U"]:
            if direc and directions[direc] == tuple(-i for i in directions[d]):
                continue

            if steps == 10 and direc == d:
                continue

            if direc and steps < 4 and direc != d:
                continue

            next = tuple(map(sum, zip(pos, directions[d])))
            x,y = next
            if x < 0 or y < 0 or x >= len(graph) or y >= len(graph[0]):
                continue

            new_cost = cost_so_far[current] + graph[*next]

            if direc == d:
                next_steps = steps + 1
            else:
                next_steps = 1
            next = (next, d, next_steps)

            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next,  priority)
                came_from[next] = current

    best = 10000000
    for i in cost_so_far:
        if i[0] == goal and cost_so_far[i] < best:
            print(i, cost_so_far[i])
            best = cost_so_far[i]
            best_route = i

    # output(best_route, came_from)

    return best


if __name__ == '__main__':
    # answer_1 = question_1()
    # print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")
