TEST = False
in_file = "./resources/day_8_test.txt" if TEST else "./resources/day_8_input.txt"

from math import lcm

instructions = "LR" if TEST else "LRRRLRRRLRRLRLRRLRLRRLRRLRLLRRRLRLRLRRRLRRRLRLRLRLLRRLLRRLRRRLLRLRRRLRLRLRRRLLRLRRLRRRLRLRRRLLRLRRLRRRLRRLRRLRLRRLRRRLRLRRRLRRLLRRLRRLRLRRRLRRLRRRLRRRLRLRRLRLRRRLRLRRLRRLRRRLRRRLRRRLLRRLRRRLRLRLRLRRRLRLRLRRLRRRLRRRLRRLRRLLRLRRLLRLRRLRRLLRLLRRRLLRRLLRRLRRLRLRLRRRLLRRLRRRR"

def file_lines():
    with open(in_file) as file:
        node_system = {}
        for line in file:
            """Custom iteration logic goes here"""

            line = line.strip()
            key, val = line.split(" = ")
            val = val.strip("(").strip(")").split(", ")
            node_system[key] = tuple(val)

        return node_system


def question_1():
    """Answer to the first question of the day"""

    pos = "AAA"
    dist = cycle(pos, file_lines())

    return dist


def right_left(pos, nodes, rl):

    l, r = nodes[pos]
    if rl == "L":
        return l
    else:
        return r


def cycle(pos, nodes):

    dist = 0
    while True:
        for instruction in instructions:
            pos = right_left(pos, nodes, instruction)
            dist += 1
            if pos == "ZZZ":
                return dist


def question_2():
    """Answer to the second question of the day"""

    nodes = file_lines()
    poss, ends = start_ends(nodes.keys())

    return lcm(*[cycle_ends(pos, nodes, ends) for pos in poss])


def start_ends(nodes):
    starts = []
    ends = []

    for node in nodes:
        if node[2] == "A":
            starts.append(node)
        if node[2] == "Z":
            ends.append(node)

    return starts, ends


def cycle_ends(pos, nodes, ends):
    dist = 0
    while True:
        for instruction in instructions:
            pos = right_left(pos, nodes, instruction)
            dist += 1
            if pos in ends:
                return dist


def condition_meet(poss, ends):
    for pos in poss:
        if pos not in ends:
            return False
    return True


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")
